import psycopg2

#establishin a new db conection
conn=psycopg2.connect(host='localhost',port=5432,user='postgres',password='Qwerty@789',dbname='myduka')

#creating a cursor object to perform db operations
cur=conn.cursor()


# def get_products():
#     cur.execute('select * from products')
#     products=cur.fetchall()
#     return products



# #Inserting one data at a time
# # def insert_products():
# #     cur.execute("insert into products(name,buying_price,selling_price)values('iphone',50000,60000)")
# #     conn.commit()

# # insert_products()


# #creating a reusable 
# def insert_products(product_values):
#     cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",product_values)
#     conn.commit()

# product1=('predator',2500,5500)
# product2=('hp probook',35000,40000)

# insert_products(product1)
# insert_products(product2)

# products=get_products()
# print(products)

# def get_sales():
#     cur.execute('select * from sales')
#     sales=cur.fetchall()
#     return sales



# def insert_sales(total_sales):
#     cur.execute("insert into sales(pid,quantity)values(%s,%s)",total_sales)
#     conn.commit()

# sale1=(7,100)

# insert_sales(sale1)

# total_sales=insert_sales()
# print(total_sales)


def get_stock():
    cur.execute("select * from stock")
    stock=cur.fetchall()
    return stock

def insert_stock(stock_values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",stock_values)
    conn.commit()

# stock1=(1,100)
# stock2=(2,50)

# insert_stock(stock1)
# insert_stock(stock2)

# stock_data=get_stock()
# print(stock_data)

def get_sales_per_product():
    cur.execute("""
            select products.name , sum(sales.quantity * products.selling_price ) as total_sales 
            from sales join products on  sales.pid = products.id group by products.name;
    """)
    sales_per_product=cur.fetchall()
    return sales_per_product

# sales_per_product=get_sales_per_product()
# print(sales_per_product)

def get_profit_per_day():
    cur.execute("""
            select date(sales.created_at) as day, sum((products.selling_price - products.buying_price) * sales.quantity) as 
            total_profit from sales join products on sales.pid = products.id group by day;

    """)
    profit_per_day=cur.fetchall()
    return profit_per_day

# profit_per_day=get_profit_per_day()
# print (profit_per_day)



#sales per day 
def get_sales_per_day():
    cur.execute("""
            select date(sales.created_at) as day, sum(products.selling_price*sales.quantity) as 
            total_sales from sales inner join products on sales.pid=products.id group by day;
    """)
    sales_per_day=cur.fetchall()
    return sales_per_day

# sales_per_day=get_sales_per_day()
# print(sales_per_day)


# profit per product
def get_profit_per_product():
    cur.execute("""
            select products.name, sum((products.selling_price-products.buying_price)*sales.quantity) as 
            product_profits from products inner join sales on products.id=sales.pid group by products.name;

    """)
    profit_per_product=cur.fetchall()
    return profit_per_product

profit_per_product=get_profit_per_product()
print(profit_per_product)





