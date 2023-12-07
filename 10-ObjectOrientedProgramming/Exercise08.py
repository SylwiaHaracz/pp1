class Phone():
    def __init__(self, name, brand, battery):
        self.name = name
        self.brand = brand
        self.battery = battery
        self.is_on = False
    
    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False

    def battery_percentage(self, percentage):
        self.battery = percentage

my_phone = Phone("iPhone", "Apple", 50)

print(my_phone.name)
my_phone.battery_percentage(99)
print(my_phone.battery)