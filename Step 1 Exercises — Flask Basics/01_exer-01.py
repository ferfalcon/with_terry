from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my site!'

@app.route('/about')
def about():
    return 'This site was built with Flask.'

@app.route('/contact')
def contact():
    return 'Contact me at email@example.com'

if __name__ == '__main__':
    app.run(debug=True)