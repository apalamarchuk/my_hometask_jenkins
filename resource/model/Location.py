class Location:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        for loc in self.data:
            if not self.data[loc] == other.data[loc]:
                return False
        return True
