from flask import Blueprint, render_template, request
from sqlalchemy import func, DATE, cast, Integer
from datetime import datetime, timedelta
from Main.utils import *
from Main.SQL import deaths_vs_supply_per_warehouse, payments_per_farm
import calendar
import json

blueprints = Blueprint('blueprints', '__name__')


@blueprints.route('/')
def index():
    result = db.engine.execute(deaths_vs_supply_per_warehouse)
    cards = result.mappings().all()
    print(cards)

    result = db.engine.execute(payments_per_farm)
    finances = result.mappings().all()
    print(finances)

    deaths = db.session.query(Deaths).with_entities(Warehouses.name, db.func.sum(Deaths.deaths_num)).join(
        Warehouses).group_by(Warehouses.name).order_by(Warehouses.name).all()
    totals = db.session.query(Supply).with_entities(Warehouses.name, db.func.sum(Supply.chicken_added)).join(
        Warehouses).group_by(Warehouses.name).order_by(Warehouses.name).all()

    today = datetime.today()

    deaths_this_week = db.session.query(Deaths).with_entities(db.func.sum(Deaths.deaths_num)).filter(
        Deaths.date.between(today - timedelta(weeks=1), today)).first()[0]
    deaths_yesterday = db.session.query(Deaths).with_entities(db.func.sum(Deaths.deaths_num)).filter(
        Deaths.date.between(today - timedelta(days=1), today)).first()[0]

    deaths_this_week = 0 if deaths_this_week is None else deaths_this_week
    deaths_yesterday = 0 if deaths_yesterday is None else deaths_yesterday

    deaths_yesterday_pct = (deaths_yesterday / deaths_this_week) * 100

    data = db.session.query(Deaths). \
        with_entities(db.func.sum(Deaths.deaths_num), cast(func.extract("dow", Deaths.date), Integer)). \
        group_by(Deaths.date). \
        filter(Deaths.date.between(today - timedelta(weeks=1), today)). \
        order_by(Deaths.date).all()

    labels = json.dumps([str(calendar.day_name[i[1]]) for i in data])
    points = json.dumps([int(i[0]) for i in data])

    def fill_feed(date, w, bags, time_of_day):
        date = datetime.strptime(date, '%d/%m/%Y').date()
        feed = Feeding(farm_id=1, warehouse_id=w, date=date, bags_consumed=bags, time_of_day=time_of_day)
        db.session.add(feed)
        db.session.commit()

    w = [1, 1, 2, 2, 3, 3]
    bags = [4, 3, 3, 4, 2, 3]
    time_of_day = ['morning', 'night', 'morning', 'night', 'morning', 'night']

    # for item in [*zip(w, bags, time_of_day)]:
    #     fill_feed('17/08/2022', item[0], item[1], item[2])

    return render_template('dashboard/dashboard.html', **locals())


@blueprints.route('/fine_w_1', methods=['GET', 'POST'])
def fine_w_1():
    result = db.engine.execute(deaths_vs_supply_per_warehouse)
    cards = result.mappings().all()
    print(cards)

    result = db.engine.execute(payments_per_farm)
    finances = result.mappings().all()
    print(finances)

    if request.method == 'POST':
        print(date)
        print(request.json())

    return render_template('warehouses/fine_w_1.html', **locals())
