class Player:
    def __init__(self, _id, name, hp):
        self._id = _id
        self._name = name.strip().title()
        self._hp = hp if hp >= 0 else 0
    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"
    def __del__(self):
        print(f"Player {self._name} удалён")
p = Player(1, " john ", 120)
print(p)#1
class Player:
    def __init__(self, _id, name, hp):
        self._id = _id
        self._name = name.strip().title()
        self._hp = hp if hp >= 0 else 0
    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"
    def __del__(self):
        print(f"Player {self._name} удалён")
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
p = Player.from_string("2, alice , 90")
print(p)#2
class Item:
    def __init__(self, id, name, power):
        self.id = id
        self.name = name.strip().title()
        self.power = power
    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"
    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.id == other.id
    def __hash__(self):
        return hash(self.id)
i = Item(1, " Sword ", 50)
print(i)#3
class Item:
    def __init__(self, id: int, name: str, value: int):
        self.id = id
        self.name = name
        self.value = value
    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', value={self.value})"
    def __eq__(self, other):
        if isinstance(other, Item):
            return self.id == other.id
        return False
    def __hash__(self):
        return hash(self.id)
class Inventory:
    def __init__(self):
        self._items = []
    def add_item(self, item: Item):
        for i in self._items:
            if i.id == item.id:
                return
        self._items.append(item)
    def remove_item(self, item_id: int):
        self._items = [item for item in self._items if item.id != item_id]
    def get_items(self) -> list[Item]:
        return self._items
    def unique_items(self) -> set[Item]:
        return set(self._items)
    def to_dict(self) -> dict[int, Item]:
        return {item.id: item for item in self._items}
i1 = Item(1, "Sword", 50)
i2 = Item(2, "Bow", 30)
i3 = Item(1, "Sword", 50)
inv = Inventory()
inv.add_item(i1)
inv.add_item(i2)
inv.add_item(i3)
print("Список предметов:")
for item in inv.get_items():
    print(item)
print("\nУникальные предметы:")
print(inv.unique_items())
print("\nСловарь предметов:")
print(inv.to_dict())#4
class Item:
    def __init__(self, id: int, name: str, power: int):
        self.id = id
        self.name = name
        self.power = power
    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"
    def __eq__(self, other):
        if isinstance(other, Item):
            return self.id == other.id
        return False
    def __hash__(self):
        return hash(self.id)
class Inventory:
    def __init__(self):
        self._items = []
    def add_item(self, item: Item):
        for i in self._items:
            if i.id == item.id:
                return
        self._items.append(item)
    def remove_item(self, item_id: int):
        self._items = [item for item in self._items if item.id != item_id]
    def get_items(self) -> list[Item]:
        return self._items
    def unique_items(self) -> set[Item]:
        return set(self._items)
    def to_dict(self) -> dict[int, Item]:
        return {item.id: item for item in self._items}
    def get_strong_items(self, min_power: int) -> list[Item]:
        return [item for item in self._items if (lambda x: x.power >= min_power)(item)]
i1 = Item(1, "Sword", 50)
i2 = Item(2, "Bow", 30)
i3 = Item(3, "Dagger", 10)
inv = Inventory#5