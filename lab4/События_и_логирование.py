from flask import Flask
from datetime import datetime
app = Flask(__name__)
class Player:
    def __init__(self, _id, name, hp):
        self._id = _id
        self.name = name
        self._hp = hp
        self.inventory = Inventory()
class Item:
    def __init__(self, _id, name, power):
        self._id = _id
        self.name = name
        self.power = power
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def get_items(self):
        return self.items
#6
class Event:
    def __init__(self, event_type: str, data: dict):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Event(type='{self.type}', data={self.data}, timestamp='{self.timestamp}')"
@app.route('/event')
def event_test():
    e = Event("ATTACK", {"damage": 20})
    return str(e)
#7
class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = int(event.data.get("damage", 0) * 0.9)
            self._hp -= damage
        else:
            pass
class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power = int(item.power * 1.1)
                self.inventory.add_item(item)
@app.route('/event-test')
def event_test_route():
    w = Warrior(1, "Aiganym", 100)
    m = Mage(2, "Akzhan", 100)
    attack = Event("ATTACK", {"damage": 50})
    loot = Event("LOOT", {"item": Item(1, "Sword", 50)})
    w.handle_event(attack)
    m.handle_event(loot)
    return f"Warrior HP: {w._hp}<br>Mage Item Power: {m.inventory.get_items()[0].power}"
#8-9
class Logger:
    def log(self, event, player, filename: str):
        line = f"{event.timestamp};{player._id};{event.type};{event.data}\n"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)
    def read_logs(self, filename: str):
        events = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                if len(parts) != 4:
                    continue
                event_type = parts[2]
                data = eval(parts[3])
                e = Event(event_type, data)
                events.append(e)
        return events
@app.route('/log-test')
def log_test():
    p = Player(1, "Aiganym", 100)
    e = Event("ATTACK", {"damage": 50})
    logger = Logger()
    logger.log(e, p, "log.txt")
    return "Событие записано"
@app.route('/read-logs')
def read_logs():
    logger = Logger()
    events = logger.read_logs("log.txt")
    return "<br>".join(str(e) for e in events)
#10
class EventIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.events):
            raise StopIteration
        event = self.events[self.index]
        self.index += 1
        return event
events = [
    Event("ATTACK", {"damage": 10}),
    Event("HEAL", {"heal": 5}),
    Event("LOOT", {"item": Item(1, "Sword", 50)})
]
iterator = EventIterator(events)
for e in iterator:
    print(e)
#11
def damage_stream(events):
    for event in events:
        if event.type == "ATTACK":
            yield event.data.get("damage", 0)
#12
def generate_events(players, items, n):
    return [Event("ATTACK", {"damage": 10}) for _ in range(n)]
@app.route('/generate')
def generate():
    events = generate_events([], [], 3)
    return "<br>".join(str(e) for e in events)
#13
def analyze_logs(events):
    total = sum(e.data.get("damage", 0) for e in events if e.type == "ATTACK")
    players = {}
    types = {}
    for e in events:
        types[e.type] = types.get(e.type, 0) + 1
        if e.type == "ATTACK":
            pid = e.data.get("player_id", 0)
            players[pid] = players.get(pid, 0) + e.data.get("damage", 0)
    top_player = max(players, key=players.get) if players else None
    most_common = max(types, key=types.get)
    return {
        "total_damage": total,
        "top_player": top_player,
        "most_common_event": most_common
    }
@app.route('/analyze')
def analyze():
    events = [
        Event("ATTACK", {"damage": 10, "player_id": 1}),
        Event("ATTACK", {"damage": 5, "player_id": 2}),
        Event("HEAL", {"heal": 5})
    ]
    return str(analyze_logs(events))
#14
decide_action = lambda player: (
    "HEAL" if player._hp < 50 else
    ("LOOT" if len(player.inventory.get_items()) == 0 else "ATTACK")
)
@app.route('/decide')
def decide():
    p = Player(1, "Aiganym", 40)
    return decide_action(p)
#15
w = Warrior(1, "Warrior", 100)
m = Mage(2, "Mage", 100)
w.handle_event(Event("ATTACK", {"damage": 50}))
m.handle_event(Event("LOOT", {"item": Item(1, "Sword", 50)}))
print(w._hp)
print(m.inventory.get_items()[0])
if __name__ == '__main__':
    app.run(port=5001)
from flask import Flask
from datetime import datetime
app = Flask(__name__)
class Item:
    def __init__(self, _id, name, power):
        self._id = _id
        self.name = name
        self.power = power
    def __str__(self):
        return f"{self.name}(power={self.power})"
class Inventory:
    def __init__(self):
        self._items = []
#18
    def __iter__(self):
        return iter(self._items)
    def add_item(self, item):
        self._items.append(item)
    def get_items(self):
        return self._items
    def strong_items(self, min_power=30):
        # comprehension
        return [i for i in self._items if i.power >= min_power]
class Player:
    def __init__(self, _id, name, hp):
        self._id = _id
        self.name = name
        self._hp = hp
        self._inventory = Inventory()

#16
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)
    @property
    def inventory(self):
        return self._inventory

#17
    def __del__(self):
        print(f"Player {self.name} удалён")
class Event:
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Event({self.type}, {self.data}, {self.timestamp})"
class Logger:
    def log(self, event, player, filename):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{event.timestamp};{player._id};{event.type};{event.data}\n")
    def read_logs(self, filename):
        events = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                t, pid, etype, data = line.strip().split(";")
                events.append(Event(etype, eval(data)))
        return events
#19
def analyze_inventory(inventories):
    all_items = []
    for inv in inventories:
        all_items.extend(inv.get_items())
    unique_items = {i.name for i in all_items}
    top_power = max(all_items, key=lambda x: x.power) if all_items else None
    return {
        "unique_items": unique_items,
        "top_power": str(top_power)
    }
@app.route('/')
def home():
    return "Server OK (Tasks 16-20 running)"
#20
@app.route('/simulate')
def simulate():
    p1 = Player(1, "Aiganym", 100)
    p2 = Player(2, "Akzhan", 100)
    sword = Item(1, "Sword", 50)
    shield = Item(2, "Shield", 20)
    p1.inventory.add_item(sword)
    p2.inventory.add_item(shield)
    e1 = Event("ATTACK", {"damage": 30, "player_id": 1})
    e2 = Event("ATTACK", {"damage": 60, "player_id": 2})
    p1.hp -= e1.data["damage"]
    p2.hp -= e2.data["damage"]
    logger = Logger()
    logger.log(e1, p1, "log.txt")
    logger.log(e2, p2, "log.txt")
    logs = logger.read_logs("log.txt")
    analysis = analyze_inventory([p1.inventory, p2.inventory])
    return f"""
    <h3>Simulation Done</h3>
    <p>Player1 HP: {p1.hp}</p>
    <p>Player2 HP: {p2.hp}</p>
    <p>Logs count: {len(logs)}</p>
    <p>Unique items: {analysis['unique_items']}</p>
    <p>Top item: {analysis['top_power']}</p>
    """
if __name__ == '__main__':
    app.run(port=5001)