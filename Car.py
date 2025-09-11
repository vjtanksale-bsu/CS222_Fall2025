class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
def main():
    car0 = Car("Ford", "F-150")
    print(car0.make)
    print(car0.model)
    car1 = Car("Toyota", "Camry")
    print(car1.model)
    car1.model = "Corolla"
    print(car1.model)
    print(car0.make)
    print(car0.model)
main()