class TV():
    def __init__(self):
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def show_status(self):
        if self.is_on == True:
            print("TV is on")
        else:
            print("TV is off")
        
my_TV = TV()

my_TV.show_status()
my_TV.turn_on()
my_TV.show_status()
my_TV.turn_off()
my_TV.show_status()