from peewee import *
from datetime import date

db = SqliteDatabase("orders.db")

class Transport(Model):
    id_transport = PrimaryKeyField()
    mark = TextField()
    registration_date = DateField()
    color = TextField()

    class Meta:
        database = db

class Recevier(Model):
    id_recevier = PrimaryKeyField()
    last_name = TextField()
    first_name = TextField()
    patronymic_name = TextField()
    date_of_birth = DateField()
    index = TextField()
    city = TextField()
    street = TextField()
    house = TextField()
    apartment = TextField()
    phone_number = TextField()

    class Meta:
        database = db

class Order(Model):
    id_order = PrimaryKeyField()
    id_sender = IntegerField()
    id_recevier = IntegerField()
    order_date = DateField()
    delivery_date = DateField()
    delivery_price = FloatField()
    id_courier = IntegerField()
    id_transport = IntegerField()

    class Meta:
        database = db

if __name__ == "__main__":
    db.create_tables([Transport, Recevier, Order])
    sample_transport1 = Transport(mark="BMW", registration_date=date(2023, 5, 13), color="Black")
    sample_transport1.save()
    sample_transport2 = Transport(mark="KIA", registration_date=date(2016, 3, 6), color="Gray")
    sample_transport2.save()
    sample_recevier1 = Recevier(last_name="Olezhnik", first_name="Maxim", patronymic_name="Zaharovich", date_of_birth=date(1977, 12, 15),
                                index="332373", city="Kaliningrad", street="Georginovaya", house="24", apartment="1", phone_number="89629563421")
    sample_recevier1.save()
    sample_recevier2 = Recevier(last_name="Borzovich", first_name="Gennadiy", patronymic_name="Konstantinovich", date_of_birth=date(1981, 7, 30),
                                index="156789", city="Kaliningrad", street="Litovskiy val", house="38", apartment="11", phone_number="89315054291")
    sample_recevier2.save()
    order1 = Order(id_sender=1, id_recevier=1, order_date=date(2024, 11, 22), delivery_date=date(2024, 11, 23),
                    delivery_price=100.50, id_courier=1, id_transport=2)
    order1.save()
    order1 = Order(id_sender=1, id_recevier=2, order_date=date(2024, 12, 11), delivery_date=date(2024, 12, 12),
                    delivery_price=131.23, id_courier=1, id_transport=1)
    order1.save()