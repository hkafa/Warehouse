from flask import Blueprint, jsonify
from sqlalchemy import func, DATE, cast, Integer
from datetime import datetime, timedelta
from Main.models import *
import calendar


api = Blueprint('endpoints', '__name__')


@api.route('/weekly_death')
def weekly_death():
    today = datetime.today()
    data = db.session.query(Deaths). \
        with_entities(db.func.sum(Deaths.deaths_num), cast(func.extract("dow", Deaths.date), Integer)). \
        group_by(Deaths.date).\
        filter(Deaths.date.between(today - timedelta(weeks=1), today)). \
        order_by(Deaths.date).all()

    labels = [calendar.day_name[i[1]] for i in data]
    points = [int(i[0]) for i in data]
    chart = {'labels': labels,
             'points': points}

    return jsonify(chart)
