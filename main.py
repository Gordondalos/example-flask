#import TODO as TODO

from flask import Flask
from flask import render_template
from car import Car

#TODO create a new route, new template, new function in the car class, new class,
from truck import Truck

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Evgeniya & Evgeniy'
    return render_template('index.html', name=name)


@app.route('/about')
def about():
    car = Car('red', '5')
    lens = car.get_count_letters('hello my friend')
    return render_template('about.html', color=car.get_color(), lens=lens)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/additional_info')
def additional_info():
    truck = Truck('white', '200')
    return render_template('additional_info.html', color=truck.get_color(), weight=truck.get_weight())

@app.route('/help')
def help():
    car = Car('blue', 4)
    car.change_door(5)
    car.set_color('grey')
    door = car.get_door()
    return render_template('help.html', color=car.get_color(), door=door)

if __name__ == '__main__':
    app.run()