import os
from flask import Flask
from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://dev:FLASKPASS@cluster.kmcxs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# Connect
client = pymongo.MongoClient(CONNECTION_STRING)
db = client['2t1db']

# Set up collections
people = db.people
sketches = db.sketches
lyrics = db.lyrics
history = db.history
comments = db.comments
donors = db.donors


# GOODIES PAGE:
# FILL LISTS
sketches = []
for sketch in db.sketches.find(sort=[('order', pymongo.ASCENDING)]):
    sketch['title'] = sketch['title'].upper()
    sketch['display_title'] = ' '.join(sketch['title'].split('_')).upper()
    sketches.append(sketch)
songs = []
for song in db.lyrics.find(sort=[('order', pymongo.ASCENDING)]):
    song['display_title'] = song['title'].upper()
    song['title'] = '_'.join(song['title'].split(' ')).upper().replace('(', '').replace(')', '').replace("’", '').replace('!', '').replace(',', '')
    songs.append(song)

# DONORS PAGE: 
# FILL LISTS
prodro = []
legend = []
fossil = []
flunky = []

for donor in db.donors.find(sort=[('name', pymongo.ASCENDING)]):
    if (donor['type'] == 'prodro'):
        prodro.append(donor['name'])
    elif (donor['type'] == 'legend'):
        legend.append(donor['name'])
    elif (donor['type'] == 'fossil'):
        fossil.append(donor['name'])
    elif (donor['type'] == 'flunky'):
        flunky.append(donor['name'])

# TIMELINE PAGE: 
# FILL LISTS:
events = []
for event in db.history.find(sort=[('order', pymongo.ASCENDING)]):
    events.append(event)

# TEAM PAGE:
cast = []
crew = []
band = []
creative = []
marketing = []
writers = []

for person in db.people.find(sort=[('order', pymongo.ASCENDING)]):
    if (person['role'].lower() == 'cast'):
        person['img'] = '_'.join(person['name'].strip().lower().split(' '))
        cast.append(person)
    elif (person['role'].lower() == 'crew'):
        person['img'] = '_'.join(person['name'].strip().lower().split(' '))
        crew.append(person)
    elif (person['role'].lower() == 'band'):
        person['img'] = '_'.join(person['name'].strip().lower().split(' '))
        band.append(person)
    elif (person['role'].lower() == 'creative'):
        person['img'] = '_'.join(person['name'].strip().lower().split(' '))
        creative.append(person)
    elif (person['role'].lower() == 'marketing'):
        person['img'] = '_'.join(person['name'].strip().lower().split(' '))
        marketing.append(person)
    elif (person['role'].lower() == 'writer'):
        writers.append(person['name'])

comments = []
for comment in db.comments.find(sort=[('datetime', pymongo.DESCENDING)]):
    if (comment['approved'] == 'true' or comment['approved'] == 'yes'):
        comments.append(comment)

