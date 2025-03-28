from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('exer-10.html'), 404

if __name__ == '__main__':
    app.run(debug=True)