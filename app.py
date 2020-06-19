from flask import Flask, render_template, request, jsonify
import model
import service


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/refresh", methods=['POST'])
def refresh():
    data,timeline = model.refresh()
    return jsonify(data)

@app.route("/transact",methods=['POST'])
def transact():
    amount = request.form.get("amount")
    duration = request.form.get("duration")
    current = request.form.get("current")
    ttype = request.form.get("ttype")
    service.transaction(amount, duration, current, ttype)
    return jsonify(1)

@app.route("/resetbalance", methods=['POST'])
def resetbalance():
    service.reset_balance()
    return jsonify(1)

@app.route("/fetchbalance", methods=['POST'])
def fetchbalance():
    return jsonify(service.balance)

@app.route("/hub")
def hub():
    data,timeline = model.generate_data()
    return render_template('hub.html', data=data, timeline=timeline)

if(__name__=="__main__"):
    app.run(debug=True)
