from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask import Flask, jsonify, abort, make_response, request, url_for, g, render_template
from pprint import pprint
import requests, os, urllib,cStringIO




@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        date1 = form.openid.data.split(' ')
        date2 = form.openid2.data.split(' ')
        start = date1[2] + "-" + date1[0] + "-" + date1[1]+"T00:00:00"
        end = date2[2] + "-" + date2[0] + "-" + date2[1]+"T23:59:59"
        print(start)
        #url = 'https://api.venmo.com/v1/oauth/authorize?client_id=3363&scope=make_payments%20access_profile&response_type=token'
        #r = requests.request(url)
        #print(r)
        url = 'https://api.venmo.com/v1/payments?access_token=3ca8f765f9b4b3ba73e9d515fce5b2d56d30ead7d8cb861747c0832327d2cf4a&date_created=' + 'start&date_completed=' + 'end'
        
        r = requests.get(url)
        response = r.json()
        pprint(response)
        #length = len(response['data'])
        #print(length)
        #for number in range(0, length):
        #	pprint(response['data'][number]['amount'])
        return redirect('/submit')

    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           )
@app.route('/submit')
def submit():
    return "Thank you!!!"
