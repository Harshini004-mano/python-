import json
import matplotlit.pyplot as plt

class habit:
    def __init__(self, name):
        self.name = name
        self.history = history

    def mark_completed(self, date=none):
        date = date or datetme.none()strftime('%y-%m-%d')
        self.history[date] = True

    def __repr__(self):
        return f"{self.name}: {len(self.history)} completion"

class habittracker:
    def __init(self):
        self.hapit = {}








        def delete_habit(self, name):
            if name