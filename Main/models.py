from Main import db


class Farms(db.Model):
    __tablename__ = 'farms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String(120))
    warehouses = db.relationship('Warehouses', backref='farms', lazy=True)
    supply = db.relationship('Supply', backref='farms', lazy=True)
    deaths = db.relationship('Deaths', backref='farms', lazy=True)
    feeds = db.relationship('Feeding', backref='farms', lazy=True)
    trucks = db.relationship('Truck', backref='farms', lazy=True)
    debit = db.relationship('Debit', backref='farms', lazy=True)
    credit = db.relationship('Credit', backref='farms', lazy=True)

    def __repr__(self):
        return self.name


class Warehouses(db.Model):
    __tablename__ = 'warehouses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'), nullable=False)
    supply = db.relationship('Supply', backref='warehouses', lazy=True)
    deaths = db.relationship('Deaths', backref='warehouses', lazy=True)
    feeds = db.relationship('Feeding', backref='warehouses', lazy=True)
    trucks = db.relationship('Truck', backref='warehouses', lazy=True)

    def __repr__(self):
        return self.name


class Supply(db.Model):
    __tablename__ = 'supply'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'), nullable=False)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouses.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    chicken_added = db.Column(db.Integer)
    bags_added = db.Column(db.Integer)

    def __repr__(self):
        return f"Supply {self.id} @ {self.date}"


class Deaths(db.Model):
    __tablename__ = 'deaths'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'), nullable=False)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouses.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    deaths_num = db.Column(db.Integer)
    time_of_day = db.Column(db.String(120))


class Feeding(db.Model):
    __tablename__ = 'feeding'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'), nullable=False)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouses.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    bags_consumed = db.Column(db.Integer)
    time_of_day = db.Column(db.String(120))


class Truck(db.Model):
    __tablename__ = 'truck'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'), nullable=False)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouses.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    loaded_num = db.Column(db.Integer)
    driver = db.Column(db.String(120))


class Debit(db.Model):
    __tablename__ = 'debit'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Integer)
    category = db.Column(db.String(120))
    note = db.Column(db.Unicode)

    def __repr__(self):
        return f"Debit {self.date} @ {self.amount}"


class Credit(db.Model):
    __tablename__ = 'credit'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Integer)
    category = db.Column(db.String(120))
    note = db.Column(db.Unicode)

    def __repr__(self):
        return f"Credit {self.date} @ {self.amount}"

