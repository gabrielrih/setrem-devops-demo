from http import HTTPStatus
from flask import Flask, jsonify, redirect, render_template, request
from marshmallow import ValidationError

from src.foods import Foods, FoodSchema


app = Flask(__name__)
foods = Foods()


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
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        response = {
            "error": {
                "code": HTTPStatus.BAD_REQUEST,
                "message": 'Content-Type not supported! Support ones: application/json'
            }
        }
        return response, HTTPStatus.BAD_REQUEST
    content = request.json
    if not content:
        response = {
            "error": {
                "code": HTTPStatus.BAD_REQUEST,
                "message": 'Body cannot be empty!'
            }
        }
        return response, HTTPStatus.BAD_REQUEST
    # Validate request body against schema data types
    schema = FoodSchema()
    try:
        schema.load(content)
    except ValidationError as error:
        return jsonify(error.messages), HTTPStatus.BAD_REQUEST
    foods.add_food(content)
    return content, HTTPStatus.CREATED
