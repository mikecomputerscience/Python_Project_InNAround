from db_python_class import DatabasePythonClass

db = DatabasePythonClass.db
cities = db.cities
item = cities.find_one()

if item:
    print('Database connection passed')
else:
    print('Database connection failed')
