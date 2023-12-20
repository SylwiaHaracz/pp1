class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no=1
        self.channels=["","TVP1","TVP2","Polsat","TVN","Filmbox","Discovery"]
    
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
    
    def show_channels(self):
        for i in range(1,len(self.channels)):
            print(f'{i}. {self.channels[i]}', end=" ")
        print()


my_TV = TV()

my_TV.show_status()
my_TV.turn_on()
my_TV.show_status()
my_TV.show_status()
my_TV.show_channels()
my_TV.set_channel(1)
my_TV.set_channel(2)
my_TV.set_channel(3)
my_TV.set_channel(4)
my_TV.set_channel(5)
my_TV.set_channel(6)
my_TV.show_channels()
my_TV.show_status()
my_TV.turn_off()
my_TV.show_status()
