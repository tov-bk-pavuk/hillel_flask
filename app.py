from flask import Flask
from jinja2 import Template

app = Flask(__name__) # Создаём наше приложение

@app.route('/<arg>')  # Как новая папка
def arg_func(arg):
    return f'arg is - {arg}'

if __name__ == '__main__':
    app.run(debug=True)