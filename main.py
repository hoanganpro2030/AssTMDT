from flask import Flask, render_template, request, redirect
from utils import Util
app = Flask(__name__)

@app.route("/")
def index():
    username = request.args.get('name')
    return render_template('index.html', name=username)

@app.route("/payment", methods=['POST'])
def payment():
    amount = request.form['amount']
    rs = Util.momo_payment_excute(amount)
    url_payment = rs['payUrl']
    return redirect(url_payment)

if __name__ == "__main__":
    app.run()