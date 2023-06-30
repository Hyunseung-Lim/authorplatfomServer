# -*- coding: utf-8 -*-
from flask import Blueprint, current_app, redirect, url_for, request, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from __init__ import create_app, db
import json
import requests

main = Blueprint('main', __name__)


@main.route("/get_lucy_answer", methods=['POST'])
@cross_origin()
def get_lucy_answer():
    params = request.get_json()
    question = params['question']
    title = params['title']
    response =  requests.post('https://lucydata.lgresearch.ai/get_lucy_answer', headers = {'Content-Type': 'application/json'}, data = json.dumps({'question': question, 'title': title}))
    return {"lucy_answer": response.json()['lucy_answer']}

app = create_app()
if __name__ == '__main__':
    db.create_all(app=create_app())
    app.run(debug=True)