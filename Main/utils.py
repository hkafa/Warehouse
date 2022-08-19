from Main import db
from Main.models import *


def deaths_number(warehouse_id, time_of_day):
    data = db.session.query(Deaths).filter((Deaths.warehouse_id == warehouse_id) & (Deaths.time_of_day == time_of_day)).first()
    return data.deaths_num


def total_deaths_per_cycle(warehouse_id, cycle_id):
    data = db.session.query(Deaths).filter((Deaths.warehouse_id == warehouse_id) & (Deaths.cycle_id == cycle_id)).all()
    return sum([item.deaths_num for item in data])


def number_in_cycle(cycle_id):
    data = db.session.query(Cycles).filter(Cycles.id == cycle_id).first().number
    return data
