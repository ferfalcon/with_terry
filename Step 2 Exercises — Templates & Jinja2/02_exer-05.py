from flask import Flask, render_template

app = Flask(__name__)

books_list = [
  {'title': '1984', 'author': 'Orwell'},
  {'title': 'Dune', 'author': 'Herbert'},
  {'title': 'Python 101', 'author': 'Someone'}
]

@app.route('/books')
def books():
    return render_template('exer-05.html', books_list=books_list)

if __name__ == '__main__':
    app.run(debug=True)