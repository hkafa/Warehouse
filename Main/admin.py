from flask_admin.contrib.sqla import ModelView

time_of_day_choices = {
        'time_of_day': [
            ('morning', 'morning'),
            ('night', 'night')
        ]
    }

category_choices = {
        'category': [
            ('personal', 'personal'),
            ('maintenance', 'maintenance'),
            ('farm', 'farm'),
            ('other', 'other')
        ]
    }


class FarmsModelView(ModelView):
    form_columns = ('name', 'location')
    form_choices = time_of_day_choices


class WarehouseModelView(ModelView):
    form_columns = ('name', 'farms')
    form_choices = time_of_day_choices


class SupplyModelView(ModelView):
    column_filters = ['warehouses.name', 'chicken_added', 'bags_added']
    column_labels = {'warehouses.name': 'Warehouse name'}


class DeathsModelView(ModelView):
    column_filters = ['warehouses.name', 'time_of_day', 'deaths_num']
    column_labels = {'warehouses.name': 'Warehouse name'}
    form_choices = time_of_day_choices


class FeedingModelView(ModelView):
    column_filters = ['warehouses.name', 'time_of_day', 'bags_consumed']
    column_labels = {'warehouses.name': 'Warehouse name'}
    form_choices = time_of_day_choices


class TruckModelView(ModelView):
    column_filters = ['warehouses.name', 'loaded_num']
    column_labels = {'warehouses.name': 'Warehouse name'}


class FinanceModelView(ModelView):
    form_choices = category_choices


# class CreditModelView(ModelView):
#     column_filters = ['warehouses.name', 'loaded_num']
#     column_labels = {'warehouses.name': 'Warehouse name'}
#
