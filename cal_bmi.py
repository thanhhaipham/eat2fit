from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cal-bmr/')
def bmr():
    return render_template('cal_bmr.html')

if __name__ == '__main__':
  app.run(debug=True)
 