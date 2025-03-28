from flask import Flask, render_template

app = Flask(__name__)
fruits_list = ['Apple', 'Banana', 'Cherry', 'Coke']

@app.route('/fruits')
def fruits():
    return render_template('fruits.html', fruits_list=fruits_list)

if __name__ == '__main__':
    app.run(debug=True)