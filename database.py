import psycopg2

#establishin a new db conection
conn=psycopg2.connect(host='localhost',port=5432,user='postgres',password='Qwerty@789',dbname='myduka')

#creating a cursor object to perform db operations
cur=conn.cursor()


def get_products():
    cur.execute('select * from products')
    products=cur.fetchall()
    return products
#Inserting one data at a time
# def insert_products():
#     cur.execute("insert into products(name,buying_price,selling_price)values('iphone',50000,60000)")
#     conn.commit()

# insert_products()


#creating a reusable 
def insert_products(product_values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",product_values)
    conn.commit()

product1=('predator',2500,5500)
product2=('hp probook',35000,40000)

insert_products(product1)
insert_products(product2)

products=get_products()
print(products)
