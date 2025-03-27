from flask import Flask

app = Flask(__name__)

@app.route('/html')
def html():
    return '''
        <h1>Flask is awesome!</h1>
        <p>This is an HTML page.</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)