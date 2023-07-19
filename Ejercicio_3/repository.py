class UserRepository:
    def __init__(self, database):
        self.database = database

    def add_user(self, user_id, name, age):
        query = "INSERT INTO users (id, name, age) VALUES (?, ?, ?)"
        self.database.execute(query, (user_id, name, age))
        self.database.commit()
        return user_id

    def get_user(self, user_id):
        query = "SELECT id, name, age FROM users WHERE id = ?"
        result = self.database.execute(query, (user_id,))
        user = result.fetchone()
        if user:
            return {
                'id': user[0],
                'name': user[1],
                'age': user[2]
            }
        else:
            return None

