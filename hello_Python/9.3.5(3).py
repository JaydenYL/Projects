class car():

    def __init__(self, make, model, year ):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def describe_car(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has '+str(self.odometer)+' miles on it.')

    def update_odometer(self, mileage):
        if mileage < self.odometer:
            print('You cannot roll back the odometer !')
        else:
            print('The odometer has updated !')

    def increase_odometer(self, increment):
        self.odometer += increment

class Battery():

    def __init__(self, battery_volume = 70):
        self.battery_volume = battery_volume

    def descibe_battery(self):
        print('This car has a '+str(self.battery_volume)+' KWh battery .')

    def get_range(self):
        """打印一条消息，指出电池的续航"""
        if self.battery_volume == 70:
            range = 240
        elif self.battery_volume == 85:
            range  = 270
        message = 'This car can approximately go '+str(range)+' miles on full charge.'
        print(message)

class electrical_car(car):

    def __init__(self, make, model,year):
        super().__init__(make, model, year)
        #注意这句话的意思

        self.battery= Battery() # KWh

my_tesla = electrical_car('Tesla', 'model s', '2019')
print(my_tesla.describe_car())
my_tesla.battery.descibe_battery()
my_tesla.battery.get_range()
