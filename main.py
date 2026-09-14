from flask import Flask , render_template, request,redirect,url_for, flash
from database import get_products,get_sales,get_stock,insert_products,insert_sales, insert_stock
# import psycopg2


#A flask instance
app=Flask(__name__)

app.secret_key='eldorado789eldorado'

@app.route('/') #decorator function
def home(): #view function
    name="Alex"
    return render_template('index.html',name=name)


# By default it's a GET ROUTE
@app.route('/products')
def products():
    products=get_products()
    return render_template('products.html',products=products)


# Route used to GET and POST data from clients
@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method=="POST":
        product_name=request.form['p_name']
        buying_price=request.form['b_price']
        selling_price=request.form['s_price']

        new_product=(product_name, buying_price, selling_price)
        insert_products(new_product)

        flash("Product Added Successfully!","success")
    return redirect(url_for('products'))    


@app.route('/sales')
def sales():
    sales=get_sales()
    products=get_products()
    return render_template('sales.html',sales=sales,products=products)


@app.route('/add_sales', methods=['GET','POST'])
def add_sales():
    if request.method=="POST":
        product_id=request.form['p_id']
        sales_quantity=request.form['s_quantity']

        new_sale=(product_id, sales_quantity)
        insert_sales(new_sale)

        flash("Sale Added Successfully!","success")
    return redirect(url_for('sales'))
        
        
     
@app.route('/stock')
def stock():
    stock=get_stock()
    products=get_products()
    return render_template('stock.html',stock=stock,products=products)

@app.route('/add_stock',methods=['GET','POST'])
def add_stck():
    if request.method=="POST":
        pid=request.form['pid']
        stock_quantity=request.form['stock_quantity']

        new_stock=(pid,stock_quantity)
        insert_stock(new_stock)

        flash("New Stock Updated Successfully!","success")
    return redirect(url_for('stock'))    

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

# debug=True->automatic update any changes done
app.run(debug=True) 