from flask import Flask , render_template


#A flask instance
app=Flask(__name__)

@app.route('/')
def home():
    name="Alex"
    return render_template('index.html',name=name)

@app.route('/products')
def products():
    products=['milk','eggs','shoes']
    return render_template('products.html',products=products)

@app.route('/sales')
def sales():
      num=12
      return render_template('sales.html',num=num)

@app.route('/stock')
def stock():
    return render_template('stock.html')

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