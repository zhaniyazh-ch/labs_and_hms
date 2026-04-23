from flask import Flask, jsonify
from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)
logs = []
class Player:
    def __init__(self, name):
        self.name = name
        logs.append(f"Player {self.name} создан")
    def __del__(self):
        logs.append(f"Player {self.name} удалён")
class Inventory:
    def __init__(self):
        self.items = [
            ("Sword", 50), ("Shield", 30), ("Sword", 50),
            ("Dragon Slayer", 150), ("Stick", 5), ("Staff", 120)
        ]
    def __iter__(self):
        return iter(self.items)

@app.route('/')
def home_player():
    p = Player("John")
    del p
    return jsonify({"events": logs})#17

@app.route('/Inventory')
def inventory_list():
    inv = Inventory()
    strong_items = [name for name, power in inv if power > 100]
    return jsonify({"strong_items": strong_items})#18

@app.route('/analyze_inventory')
def analyze():
    inv = Inventory()
    unique_names = list({item[0] for item in inv.items})
    top_item = max(inv.items, key=lambda x: x[1])
    return jsonify({
        "unique_items": unique_names,
        "top_item": {"name": top_item[0], "power": top_item[1]}
    })#19
if __name__ == '__main__':
    app.run(port=7007, debug=True)