import psycopg2
#1-masala:
#from decimal import Decimal, getcontext
#class ToDecimal:
#    def __init__(self, number):
#        self.decimal = Decimal(number)
#
#number = 452.125478  # Float değer
#to_decimal = ToDecimal(number)
#
#print("Decimal value:", to_decimal.decimal)

#2-masala:
#import psycopg2
#from decimal import Decimal, getcontext
#
#connection = psycopg2.connect(
#    database="imtixon1",
#    user="postgres",
#    password="Begzod0708",
#    host="localhost",
#    port="5432"
#)
#
#cursor = connection.cursor()
#
#cursor.execute("""
#CREATE TABLE IF NOT EXISTS Product (
#    id SERIAL PRIMARY KEY,
#    name VARCHAR(100),
#    color VARCHAR(50),
#    price DECIMAL(10, 2)
#)
#""")
#
#connection.commit()
#
#price = Decimal(452.125478).quantize(Decimal('0.01'))
#
#cursor.execute("""
#INSERT INTO Product (name, color, price)
#VALUES (%s, %s, %s)
#""", ('Samsung A72', 'black', price))
#
#connection.commit()
#
#cursor.close()
#connection.close()
#
#print("Product tablosu oluşturuldu ve veri eklendi.")

#3-masala:
#1 git init
#2 git status
#3 git add .
#4 git commit


#4-masala:
#class Car:
#    def __init__(self, model, color, year, price):
#        # Özellikleri tanımlar
#        self.model = model
#        self.color = color
#        self.year = year
#        self.price = price
#
#    def change_price(self, new_price):
#        self.price = new_price
#
#    def display_info(self):
#        return f"Model: {self.model}, Color: {self.color}, Year: {self.year}, Price: {self.price}"
#
#
#my_car = Car("Toyota", "Red", 2020, 25000)
#
#print(my_car.display_info())
#
#my_car.change_price(27000)
#
#print("Updated info:", my_car.display_info())

#6-masala:
#class Alphabet:
#    def __init__(self):
#        self.letters = [chr(i) for i in range(65, 91)]
#        self.index = 0
#
#    def __iter__(self):
#        return self
#
#    def __next__(self):
#        if self.index >= len(self.letters):
#            raise StopIteration
#
#        letter = self.letters[self.index]
#        self.index += 1
#        return letter
#
#alphabet = Alphabet()
#
#for letter in alphabet:
#    print(letter, end=' ')

#7-masala:
#keys = ["name", "description", "title", "keywords", "content", "charset"]
#values = ["document", "The best document", "My document", "doc, word, excel", "None"]
#
#my_dict = {key: values[i] if i < len(values) else None for i, key in enumerate(keys)}
#
#print("Generated Dictionary:", my_dict)


#8-masala:
#import psycopg2
#import threading
#

#def fetch_all_products():
#    connection = psycopg2.connect(
#        database="imtixon1",
#        user="postgres",
#        password="Begzod0708",
#        host="localhost",
#        port="5432"
#    )
#
#    cursor = connection.cursor()
#
#    cursor.execute("SELECT * FROM Product")
#    products = cursor.fetchall()
#
#    for product in products:
#        print("Product:", product)
#
#    cursor.close()
#    connection.close()
#
#
#threads = []
#for i in range(4):
#    t = threading.Thread(target=fetch_all_products)
#    threads.append(t)
#
#for t in threads:
#    t.start()



#def connect():
#    user = "postgres"
#    dbname = "imtixon1"
#    password = "Begzod0708"
#    host = "localhost"
#    port = "5432"
#    def select():
#        connection = psycopg2.connect(
#            user='postgres',
#            database='imtixon1',
#            password='Begzod0708',
#            host='localhost',
#            port="5432"
#        )
#
#        cursor = connection.cursor()
#
#        cursor.execute("SELECT * FROM  product")
#        products = cursor.fetchall()
#
#        cursor.close()
#        connection.close()
#
#        return products
#    connect.select = select
#
#
#connect()
#
#products = connect.select()
#
#for product in products:
#    print("Product:", product)

