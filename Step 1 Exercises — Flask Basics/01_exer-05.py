from flask import Flask

app = Flask(__name__)
print(f'My name is: {__name__}')

if __name__ == '__main__':
    print('Starting the Flask app...')
    app.run(debug=True)
