from mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    @classmethod
    def get_all(cls):
        query = "SELECT *, concat_ws(' ', first_name, last_name) as full_name FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        print(results)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
            
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s, NOW() , NOW() );"

        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def update(cls, data ):
        query = "UPDATE users SET first_name = %(first_name)s , last_name = %(last_name)s , email = %(email)s WHERE id = %(id)s;"
    
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"

        connectToMySQL('users_schema').query_db( query, data )
        return id

    @classmethod
    def data(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        results = connectToMySQL('users_schema').query_db( query, data )
        user = cls(results[0])
        return user