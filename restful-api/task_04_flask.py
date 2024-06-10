from flask import Flask, jsonify, request

# Instantiate a Flask web server
app = Flask(__name__)

# Users stored in memory
users = {}


# Define a route for the root URL
@app.route('/')
def home():
    return "Welcome to the Flask API!"


# Route for serving JSON data
@app.route('/data')
def data():
    return jsonify(list(users.keys()))


# Route to check API status
@app.route('/status')
def status():
    return "OK"


# Dynamic route to get user details
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


# Route to handle POST requests for adding a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.json
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = new_user
    return jsonify({"message": "User added",
                    "user": new_user}), 201


# Run the Flask development server
if __name__ == "__main__":
    app.run()
