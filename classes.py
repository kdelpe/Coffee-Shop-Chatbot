class Menu:
    def __init__(self, name, items, open_time, close_time):
        self.name = name
        self.items = items
        self.open_time = open_time
        self.close_time = close_time

    def __repr__(self):
        return self.name + ' available from ' + str(self.open_time) + ' - ' + str(self.close_time)




