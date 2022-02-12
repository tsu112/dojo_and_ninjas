from flask_app.config.mysqlconnection import connectToMySQL  # connects my database


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        # adds the new ninja
        query = "INSERT INTO ninjas (f_name, l_name, age, dojos_id) VALUES (%(f_name)s, %(l_name)s, %(age)s, %(dojos_id)s);"
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        return results
