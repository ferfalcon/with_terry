from flask import Flask, render_template

app = Flask(__name__)

@app.route('/greet/<title>/<name>')
def greet(title, name):
    return render_template('exer-02.html', title=title, name=name)

if __name__ == '__main__':
    app.run(debug=True)