from flask import Flask, render_template, request
import requests
import json 
app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/converter/')
def converter():
   currency = request.args.get('currency','USD')
   amount = float(request.args.get('amount',1))
   full_URL = 'https://v6.exchangerate-api.com/v6/5b11cb991f1316781359c849/latest/'+currency
   res = requests.get(full_URL)
   data = json.loads(res.text)
   print(data)
   euro = data["conversion_rates"]["EUR"] * amount
   dollar = data["conversion_rates"]["USD"] * amount
   yen = data["conversion_rates"]["JPY"] * amount
   return {"euro" : euro, "dollar": dollar, "yen": yen}

if __name__ == '__main__':
   app.run('localhost', 80)