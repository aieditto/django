class Company:
    def __init__(self,name, address):
        self.name=name
        self.bus=[]
        self.routes=[]
        self.drivers=[]
        self.counter=[]
        self.manager=[]
        self.supervisor=[]
        pass

class Driver:
    def __init__(self, license, name, age):
        self.license=license
        self.name=name
        self.age=age

class Counter:
    def __init__(self) -> None:   
        pass

class Passenger:
    pass

class supervisor:
    pass