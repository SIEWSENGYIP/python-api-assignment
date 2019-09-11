import csv
from models import Houses
from extensions import db
from app import app

with open("houses.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        x = Houses()

        x.sell_price = row["Sell"]
        x.list_price = row[' "List"'].replace(" ", "")
        x.living_size = row[' "Living"'].replace(" ", "")
        x.rooms_num = row[' "Rooms"'].replace(" ", "")
        x.beds_num = row[' "Beds"'].replace(" ", "")
        x.baths_num = row[' "Baths"'].replace(" ", "")
        x.age = row[' "Age"'].replace("  ", "")
        x.acres = row[' "Acres"'].replace(" ", "")
        x.taxes = row[' "Taxes"'].replace("  ", "")
        
        with app.app_context():
            db.session.add(x)
            db.session.commit()