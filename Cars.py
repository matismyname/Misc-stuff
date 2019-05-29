#A car class, nothing more and nothing less

class Cars:

    def __init__(self, name, model, by):
        self.name = name
        self.model = model
        self.by = by
    
    @property
    def message(self):
        return "This is a {} {} and it was built in the year {}.".format(self.name, self.model, self.by)

    @message.setter
    def message(self, msg):
        name, model = msg.split(" ")
        self.name = name
        self.model = model


tesla = Cars("Tesla", 3, 2010)
print(tesla.message)