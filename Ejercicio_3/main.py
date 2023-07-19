from flask import Flask, request, jsonify
from db_connector import create_database, close_database
from repository import UserRepository

app = Flask(__name__)
database = create_database()
user_repository = UserRepository(database)

@app.route('/create/user/<int:user_id>/<string:name>/<int:age>', methods=['POST'])
def create_user(user_id, name, age):
    user_id = user_repository.add_user(user_id, name, age)
    return jsonify({'message': 'User created', 'id': user_id})

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_repository.get_user(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
    close_database(database)

