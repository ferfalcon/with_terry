from flask import Flask

app = Flask(__name__)

@app.route('/square/<int:number>')
def square(number):
    return f'The square of {number} is {number*number}'

if __name__ == '__main__':
    app.run(debug=True)