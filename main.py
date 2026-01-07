# UPDATE
class MyDict:
    def __init__(self):
        self.data = {}

    def update(self, other):
        for key in other:
            self.data[key] = other[key]

d = MyDict()
d.data = {"a": 1, "b": 2}

d.update({"b": 20, "c": 30})

print(d.data)
