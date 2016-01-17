from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask import Flask, jsonify, abort, make_response, request, url_for, g, render_template, session
from pprint import pprint
import requests, os, urllib,cStringIO


@app.route('/')
def index():
    CONSUMER_ID = ???? #hidden for security
    return redirect('https://api.venmo.com/v1/oauth/authorize?client_id=%s&scope=make_payments,access_profile&response_type=token' % CONSUMER_ID)

@app.route('/oauth-authorized', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        AUTHORIZATION_CODE = request.args.get('code')
        data = {
        "client_id":???,
        "client_secret":'vXpe8uzQZWs6mAEEbSUwWz3FYP8SJaZJ',
        "code":AUTHORIZATION_CODE
        }
        
        date1 = form.openid.data.split(' ')
        date2 = form.openid2.data.split(' ')
        start = date1[2] + "-" + date1[0] + "-" + date1[1]+"T00:00:00"
        end = date2[2] + "-" + date2[0] + "-" + date2[1]+"T23:59:59"
        url = "https://api.venmo.com/v1/oauth/access_token"
        response = requests.post(url, data)
        response_dict = response.json()
        print(response_dict)
        #url = 'https://api.venmo.com/v1/oauth/authorize?client_id=????&scope=make_payments%20access_profile&response_type=token'
        access_token = response_dict.get('access_token')
        #print(r)
        url = 'https://api.venmo.com/v1/payments?access_token=49f5f5100703d53424a7e585146cb76260188edb37aab9447d472d45ecd4476f&date_created=' + 'start&date_completed=' + 'end'
        r = requests.get(url)
        response = r.json()
        pprint(response)
        f = open('ledger.txt', 'w')
        
        length = len(response['data'])
        #print(length)
        for number in range(0, length):
            f.write("%s \n" %response['data'][number]['amount'])
        

        f.close()
       
        return redirect('/submit')

    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           )
@app.route('/submit')
def submit():
    return "Thank you!!!"
