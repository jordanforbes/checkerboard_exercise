from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html',times = 8)

@app.route('/<num>')
def buildboard(num):
    return render_template('index.html',times= int(num),color1='red',color2='black')

if __name__ =="__main__":
    app.run(debug=True)