# FILE OUTPUT
with open('DB_OUTPUT.html', 'w') as f:
    for comment in comments:
        f.write("                            <div class='comment-item pb-2'>\n")
        f.write("                                <span class='fs-5 fw-bold'>"+comment['name'])
        if (comment['uoft'] != ''):
            f.write(" ("+comment['uoft']+")")
        f.write("</span><span class='float-end fs-6 fst-italic text-muted'>"+comment['date-readable']+"</span>\n")
        f.write("                                <p class='fs-6'>"+comment['comment']+"</p>\n")
        f.write("                            </div>\n")
    
    # TEAM:
    # f.write("CAST PHOTO:::::\n")
    # for person in cast:
    #     if (person['no-photo'] == 'false'):
    #         f.write("                        <div class='col'>\n")
    #         f.write("                          <div class='mx-auto card flip-card text-dark mb-4 g-0 show-on-scroll'>\n")
    #         f.write("                            <div class='flip-inner shadow'>\n")
    #         f.write("                              <div class='card-img flip-front bg-light'>\n")
    #         f.write("                                <img src=\"img/team/"+person['img']+".JPG\" class='card-img-top' alt='Photo of "+person['name']+"'>\n")
    #         f.write("                              </div>\n")
    #         f.write("                              <div class='card-body flip-back bg-light d-flex flex-column justify-content-center handwritten'>\n")
    #         f.write("                                <h3 class='card-title text-center fs-1'>"+person['name']+"</h5>\n")
    #         f.write("                                <p class='card-text text-center sub-font fs-5' style=\"font-weight: 300;\">"+person['blurb']+"</p>\n")
    #         f.write("                              </div>\n")
    #         f.write("                            </div>\n")
    #         f.write("                          </div>\n")
    #         f.write("                        </div>\n")

    # f.write("CAST NOPHOTO:::::\n")
    # for person in cast:
    #     if (person['no-photo'] == 'true'):
    #         f.write("                        <span class='name-credit sub-font fs-3 mx-1'>"+person['name']+","+person['title']+"</span>\n")
    #         f.write("                        <span class='name-credit-separator sub-font fs-3 mx-1'> • </span>\n")


    # f.write("BAND PHOTO:::::\n")
    # for person in band:
    #     if (person['no-photo'] == 'false'):
    #         f.write("                        <div class='col'>\n")
    #         f.write("                          <div class='mx-auto card flip-card text-dark mb-4 g-0 show-on-scroll'>\n")
    #         f.write("                            <div class='flip-inner shadow'>\n")
    #         f.write("                              <div class='card-img flip-front bg-light'>\n")
    #         f.write("                                <img src=\"img/team/"+person['img']+".JPG\" class='card-img-top' alt='Photo of "+person['name']+"'>\n")
    #         f.write("                              </div>\n")
    #         f.write("                              <div class='card-body flip-back bg-light d-flex flex-column justify-content-center handwritten'>\n")
    #         f.write("                                <h5 class='card-title text-center fs-1'>"+person['name']+"</h5>\n")
    #         f.write("                                <p class='card-text text-center fs-3'>"+person['title']+"</p>\n")
    #         f.write("                              </div>\n")
    #         f.write("                            </div>\n")
    #         f.write("                          </div>\n")
    #         f.write("                        </div>\n")

    # f.write("BAND NOPHOTO:::::\n")
    # for person in band:
    #     if (person['no-photo'] == 'true'):
    #         f.write("                        <span class='name-credit sub-font fs-3 mx-1'>"+person['name']+","+person['title']+"</span>\n")
    #         f.write("                        <span class='name-credit-separator sub-font fs-3 mx-1'> • </span>\n")


    # f.write("CREW PHOTO:::::\n")
    # for person in crew:
    #     if (person['no-photo'] == 'false'):
    #         f.write("                        <div class='col'>\n")
    #         f.write("                          <div class='mx-auto card flip-card text-dark mb-4 g-0 show-on-scroll'>\n")
    #         f.write("                            <div class='flip-inner shadow'>\n")
    #         f.write("                              <div class='card-img flip-front bg-light'>\n")
    #         f.write("                                <img src=\"img/team/"+person['img']+".JPG\" class='card-img-top' alt='Photo of "+person['name']+"'>\n")
    #         f.write("                              </div>\n")
    #         f.write("                              <div class='card-body flip-back bg-light d-flex flex-column justify-content-center handwritten'>\n")
    #         f.write("                                <h5 class='card-title text-center fs-1'>"+person['name']+"</h5>\n")
    #         f.write("                                <p class='card-text text-center fs-3'>"+person['title']+"</p>\n")
    #         f.write("                              </div>\n")
    #         f.write("                            </div>\n")
    #         f.write("                          </div>\n")
    #         f.write("                        </div>\n")

    # f.write("CREW NOPHOTO:::::\n")
    # for person in crew:
    #     if (person['no-photo'] == 'true'):
    #         f.write("                        <span class='name-credit sub-font fs-3 mx-1'>"+person['name']+","+person['title']+"</span>\n")
    #         f.write("                        <span class='name-credit-separator sub-font fs-3 mx-1'> • </span>\n")


    # f.write("MARKETING PHOTO:::::\n")
    # for person in marketing:
    #     if (person['no-photo'] == 'false'):
    #         f.write("                        <div class='col'>\n")
    #         f.write("                          <div class='mx-auto card flip-card text-dark mb-4 g-0 show-on-scroll'>\n")
    #         f.write("                            <div class='flip-inner shadow'>\n")
    #         f.write("                              <div class='card-img flip-front bg-light'>\n")
    #         f.write("                                <img src=\"img/team/"+person['img']+".JPG\" class='card-img-top' alt='Photo of "+person['name']+"'>\n")
    #         f.write("                              </div>\n")
    #         f.write("                              <div class='card-body flip-back bg-light d-flex flex-column justify-content-center handwritten'>\n")
    #         f.write("                                <h5 class='card-title text-center fs-1'>"+person['name']+"</h5>\n")
    #         f.write("                                <p class='card-text text-center fs-3'>"+person['title']+"</p>\n")
    #         f.write("                              </div>\n")
    #         f.write("                            </div>\n")
    #         f.write("                          </div>\n")
    #         f.write("                        </div>\n")

    # f.write("MARKETING NOPHOTO:::::\n")
    # for person in marketing:
    #     if (person['no-photo'] == 'true'):
    #         f.write("                        <span class='name-credit sub-font fs-3 mx-1'>"+person['name']+","+person['title']+"</span>\n")
    #         f.write("                        <span class='name-credit-separator sub-font fs-3 mx-1'> • </span>\n")


    # f.write("CREATIVE PHOTO:::::\n")
    # for person in creative:
    #     if (person['no-photo'] == 'false'):
    #         f.write("                        <div class='col'>\n")
    #         f.write("                          <div class='mx-auto card flip-card text-dark mb-4 g-0 show-on-scroll'>\n")
    #         f.write("                            <div class='flip-inner shadow'>\n")
    #         f.write("                              <div class='card-img flip-front bg-light'>\n")
    #         f.write("                                <img src=\"img/team/"+person['img']+".JPG\" class='card-img-top' alt='Photo of "+person['name']+"'>\n")
    #         f.write("                              </div>\n")
    #         f.write("                              <div class='card-body flip-back bg-light d-flex flex-column justify-content-center handwritten'>\n")
    #         f.write("                                <h5 class='card-title text-center fs-1'>"+person['name']+"</h5>\n")
    #         f.write("                                <p class='card-text text-center fs-3'>"+person['title']+"</p>\n")
    #         f.write("                              </div>\n")
    #         f.write("                            </div>\n")
    #         f.write("                          </div>\n")
    #         f.write("                        </div>\n")

    # f.write("CREATIVE NOPHOTO:::::\n")
    # for person in creative:
    #     if (person['no-photo'] == 'true'):
    #         f.write("                        <span class='name-credit sub-font fs-3 mx-1'>"+person['name']+","+person['title']+"</span>\n")
    #         f.write("                        <span class='name-credit-separator sub-font fs-3 mx-1'> • </span>\n")


    # f.write("WRITERS:::::\n")
    
    # for writer in writers:
    #     f.write("                        <span class='name-credit sub-font fs-4 mx-1'>"+writer+"</span>\n")
    #     f.write("                        <span class='name-credit-separator sub-font fs-4 mx-1'> • </span>\n")




    # TIMELINE: 
    # f.write("FIRST FOR (d-none)::::::\n")

    # for event in events:
    #     f.write("                        <div class='timeline-item'>\n")
    #     f.write("                            <div class='card shadow script translate-middle-y")
    #     if (event['date'] == '2021'):
    #         f.write(" mb-2")
    #     else: 
    #         f.write(" mb-1")
    #     f.write("' style='max-width: 50%;'>\n")
    #     f.write("                                <div class='card-body'>\n")
    #     f.write("                                    <h5 class='fw-bold card-title'>"+event['date']+"</h5>\n")
    #     f.write("                                    <ul>\n")
    #     for desc in event['description']:
    #         f.write("                                        <li class='card-text'>"+desc+"</li>\n")
    #     f.write("                                    </ul>\n")
    #     f.write("                                </div>\n")
    #     f.write("                            </div>\n")
    #     f.write("                        </div>\n")
    

    # f.write("\n\n\n\n\nSECOND FOR (d-flex)::::::\n")

    # for event in events:
    #     f.write("                        <div class='row mb-3'>\n")
    #     f.write("                            <div class='card shadow script")
    #     if (event['date'] == '2021'):
    #         f.write(" mb-2'>\n")
    #     else: 
    #         f.write(" mb-1'>\n")
    #     f.write("                                <div class='card-body'>\n")
    #     f.write("                                    <h5 class='fw-bold card-title'>"+event['date']+"</h5>\n")
    #     f.write("                                    <ul>\n")
    #     for desc in event['description']:
    #         f.write("                                        <li class='card-text'>"+desc+"</li>\n")
    #     f.write("                                    </ul>\n")
    #     f.write("                                </div>\n")
    #     f.write("                            </div>\n")
    #     f.write("                        </div>\n")
    
    
    
    
    # DONORS:
    # f.write("PRODRO::::\n")
    # for donor in prodro:
    #     f.write("                        <span class='col-12 col-xs-6 col-md-4 col-xl-3 sub-font fs-4 mx-3'>"+donor+"</span>\n")
    # f.write("\n\n\n")
    # f.write("LEGEND::::\n")
    # for donor in legend:
    #     f.write("                        <span class='col-12 col-xs-6 col-md-4 col-xl-3 sub-font fs-4 mx-3'>"+donor+"</span>\n")
    # f.write("\n\n\n")
    # f.write("FOSSIL::::\n")
    # for donor in fossil:
    #     f.write("                        <span class='col-12 col-xs-6 col-md-4 col-xl-3 sub-font fs-4 mx-3'>"+donor+"</span>\n")
    # f.write("\n\n\n")
    # f.write("FLUNKY::::\n")
    # for donor in flunky:
    #     f.write("                        <span class='col-12 col-xs-6 col-md-4 col-xl-3 sub-font fs-4 mx-3'>"+donor+"</span>\n")
    # f.write("\n\n\n")



    # GOODIES:
    # f.write("AT LINE 82:\n")
    # for sketch in sketches:
    #     f.write("                                                <li><a class='dropdown-item' onclick=\"switchSketch('"+sketch['title']+"', '"+sketch['display_title']+"');\">"+sketch['display_title']+"</a></li>\n")
    # f.write("\n\n\n")

    # f.write("AT LINE 95:\n")
    # for sketch in sketches: 
    #     f.write("                                    <div class='sketch-script-text d-flex flex-column text-center ")
    #     if (sketch['title'] != sketches[0]['title']):
    #         f.write("d-none")
    #     f.write("' id='"+sketch['title']+"'>\n")
    #     for line in sketch['script']:
    #         f.write("                                      <p class='script-"+line['type']+" ")
    #         if (line['type'] == 'dial' or line['type'] == 'dial-ital'):
    #             f.write("align-self-center")
    #         f.write("'> "+line['text']+" </p>\n")
    # f.write("\n\n\n")


    # f.write("AT LINE 122:\n")
    # for song in songs:
    #     f.write("                                                <li><a class='dropdown-item' onclick=\"switchSong('"+song['title']+"', '"+song['display_title']+"');\">"+song['display_title']+"</a></li>\n")
    # f.write("\n\n\n")

    
    # f.write("AT LINE 136:\n")
    # for song in songs:
    #     f.write("                                    <div class='song-script-text d-flex flex-column text-center ")
    #     if (song['title'] != songs[0]['title']):
    #         f.write("d-none")
    #     f.write("' id='"+song['title']+"'>\n")
    #     for line in song['lines']:
    #         f.write("                                      <p class='mb-1 align-self-center' style='width: 60%'>"+line+"</p>\n")
    # f.write("\n\n\n")