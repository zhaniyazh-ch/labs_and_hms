from flask import Flask, jsonify, request
from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)
class Player:
    def __init__(self, _id, name, hp):
        self._id = _id
        self._name = name.strip().title()
        self._hp = hp if hp >= 0 else 0
    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"
    @classmethod
    def from_string(cls, data: str):
        parts = data.split(",")
        if len(parts) != 3:
            raise ValueError("Неверный формат строки")
        try:
            _id = int(parts[0].strip())
            name = parts[1].strip()
            hp = int(parts[2].strip())
        except:
            raise ValueError("Неверные данные")
        return cls(_id, name, hp)
@app.route('/')
def home():
    p = Player(1, " john ", 120)
    return str(p)#1

@app.route('/player')
def player_from_string():
    data = request.args.get("data", "2, alice , 90")
    try:
        p = Player.from_string(data)
        return jsonify({
            "id": p._id,
            "name": p._name,
            "hp": p._hp
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400#2

class Item:
    def __init__(self, _id, name, power):
        self._id = _id
        self._name = name.strip().title()
        self._power = power
    def __str__(self):
        return f"Item(id={self._id}, name='{self._name}', power={self._power})"
    def __eq__(self, other):
        return isinstance(other, Item) and \
               (self._id, self._name, self._power) == (other._id, other._name, other._power)
    def __hash__(self):
        return hash((self._id, self._name, self._power))
@app.route('/items')
def items_demo():
    i1 = Item(1, " Sword ", 50)
    i2 = Item(1, "sword", 50)
    i3 = Item(2, "Bow", 30)
    items = {i1, i2, i3}
    return jsonify({
        "items": [str(i) for i in items],
        "count": len(items)
    })
if __name__ == '__main__':
    app.run(port=4000)#3

from flask import Flask, jsonify
from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)
class Item:
    def __init__(self, _id, name, power):
        self._id = _id
        self._name = name.strip().title()
        self._power = power
    def __str__(self):
        return f"Item(id={self._id}, name='{self._name}', power={self._power})"
    def __eq__(self, other):
        return isinstance(other, Item) and \
               (self._id, self._name, self._power) == (other._id, other._name, other._power)
    def __hash__(self):
        return hash((self._id, self._name, self._power))
class Inventory:
    def __init__(self):
        self._items = []
    def add_item(self, item: Item):
        if not any(i._id == item._id for i in self._items):
            self._items.append(item)
    def remove_item(self, item_id: int):
        self._items = [i for i in self._items if i._id != item_id]
    def get_items(self):
        return self._items
    def unique_items(self):
        return set(self._items)
    def to_dict(self):
        return {item._id: item for item in self._items}
    def get_strong_items(self, min_power: int):
        return [i for i in self._items if i._power >= min_power]
inv = Inventory()
@app.route('/inventory')
def inventory_task():
    inv._items = []
    inv.add_item(Item(1, " sword ", 50))
    inv.add_item(Item(2, " bow ", 30))
    inv.add_item(Item(1, " sword ", 50))  # дубликат
    inv.add_item(Item(3, " axe ", 80))
    inv.remove_item(2)
    return jsonify({
        "all_items": [str(i) for i in inv.get_items()],
        "unique_items": [str(i) for i in inv.unique_items()],
        "dict_items": {str(k): str(v) for k, v in inv.to_dict().items()}
    })#4
@app.route('/inventory/strong')
def strong_items_task():
    inv._items = [
        Item(1, " sword ", 50),
        Item(2, " bow ", 30),
        Item(3, " axe ", 80)
    ]
    result = inv.get_strong_items(50)
    return jsonify({
        "strong_items": [str(i) for i in result]
    })
if __name__ == '__main__':
    app.run(port=4000, debug=True)#5