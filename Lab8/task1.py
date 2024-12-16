import sqlite3 as sq

def createTableCourier(cur):
    cur.execute("""
                CREATE TABLE courier (
                    id_courier INTEGER PRIMARY KEY AUTOINCREMENT,
                    last_name VARCHAR(256),
                    first_name VARCHAR(256),
                    patronymic_name VARCHAR(256),
                    passport_number VARCHAR(32),
                    date_of_birth DATE,
                    hiring_date DATE,
                    start_of_working_day TIME,
                    end_of_working_day TIME,
                    city VARCHAR(64),
                    street VARCHAR(64),
                    house VARCHAR(8),
                    apartment VARCHAR(8),
                    phone_number VARCHAR(16));
                """)


def createTableSender(cur):
    cur.execute("""
                CREATE TABLE sender (
                    id_sender INTEGER PRIMARY KEY AUTOINCREMENT,
                    last_name VARCHAR(256),
                    first_name VARCHAR(256),
                    patronymic_name VARCHAR(256),
                    date_of_birth DATE,
                    `index` VARCHAR(10),
                    city VARCHAR(64),
                    street VARCHAR(64),
                    house VARCHAR(8),
                    apartment VARCHAR(8),
                    phone_number VARCHAR(16));
                """)


def insertSampleCourier(cur):
    courier = (
    "Petrov", "Petr", "Alekseevich", "7432 671675", "20.01.1999", "19.10.2023", "8:00:00", "20:00:00", "Kaliningrad",
    "Telmana", "1 a", "3", "+79062386561")
    cur.execute("""
                INSERT INTO courier (last_name, first_name, patronymic_name, passport_number, date_of_birth,
                hiring_date, start_of_working_day, end_of_working_day, city, street, house, apartment, phone_number)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
                """, courier)


def insertSampleSender(cur):
    sender = ("Nazarov", "Viktor", "Aleksandrovich", "12.02.1990", "350003", "Kaliningrad",
              "Gerzena", "1 b", "7", "+79622593544")
    cur.execute("""
                INSERT INTO sender (last_name, first_name, patronymic_name, date_of_birth, `index`,
                city, street, house, apartment, phone_number)
                VALUES(?,?,?,?,?,?,?,?,?,?)
                """, sender)


def updateSampleSender(cur):
    sender = ("Nazarov", "Viktor", "Aleksandrovich", "12.02.1990")
    cur.execute("""
                UPDATE sender SET phone_number="+79899113542"
                WHERE last_name=? AND first_name=? AND patronymic_name=? AND date_of_birth=?;
                """, sender)


if __name__ == "__main__":
    conn = sq.connect('orders.db')
    cur = conn.cursor()
    createTableCourier(cur)
    createTableSender(cur)
    insertSampleCourier(cur)
    insertSampleSender(cur)
    updateSampleSender(cur)
    conn.commit()