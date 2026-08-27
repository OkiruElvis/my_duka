from flask import Flask


#A flask instance
app=Flask(__name__)

@app.route('/')
def home():
    return "Hello World!!"

@app.route('/products')
def products():
    return "My Products"

@app.route('/sales')
def sales():
    return "Sales"

@app.route('/stock')
def stock():
    return "My Stock"

@app.route('/dashboard')
def dashboard():
    return "Dashboard"


app.run()