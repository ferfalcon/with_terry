from flask import Flask, render_template

app = Flask(__name__)

@app.route('/includes')
def with_includes():
    return render_template('exer-08-blocks.html')

if __name__ == '__main__':
    app.run(debug=True)