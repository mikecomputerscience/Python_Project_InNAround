import bottle

from db_python_class import DatabasePythonClass

db = DatabasePythonClass.db
cities = db.cities
item = cities.find_one()


@bottle.route('/static/:path#.+#', name='static')
def static(path):
    return bottle.static_file(path, root='static')


@bottle.route('/')
def home_page():
    my_things = ['alexis', 'ozil', 'santi']
    return bottle.template('views/index.html', {
        'username': 'Ligang', 'things': my_things
    })


@bottle.post('/destination')
def destination():
    city = bottle.request.forms.get('city')
    if city is None or city == '':
        city = 'No Destination Selected'
    interest = 'place'
    bottle.response.set_cookie('city', city, path='/')
    bottle.response.set_cookie('interest', interest, path='/')
    bottle.redirect('/show_city')


@bottle.route('/show_city')
def show_city():
    city = bottle.request.get_cookie('city')
    interest = bottle.request.get_cookie('interest')

    return bottle.template('views/city.html', {
        'city': city,
        'interest': interest
    })


@bottle.post('/interest')
def post_interest():
    city = bottle.request.json['city']
    interest = bottle.request.json['interest']
    print(city)
    print(interest)
    if interest is None or interest == '':
        interest = 'No Interest Selected'
    return bottle.template('views/city.html', {
        'city': city,
        'interest': interest
    })


@bottle.route('/test')
def test_page():
    return 'This is a test page'


bottle.debug(True)
bottle.run(host='localhost', port=8080)
