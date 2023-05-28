class Mark: 
    def __init__(self):
        self.__mark = {}
    def get_mark(self):
        return self.__mark 
    def set_mark(self, m):
        self.__mark = m

m = Mark()
setattr(m, "New student", 10)
print(m)