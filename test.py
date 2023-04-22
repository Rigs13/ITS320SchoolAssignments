class Vehicle:

    def __init__(self, object_number, make, model):
        self.object_number = object_number
        self.make = make
        self.model = model

    def get_details(self):
        print('The make of Vehicle ', self.object_number, ' is: ', self.make)
        print('The model of Vehicle ', self.object_number, ' is: ', self.model)

def main():
    vehicle1 = Vehicle('1', 'Ferrari', '250 GTO')
    vehicle2 = Vehicle('2', 'Subaru', 'WRX')

    vehicle1.get_details()
    vehicle2.get_details()

if __name__ == '__main__':
    main()