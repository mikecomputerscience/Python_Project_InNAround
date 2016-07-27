from pymongo import MongoClient
import configparser


class DatabasePythonClass(object):
    # Get credentials
    config = configparser.RawConfigParser()
    config.read('credential.properties')
    db_username = config.get('DatabaseSection', 'database.username')
    db_password = config.get('DatabaseSection', 'database.password')

    # Connect to database
    uri = 'mongodb://' + db_username + ':' + db_password + '@ds031995.mlab.com:31995/python_class'
    client = MongoClient(uri)
    db = client.python_class

    # Connect to collection
    # cities = db.cities

    # Get info
    # item = cities.find_one()
    # print(item)
