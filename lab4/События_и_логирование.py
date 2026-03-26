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