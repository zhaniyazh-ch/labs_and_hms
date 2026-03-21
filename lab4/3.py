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
print(i)