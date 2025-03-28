from flask import Flask, render_template

app = Flask(__name__)

filter_list = ['lowercase', 15.8890015, 'UPPERCASE', 'some title words', '<h1>safe</h1>', 'String of chars']

@app.route('/filters')
def filters():
    return render_template('exer-06.html', filter_list=filter_list)

if __name__ == '__main__':
    app.run(debug=True)