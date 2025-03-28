from flask import Flask, render_template

app = Flask(__name__)

messages_list = ['Flask is cool', 'Jinja is powerful']

@app.route('/messages')
def messages():
    return render_template('exer-09.html', messages_list=messages_list)

if __name__ == '__main__':
    app.run(debug=True)