from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 初始化購物車
def init_cart():
    if 'cart' not in session:
        session['cart'] = []

@app.route('/')
def index():
    init_cart()
    return render_template('index.html', cart=session['cart'])

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    init_cart()
    # 獲取商品資訊，這裡僅簡單示範
    product = {
        'id': product_id,
        'name': 'Product Name',
        'price': 10.0
    }
    session['cart'].append(product)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
