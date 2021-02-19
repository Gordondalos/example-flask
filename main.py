from flask import Flask
from flask import render_template
from car import Car


app = Flask(__name__)

@app.route('/')
def index():
    name = 'Evgeniya'
    return render_template('index.html', name=name)


@app.route('/about')
def about():
    car = Car('red')
    lens = car.get_count_letters('hello my friend')
    return render_template('about.html', color=car.get_color(), lens=lens)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/additional_info')
def additional_info():
    return render_template('additional_info.html')


if __name__ == '__main__':
    app.run()