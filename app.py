from flask import Flask
from jinja2 import Template

app = Flask(__name__) # Создаём наше приложение

main = '<h5><a href="http://127.0.0.1:5000/">Главная</a></br><h5>'
@app.route('/')  # Добавить Корень нашего сайта.
def hello_world():
    return '<h3><a href="http://127.0.0.1:5000/requirements/">Список установленных пакетов</a></br>' \
           '<a href="http://127.0.0.1:5000/space/">Космонавты</a></br>' \
           '<a href="http://127.0.0.1:5000//generate-users/100">Юзеры</a></br>' \
           '<a href="http://127.0.0.1:5000/mean/">Средний рост и вес</a></br></h3>' \
           '<h5><a href="http://127.0.0.1:5000/">Главная</a></br><h5>' \


@app.route('/requirements/')
def req():
    with open('requirements.txt') as file:
        text = file.read()
    return f'<p>{text}</p><p>{main}</p>'

@app.route('/generate-users/<amount>')
def gen_users(amount):
    from faker import Faker
    fake = Faker()
    names = str()
    amount = int(amount)
    for i in range(amount):
        names += f'<p> {str(i+1)} . {fake.name()} <span style="margin-left:5%;font-style:italic"> {fake.email()} </span></p>'
    return f'<p>{main}</p>{names}<p>{main}</p>'

@app.route('/mean/') #Средний рост, средний вес в (см, кг) hw.csv
def avg():
    import csv
    pounds = 0.453592  # кг
    inches = 2.54  # см
    ind = 1  # индекс столбца
    def avg(ind=1, mesure=2.54):  # по умолчанию для длины
        with open('./static/hw.csv') as file:
            text = csv.reader(file)
            tab_1 = {i[0]: i[ind] for i in text}
            tab_1.pop('Index')
            for i,k in tab_1.items():
                tab_1.update({i: float(k)})
            avg = sum(tab_1.values())/len(tab_1)*mesure
        return avg

    return f'<h2>Средний рост: {avg()} см</h2><h2>Средний вес: {avg(2,pounds)} кг</h2></br><p>{main}</p>'

@app.route('/space/')  # Как новая папка
def space():
    import requests
    r = requests.get('http://api.open-notify.org/astros.json')
    a = r.json() ["number"]
    return f'<h3 style="margin:10% 10%">Космонавтов на орбите: {a} </h3><p>{main}</p>'

@app.route('/<arg>')  # Как новая папка
def arg_func(arg):
    return f'arg is - {arg}'

if __name__ == '__main__':
    app.run(debug=True)