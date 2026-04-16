from flask import Flask, request, jsonify
app = Flask(__name__)
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._id = user_id
        self._name = name.strip().title()
        email = email.lower()
        if "@" not in email:
            raise ValueError("Invalid email")
        self._email = email
    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"
    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "email": self._email
        }
    def __del__(self):
        print(f"User {self._name} deleted")
@app.route('/')
def home():
    return "Flask работает "
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    try:
        user = User(
            data["id"],
            data["name"],
            data["email"]
        )
        return jsonify({
            "message": "User created",
            "user": user.to_dict()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
@app.route('/user_str', methods=['GET', 'POST'])
def user_str():
    data = request.json
    try:
        user = User(
            data["id"],
            data["name"],
            data["email"]
        )
        return str(user)
    except Exception as e:
        return str(e), 400
if __name__ == '__main__':
    app.run(debug=True)