import sqlite3

cur=0
con=0

def connection():
    global con
    global cur
    con = sqlite3.connect('dogo.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS add_doggy(name Text, gender Text,breed1 Text, about Text ,price Text,meet Text,image BOLB)')
    cur.execute('CREATE TABLE IF NOT EXISTS add_customer(dog_name Text, dog_breed Text,dog_price Text, cust_name Text ,cust_gender Text,cust_mob Text,cust_address Text)')
    # cur.execute('DROP TABLE add_dog')

def close_db():
    cur.close()
    con.close()

def convert_to_binary(filename):
    with open(filename,'rb') as file:
        binary=file.read()
    return binary

def insert_db(name1,gender1,breed1,about1,price1,meet1,image):
    connection()
    image_binary=convert_to_binary(image)
    cur.execute('INSERT INTO add_doggy VALUES(?,?,?,?,?,?,?)',(name1,gender1,breed1,about1,price1,meet1,image_binary))
    con.commit()
    close_db()

def select_from_db():
    global record
    connection()
    records=cur.execute('SELECT rowid,name,gender,breed1,about,price,meet,image FROM add_doggy')
    record=records.fetchall()
    close_db()
    return record

#customer_detailing:-
def insert_customer(dog_name,dog_breed,dog_price,cust_name,cust_gender,cust_mob,cust_address):
    connection()
    cur.execute('INSERT INTO add_customer VALUES(?,?,?,?,?,?,?)',(dog_name,dog_breed,dog_price,cust_name,cust_gender,cust_mob,cust_address))
    con.commit()
    close_db()

# insert_customer('as','ass','ass','asss','as','assxlckld','assszgdj')
def remove_dog(id):
    connection()
    cur.execute('DELETE FROM add_doggy WHERE (rowid=?)',(id,))
    con.commit()
    close_db()
    print('success')

def customer_details():
    connection()
    records=cur.execute('SELECT * FROM add_customer')
    record=records.fetchall()
    close_db()
    return record
# print(customer_details())
    
# connection()
# close_db()
# print(select_from_db())