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
inv = Inventory