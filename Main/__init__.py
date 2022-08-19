from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_migrate import Migrate
from Main.admin import *


db = SQLAlchemy()
admin = Admin(template_mode='bootstrap4')
migrate = Migrate(compare_type=True)


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    import Main.routes
    app.register_blueprint(Main.routes.blueprints)

    import API.endpoints
    app.register_blueprint(API.endpoints.api)

    # registering views with admin
    from Main.models import Farms, Warehouses, Supply, Deaths, Feeding, Truck, Debit, Credit
    admin.add_view(FarmsModelView(Farms, db.session))
    admin.add_view(WarehouseModelView(Warehouses, db.session))
    admin.add_view(SupplyModelView(Supply, db.session))
    admin.add_view(DeathsModelView(Deaths, db.session))
    admin.add_view(FeedingModelView(Feeding, db.session))
    admin.add_view(TruckModelView(Truck, db.session))
    admin.add_view(ModelView(Debit, db.session, category="Finance"))
    admin.add_view(FinanceModelView(Credit, db.session, category="Finance"))

    return app