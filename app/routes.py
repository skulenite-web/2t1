from flask import render_template, request, make_response, redirect, url_for
from flask_pymongo import pymongo
from wtforms import Form, StringField, TextAreaField, validators
import datetime
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
    email = StringField('Email Address', [validators.DataRequired(), validators.Email()])
    uoft = StringField('Grad Year (optional)', [validators.Length(min=3, max=15)])
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

# Landing - Intro & Main Page
@app.route('/')
def comingsoon():
    resp = make_response(render_template('comingsoon.html'))
    return headersify(resp)

@app.route('/shallnotpass/index')
@app.route('/shallnotpass/watch')
@app.route('/shallnotpass/home', methods=['GET', 'POST'])
def home():
    form = CommentForm(request.form)
    if (request.method == 'POST' and form.validate()):
        comment = {
            'name'      :   form.name.data,
            'email'     :   form.email.data,
            'uoft'      :   form.uoft.data,
            'comment'   :   form.comment.data
        }
        db.comments.insert_one(comment)
        #flash('Thanks for submitting your comment!')
        return redirect(url_for('home'))
    resp = make_response(render_template('watch.html', form=form))
    return headersify(resp)


# Team 
@app.route('/shallnotpass/team')
@app.route('/shallnotpass/meettheteam')
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

@app.route('/shallnotpass/cast')
def cast():
    return redirect(url_for('team', _anchor='cast'))
@app.route('/shallnotpass/band')
def band():
    return redirect(url_for('team', _anchor='band'))
@app.route('/shallnotpass/crew')
def crew():
    return redirect(url_for('team', _anchor='crew'))
@app.route('/shallnotpass/marketing')
def marketing():
    return redirect(url_for('team', _anchor='marketing'))
@app.route('/shallnotpass/creative')
def creative():
    return redirect(url_for('team', _anchor='creative'))


# History
@app.route('/shallnotpass/history')
@app.route('/shallnotpass/timeline')
def history():
    events = []
    for event in db.history.find(sort=[('order', pymongo.ASCENDING)]):
        events.append(event)
    resp = make_response(render_template('timeline.html', events=events))
    return headersify(resp)


# Goodies
@app.route('/shallnotpass/goodies')
def goodies():

    sketches = []
    for sketch in db.sketches.find(sort=[('order', pymongo.ASCENDING)]):
        sketch['title'] = sketch['title'].upper()
        sketch['display_title'] = ' '.join(sketch['title'].split('_')).upper()
        sketches.append(sketch)
    songs = []
    songs.append({'title':'song1'})
    
    resp = make_response(render_template('goodies.html', sketches=sketches, songs=songs))
    return headersify(resp)

@app.route('/shallnotpass/sketches')
def sketches():
    return redirect(url_for('goodies', _anchor='sketches'))
@app.route('/shallnotpass/lyrics')
def lyrics():
    return redirect(url_for('goodies', _anchor='lyrics'))
@app.route('/shallnotpass/promo')
def promo():
    return redirect(url_for('goodies', _anchor='promo'))


# Donor Thanks
@app.route('/shallnotpass/donors')
def donors():
    resp = make_response(render_template('donors.html'))
    return headersify(resp)


# Error Handling
## 404
@app.errorhandler(404)
def page_not_found(e):
    return """ooops!""", e
