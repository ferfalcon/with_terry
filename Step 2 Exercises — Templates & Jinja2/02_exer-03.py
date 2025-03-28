from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return render_template('greet-03.html', user_logged_in=True)

if __name__ == '__main__':
    app.run(debug=True)
