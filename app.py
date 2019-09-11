from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow_sqlalchemy import ModelSchema
from extensions import db
from models import Houses
from schemas import HouseSchema

url = "postgres://postgres:postgres@localhost:5432/house_db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/houses/<id>')
def get_house_by_id(id):
    house = Houses.query.get(id)
    json_house = HouseSchema().dump(house)
    return jsonify(json_house)

@app.route("/houses")
def get_houses():
    min_sell_price = request.args.get('min_sell_price')
    max_sell_price = request.args.get('max_sell_price')
    min_list_price = request.args.get('min_list_price')
    max_list_price = request.args.get('max_list_price')
    min_living_size = request.args.get('min_living_size')
    max_living_size = request.args.get('max_living_size')
    min_rooms_num = request.args.get('min_rooms_num')
    max_rooms_num = request.args.get('max_rooms_num')
    min_beds_num = request.args.get('min_beds_num')
    max_beds_num = request.args.get('max_beds_num')
    min_baths_num = request.args.get('min_baths_num')
    max_baths_num = request.args.get('max_baths_num')
    min_age = request.args.get('min_age')
    max_age = request.args.get('max_age')
    min_acres = request.args.get('min_acres')
    max_acres = request.args.get('max_acres')
    min_taxes = request.args.get('min_taxes')
    max_taxes = request.args.get('max_taxes')


    query = Houses.query

    if min_sell_price is not None:
        query = query.filter(Houses.sell_price >= min_sell_price)
    if max_sell_price is not None:
        query = query.filter(Houses.sell_price <= max_sell_price)
    if min_sell_price is not None and max_sell_price is not None:
        query = query.filter(Houses.sell_price >= min_sell_price, Houses.sell_price <= max_sell_price)
    if min_list_price is not None:
        query = query.filter(Houses.list_price >= min_list_price)
    if max_list_price is not None:
        query = query.filter(Houses.list_price <= max_list_price)
    if min_list_price is not None and max_list_price is not None:
        query = query.filter(Houses.list_price >= min_list_price, Houses.list_price <= max_list_price)
    if min_living_size is not None:
        query = query.filter(Houses.living_size >= min_living_size)
    if max_living_size is not None:
        query = query.filter(Houses.living_size <= max_living_size)
    if min_living_size is not None and max_living_size is not None:
        query = query.filter(Houses.living_size >= min_living_size, Houses.living_size <= max_living_size)
    if min_rooms_num is not None:
        query = query.filter(Houses.rooms_num >= min_rooms_num)
    if max_rooms_num is not None:
        query = query.filter(Houses.rooms_num <= max_rooms_num)
    if min_rooms_num is not None and max_rooms_num is not None:
        query = query.filter(Houses.rooms_num >= min_rooms_num, Houses.rooms_num <= max_rooms_num)
    if min_beds_num is not None:
        query = query.filter(Houses.beds_num >= min_beds_num)
    if max_beds_num is not None:
        query = query.filter(Houses.beds_num <= max_beds_num)
    if min_beds_num is not None and max_beds_num is not None:
        query = query.filter(Houses.beds_num >= min_beds_num, Houses.beds_num <= max_beds_num)
    if min_baths_num is not None:
        query = query.filter(Houses.baths_num >= min_baths_num)
    if max_baths_num is not None:
        query = query.filter(Houses.baths_num <= max_baths_num)
    if min_baths_num is not None and max_baths_num is not None:
        query = query.filter(Houses.baths_num >= min_baths_num, Houses.baths_num <= max_baths_num)
    if min_age is not None:
        query = query.filter(Houses.age >= min_age)
    if max_age is not None:
        query = query.filter(Houses.age <= max_age)
    if min_age is not None and max_age is not None:
        query = query.filter(Houses.age >= min_age, Houses.age <= max_age)
    if min_acres is not None:
        query = query.filter(Houses.acres >= min_acres)
    if max_acres is not None:
        query = query.filter(Houses.acres <= max_acres)
    if min_acres is not None and max_acres is not None:
        query = query.filter(Houses.acres >= min_acres, Houses.acres <= max_acres)
    if min_taxes is not None:
        query = query.filter(Houses.taxes >= min_taxes)
    if max_taxes is not None:
        query = query.filter(Houses.taxes <= max_taxes)
    if min_taxes is not None and max_taxes is not None:
        query = query.filter(Houses.taxes >= min_taxes, Houses.taxes <= max_taxes)

    houses = query.all()
    json_houses = HouseSchema(many=True).dump(houses)

    return jsonify(json_houses)    

app.run(debug=True)

