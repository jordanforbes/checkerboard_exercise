from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html',times = 8, halfTimes=4)

@app.route('/<num>')
def buildboard(num):
    return render_template('index.html',times= int(num), halfTimes=4)

@app.route('/<x>/<y>')
def bothSides(x,y):
    return render_template('index.html',times =int(x), halfTimes=int(int(y)/2))

if __name__ =="__main__":
    app.run(debug=True)