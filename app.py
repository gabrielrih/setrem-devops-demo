import json

from typing import Dict
from http import HTTPStatus
from flask import Flask, jsonify, redirect, render_template, request

from src.foods import Foods, FoodSchema


app = Flask(__name__)
foods = Foods()


class ResponseError:
    @staticmethod
    def as_dict(code: int = HTTPStatus.BAD_REQUEST, 
                message: str = 'General error') -> Dict:
        return {
            "error": {
                "code": code,
                "message": message
            }
        }


# Redirect
@app.route('/')
def index():
    return redirect('/home')


# Web Site
@app.route('/home')
def home():
    items = foods.get_all()
    return render_template('index.html', items=items)


# APIs
@app.route("/api/food/", methods=['GET'])
def get_foods():
    name = request.args.get('name')
    if name:
        return jsonify(foods.get_food_by_name(name)), HTTPStatus.OK
    return jsonify(foods.get_all()), HTTPStatus.OK


@app.route("/api/food/", methods=['POST'])
def add_food():
    content_type = request.content_type
    if content_type != 'application/json':
        error_code = HTTPStatus.BAD_REQUEST
        response = ResponseError().as_dict(code=error_code,
                                           message=f'Content-Type {content_type} not supported! Must be application/json')
        return response, HTTPStatus.BAD_REQUEST
    body = request.data
    if not body:
        error_code = HTTPStatus.BAD_REQUEST
        response = ResponseError().as_dict(code=error_code,
                                           message='Body cannot be empty!')
        return response, error_code
    try:
        schema = FoodSchema()
        content = request.get_json()
        schema.load(content)
    except Exception:
        error_code = HTTPStatus.BAD_REQUEST
        response = ResponseError().as_dict(code=error_code,
                                           message='Invalid schema! Failed to parse it.')
        return response, error_code
    # Add food on the database
    foods.add_food(content)
    return content, HTTPStatus.CREATED
