"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

# connect to db
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='north',
    user='postgres',
    password='22k16k-46l24'
)
try:
    with conn:
        with conn.cursor() as cur:
            # execute query
            with open('north_data/employees_data.csv', 'r', encoding='UTF-8') as emp_file:
                reader = csv.DictReader(emp_file)
                for row in reader:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                (row['employee_id'], row['first_name'], row['last_name'],
                                 row['title'], row['birth_date'], row['notes']))
            with open('north_data/customers_data.csv', 'r', encoding='UTF-8') as cust_file:
                reader = csv.DictReader(cust_file)
                for row in reader:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                (row["customer_id"], row["company_name"], row["contact_name"]))
            with open('north_data/orders_data.csv', 'r', encoding='UTF-8') as orders_file:
                reader = csv.DictReader(orders_file)
                for row in reader:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                (row["order_id"], row["customer_id"], row["employee_id"],
                                 row["order_date"], row["ship_city"]))
            cur.execute("SELECT * FROM employees")
            cur.execute("SELECT * FROM customers")
            cur.execute("SELECT * FROM orders")
            rows = cur.fetchall()
            print(rows)
finally:
    conn.close()
