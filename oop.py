class Car:
    def __init__(self,name,engine,torque):
        self.name = name
        self.engine = engine
        self.torque = torque

    def accelerate(self):
        print(self.name+" is accelerating.")

swift = Car("swift",2000,211)
fortuner = Car("fortuner",2500,150)
swift.accelerate()
fortuner.accelerate()
print(swift.engine,swift.torque)
print(fortuner.engine,fortuner.torque)