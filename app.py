from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
   return render_template("index.html")

@app.route('/ecoCalculator')
def ecoCalculator():
   return render_template("calculator.html")


if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)