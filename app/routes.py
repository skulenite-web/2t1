from flask import render_template, request, make_response, redirect, url_for
from flask_pymongo import pymongo
from wtforms import Form, StringField, TextAreaField, validators
from datetime import datetime
from pytz import timezone
from app import app
from app import db

##########################
## DB Collections:      ##
##   - db.people        ##
##   - db.sketches      ##
##   - db.lyrics        ##
##   - db.history       ##
##   - db.comments      ##
##########################

##########################
####### FORM CLASS #######
##########################

class CommentForm(Form):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=100)])
    #email = StringField('Email Address', [validators.DataRequired(), validators.Email()])
    uoft = StringField('Grad Year (optional)')
    comment = TextAreaField('Comment', [validators.DataRequired(), validators.Length(min=1, max=300)])

# Security
@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

def headersify(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubdomains'
    response.cache_control.max_age = 172800
    return response

#############
### PAGES ###
#############

# Legacy - Coming Soon page
@app.route('/comingsoon')
def comingsoon():
    resp = make_response(render_template('comingsoon.html'))
    return headersify(resp)

# Landing - Intro & Main Page
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/watch', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = CommentForm(request.form)
    if (request.method == 'POST' and form.validate()):
        tz = timezone('US/Eastern')
        comment = {
            'name'      :   form.name.data,
            #'email'     :   form.email.data,
            'uoft'      :   form.uoft.data,
            'comment'   :   form.comment.data,
            'datetime'  :   datetime.now(tz),
            'date-readable' : datetime.now(tz).strftime('%B %-d at %H:%M'),
            'approved' :   'false'
        }
        db.comments.insert_one(comment)
        return 'SUCCESS'
    if (request.method == 'POST' and not form.validate()):
        return 'FAILURE'
    comments = []
    for comment in db.comments.find(sort=[('datetime', pymongo.DESCENDING)]):
        if (comment['approved'] == 'true' or comment['approved'] == 'yes'):
            comments.append(comment)
    resp = make_response(render_template('watch.html', form=form, comments=comments))
    return headersify(resp)


# Team 
@app.route('/team')
@app.route('/meettheteam')
def team():
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

    resp = make_response(render_template('team.html', cast=cast, crew=crew, band=band, creative=creative, marketing=marketing, writers=writers))
    return headersify(resp)

@app.route('/cast')
def cast():
    return redirect(url_for('team', _anchor='cast'))
@app.route('/band')
def band():
    return redirect(url_for('team', _anchor='band'))
@app.route('/crew')
def crew():
    return redirect(url_for('team', _anchor='crew'))
@app.route('/marketing')
def marketing():
    return redirect(url_for('team', _anchor='marketing'))
@app.route('/creative')
def creative():
    return redirect(url_for('team', _anchor='creative'))


# History
@app.route('/history')
@app.route('/timeline')
def history():
    events = []
    for event in db.history.find(sort=[('order', pymongo.ASCENDING)]):
        events.append(event)
    resp = make_response(render_template('timeline.html', events=events))
    return headersify(resp)


# Goodies
@app.route('/goodies')
def goodies():

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
    
    resp = make_response(render_template('goodies.html', sketches=sketches, songs=songs))
    return headersify(resp)

@app.route('/sketches')
def sketches():
    return redirect(url_for('goodies', _anchor='sketches'))
@app.route('/lyrics')
def lyrics():
    return redirect(url_for('goodies', _anchor='lyrics'))


@app.route('/programme')
def programme():
    resp = make_response(render_template('programme.html'))
    return headersify(resp)

# Donor Thanks
@app.route('/donors')
def donors():
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

    resp = make_response(render_template('donors.html', prodro=prodro, legend=legend, fossil=fossil, flunky=flunky))
    return headersify(resp)


# Error Handling
## 404
@app.errorhandler(404)
def page_not_found(e):
    resp = make_response(render_template('error.html'))
    return headersify(resp), 404
