class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no=1
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def show_status(self):
        if self.is_on == True:
            print(f'TV is on, channel {self.channel_no}')
        else:
            print("TV is off")
    def set_channel(self,new_channel_no):
            self.channel_no=new_channel_no


my_TV = TV()

my_TV.show_status()
my_TV.turn_on()
my_TV.show_status()
my_TV.set_channel(5)
my_TV.show_status()
my_TV.turn_off()
my_TV.show_status()
