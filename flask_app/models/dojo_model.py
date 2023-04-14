from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE

from flask_app.models.ninja_model import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL(DATABASE).query_db(query)

        dojos = []

        if results:
            for dojo in results:
                new_dojo = cls(dojo)
                dojos.append(new_dojo)

        return dojos
    
    @classmethod
    def get_one(cls,id):

        data = {
            "id": id
        }

        query = """
                SELECT * FROM dojos
                WHERE id = %(id)s
        """

        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        dojo = cls(result[0])

        return dojo
    
    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos(name) VALUE(%(new_dojo)s);"
        return connectToMySQL(DATABASE).query_db(query, data);

    @classmethod
    def get_ninjas(cls,id):

        data = {
            "id": id
        }

        query = """

                Select * FROM dojos
                JOIN ninjas ON
                dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(id)s;
        """

        results = connectToMySQL(DATABASE).query_db(query,data)

        

        

        if results:
            ninjas_of_dojo = []

            for row in results:               
                ninja_data = {
                    'id': row['ninjas.id'],
                    'dojo_id': row['dojo_id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'created_at': row['ninjas.created_at'],
                    'updated_at':row['ninjas.updated_at']  
                }

                new_ninja = Ninja(ninja_data)
                ninjas_of_dojo.append(new_ninja)

        print(ninjas_of_dojo)

        return ninjas_of_dojo