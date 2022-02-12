from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

# This will align my data to the database


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

# This class method will query for all my dojos and puts them on a list
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        # make sure you have the correct schema listed in the ()
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []  # empty list to store the results
        for row in results:  # makes d represent each row that comes back from the database
            dojos.append(cls(row))  # will append each row to the list
        return dojos  # returns the list

    @classmethod
    def create(cls, data):
        # adds the new dojo
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        this_user = cls(results[0])
        for row in results:
            x = {
                'id': row['ninjas.id'],
                'f_name': row['f_name'],
                'l_name': row['l_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
            }
            this_user.ninjas.append(Ninja(x))
        return this_user
