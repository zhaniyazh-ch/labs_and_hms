from datetime import datetime
class Event:
    def __init__(self, type: str, data: dict):
        self.type = type
        self.data = data
        self.timestamp = datetime.now()
    def __repr__(self):
        return f"Event(type='{self.type}', data={self.data}, timestamp='{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}')"
e = Event("ATTACK", {"damage": 20})
print(e)#6
class Event:
    def __init__(self, type: str, data: dict):
        self.type = type
        self.data = data
class Item:
    def __init__(self, id: int, name: str, power: int):
        self.id = id
        self.name = name
        self.power = power
    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"
class Inventory:
    def __init__(self):
        self._items = []
    def add_item(self, item: Item):
        for i in self._items:
            if i.id == item.id:
                return
        self._items.append(item)
    def __repr__(self):
        return f"Inventory({self._items})"
class Player:
    def __init__(self, name: str, hp: int = 100):
        self.name = name
        self.hp = hp
        self.inventory = Inventory()
    def handle_event(self, event: Event):
        if event.type == "ATTACK":
            self.handle_attack(event.data.get("damage", 0))
        elif event.type == "HEAL":
            self.handle_heal(event.data.get("heal", 0))
        elif event.type == "LOOT":
            self.handle_loot(event.data.get("item"))
    def handle_attack(self, damage: int):
        self.hp -= damage
    def handle_heal(self, heal: int):
        self.hp += heal
    def handle_loot(self, item: Item):
        if item:
            self.inventory.add_item(item)
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', hp={self.hp}, inventory={self.inventory})"
class Warrior(Player):
    def handle_attack(self, damage: int):
        reduced = int(damage * 0.9)  # уменьшение урона на 10%
        self.hp -= reduced
class Mage(Player):
    def handle_loot(self, item: Item):
        if item:
            boosted = Item(item.id, item.name, int(item.power * 1.1))  # +10% к силе предмета
            self.inventory.add_item(boosted)
e1 = Event("ATTACK", {"damage": 20})
e2 = Event("HEAL", {"heal": 15})
e3 = Event("LOOT", {"item": Item(1, "Magic Staff", 40)})
p = Player("Hero")
w = Warrior("Conan")
m = Mage("Merlin")
print("До событий:")
print(p)
print(w)
print(m)
p.handle_event(e1)
w.handle_event(e1)
m.handle_event(e1)
p.handle_event(e2)
w.handle_event(e2)
m.handle_event(e2)
p.handle_event(e3)
w.handle_event(e3)
m.handle_event(e3)
print("\nПосле событий:")
print(p)
print(w)
print(m)#7