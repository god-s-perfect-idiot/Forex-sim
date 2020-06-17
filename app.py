from flask import Flask, render_template,request
import model
import service


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/hub")
def hub():
    data,timeline = model.generate_data()
    print(type(data[0]))
    return render_template('hub.html', data=data, timeline=timeline)

if(__name__=="__main__"):
    app.run(debug=True)
