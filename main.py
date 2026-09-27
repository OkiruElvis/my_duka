from flask import Flask , render_template, request,redirect,url_for, flash, session
from database import get_products,get_sales,get_stock,insert_products,insert_sales, insert_stock,available_stock,check_user_exists,insert_user,get_profit_per_product,get_sales_per_day,get_profit_per_day
from flask_bcrypt import Bcrypt
from functools import wraps
# import psycopg2


#A flask instance
# app=object and Flask=class
app=Flask(__name__)

# object=class
bcrypt=Bcrypt(app) #bcrypt instamce

app.secret_key='eldorado789eldorado'

@app.route('/') #decorator function
def home(): #view function
    name="Alex"
    return render_template('index.html',name=name)

def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected


# By default it's a GET ROUTE
@app.route('/products')
@login_required
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
@login_required
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


        check_stock=available_stock(product_id)

        if check_stock < float(sales_quantity):
            flash(f"Insufficient stock to complete sale, only {check_stock} remaining",'danger')
            return redirect(url_for('sales'))

        insert_sales(new_sale)
        flash("Sale made successfully",'success')

    return redirect(url_for('sales'))
        


        
        
     
@app.route('/stock')
@login_required
def stock():
    stock=get_stock()
    products=get_products()
    return render_template('stock.html',stock=stock,products=products)

@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method=="POST":
        pid=request.form['pid']
        stock_quantity=request.form['stock_quantity']

        new_stock=(pid,stock_quantity)
        insert_stock(new_stock)

        flash("New Stock Updated Successfully!","success")
    return redirect(url_for('stock')) 




@app.route('/dashboard')
@login_required
def dashboard():
    sales_per_product=get_profit_per_product()
    profit_per_product=get_profit_per_product()

    sales_per_day=get_sales_per_day()
    profit_per_day=get_profit_per_day()

    product_names=[ i[0] for i in sales_per_product ]
    product_sales=[ float(i[1]) for i in sales_per_product ]
    product_profit=[ float(i[1]) for i in profit_per_product ]

    dates=[ str(i[0]) for i in sales_per_day ]
    daily_sales=[ float(i[1]) for i in sales_per_day ]
    daily_profit=[ float(i[1]) for i in profit_per_day ]
   
    return render_template('dashboard.html',
                           product_names=product_names,product_sales=product_sales,product_profit=product_profit,
                           dates=dates,daily_sales=daily_sales,daily_profit=daily_profit)




@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        email=request.form['email']
        password=request.form['password']

        existing_user=check_user_exists(email)
        if not existing_user:
            flash("User with this email not registered","danger")
            return redirect(url_for('login'))

        check_password=bcrypt.check_password_hash(existing_user[-1],password)

        if check_password:
            session['email']=email
            flash("Login successful",'success')
            return redirect(url_for('dashboard'))
        else:
            flash("incorrect password,try again","danger")
            return redirect(url_for('login'))

    return render_template('login.html')




@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        full_name=request.form['full_name']
        email=request.form['email']
        phone_number=request.form['phone']
        password=request.form['password']

        existing_user=check_user_exists(email)
        if existing_user:
            flash("User with this email already exists, login instead",'danger')
            return redirect(url_for('register'))

        hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')

        new_user=(full_name,email,phone_number,hashed_password)
        insert_user(new_user)
        flash("User created successfully",'success')
        return redirect(url_for('login'))


    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('email',None)
    flash("logged out successfully",'success')
    return redirect(url_for('login'))

# debug=True->automatic update any changes done
app.run(debug=True) 