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
print(inv.to_dict())