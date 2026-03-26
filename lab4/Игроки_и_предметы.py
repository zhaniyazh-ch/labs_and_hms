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