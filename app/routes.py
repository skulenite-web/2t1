from flask import render_template, request, make_response, redirect, url_for
from flask_pymongo import pymongo
from app import app
from app import db

##########################
## DB Collections:      ##
##   - db.people        ##
##   - db.sketches      ##
##########################

# Landing - Intro & Main Page
@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    visited = request.cookies.get('visited')
    if (visited == 'true'):
        # Have visited - skip animation
#        db.people.insert({'name' : 'allison', 'role':'crew'})
        return render_template('watch.html')
    else:
        # New visiton - play animation
        resp = make_response(render_template('intro_animation.html'))
        resp.set_cookie('visited', 'true')
        return resp

## Subpage - force animation
@app.route('/intro')
def intro():
    return render_template('intro_animation.html')

## Subpage: - Direct to watch
@app.route('/watch')
def watch():
    resp = make_response(redirect(url_for('home', _anchor='video')))
    resp.set_cookie('visited', 'true')
    return resp

# Team 
@app.route('/team')
@app.route('/meettheteam')
def team():
    cast = []
    crew = []
    band = []
    creative = []

    for person in db.people.find(sort=[('name', pymongo.ASCENDING)]):
        if (person['role'] == 'cast'):
            cast.append(person)
        elif (person['role'] == 'crew'):
            crew.append(person)
        elif (person['role'] == 'band'):
            band.append(person)
        elif (person['role'] == 'creative'):
            creative.append(person)
    return render_template('team.html', cast=cast, crew=crew, band=band, creative=creative)

@app.route('/cast')
def cast():
    return redirect(url_for('team', _anchor='cast'))
@app.route('/crew')
def crew():
    return redirect(url_for('team', _anchor='crew'))
@app.route('/band')
def band():
    return redirect(url_for('team', _anchor='band'))
@app.route('/creative')
def creative():
    return redirect(url_for('team', _anchor='creative'))

# History
@app.route('/history')
def history():
    return """history"""

# Goodies
@app.route('/goodies')
def goodies():
    return """sketches and lyrics coming soon"""

@app.route('/sketches')
def sketches():
    return redirect(url_for('goodies', _anchor='sketches'))
@app.route('/lyrics')
def lyrics():
    return redirect(url_for('goodies', _anchor='lyrics'))
@app.route('/promo')
def promo():
    return redirect(url_for('goodies', _anchor='promo'))

# Behind the scenes
@app.route('/bts')
@app.route('/BTS')
@app.route('/behindthescenes')
def bts():
    return """behind the scenes content here"""

# 1T00
@app.route('/1t00')
@app.route('/1T00')
def oneteehundred():
    return """1t00 babyyyyy!!!"""

# Contact
@app.route('/contact')
@app.route('/social')
@app.route('/socials')
def contact():
    return """socials and contact info"""


# Error Handling
## 404
@app.errorhandler(404)
def page_not_found(e):
    return """ooops!""", e
