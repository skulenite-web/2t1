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
def comingsoon():
    return render_template('comingsoon.html')

@app.route('/shallnotpass/index')
@app.route('/shallnotpass/home')
def home():
    visited = request.cookies.get('visited')
    if (visited == 'true'):
        # Have visited - skip animation
        return render_template('watch.html')
    else:
        # New visitor - play animation
        resp = make_response(render_template('intro_animation.html'))
        resp.set_cookie('visited', 'true')
        return resp

## Subpage - force animation
@app.route('/shallnotpass/intro')
def intro():
    return render_template('intro_animation.html')

## Subpage: - Direct to watch
@app.route('/shallnotpass/watch')
def watch():
    resp = make_response(redirect(url_for('home', _anchor='video')))
    resp.set_cookie('visited', 'true')
    return resp

# Team 
@app.route('/shallnotpass/team')
@app.route('/shallnotpass/meettheteam')
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

@app.route('/shallnotpass/cast')
def cast():
    return redirect(url_for('team', _anchor='cast'))
@app.route('/shallnotpass/crew')
def crew():
    return redirect(url_for('team', _anchor='crew'))
@app.route('/shallnotpass/band')
def band():
    return redirect(url_for('team', _anchor='band'))
@app.route('/shallnotpass/creative')
def creative():
    return redirect(url_for('team', _anchor='creative'))

# History
@app.route('/shallnotpass/history')
def history():
    return """history"""

# Goodies
@app.route('/shallnotpass/goodies')
def goodies():
    sketch = [{'character':'Alice', 'line':'Hey Bob!'}, {'character':'Bob', 'line':'Alice, what the fuck are you doing here!?'}]
    
    return render_template('goodies.html', sketch=sketch)

@app.route('/shallnotpass/sketches')
def sketches():
    return redirect(url_for('goodies', _anchor='sketches'))
@app.route('/shallnotpass/lyrics')
def lyrics():
    return redirect(url_for('goodies', _anchor='lyrics'))
@app.route('/shallnotpass/promo')
def promo():
    return redirect(url_for('goodies', _anchor='promo'))

# Behind the scenes
@app.route('/shallnotpass/bts')
@app.route('/shallnotpass/BTS')
@app.route('/shallnotpass/behindthescenes')
def bts():
    return """behind the scenes content here"""

# Donor Thanks
@app.route('/shallnotpass/thanks')
@app.route('/shallnotpass/1t00')
@app.route('/shallnotpass/1T00')
def thanks():
    return """1t00 babyyyyy!!!"""

# Contact
@app.route('/shallnotpass/contact')
@app.route('/shallnotpass/social')
@app.route('/shallnotpass/socials')
def contact():
    return """socials and contact info"""


# Error Handling
## 404
@app.errorhandler(404)
def page_not_found(e):
    return """ooops!""", e
