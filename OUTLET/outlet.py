from Hourly_power_price import prices
import datetime
from datetime import time
class outlet:
    def __init__(self) -> None:
        self.outlets=[1,2,3,4,5,6]
        self.prices=prices
        self.myprices= int(1.2) * self.prices
        
    def add_chargers(self,outlet_number):
        self.outlets.append(outlet_number)
        print("charger {} added".format(outlet_number))
        
    def display_chargers(self):
        print("Currently available chargers are {}".format(self.outlets))
        
    def book_charger(self,charger_number):
        if charger_number in self.outlets:
            self.time_now = datetime.datetime.now().hour()
            self.outlets.remove(charger_number)  
            print("you have booked outlet number {} at {} o'clock".format(charger_number,self.time_now))
            print("You will be charged ${} for each kilowatt hour per charger.".format(self.myprices))
        else:
            print("Charger not currently available, please select another")
            
    def end_charging(self):
        now = datetime.datetime.now().hour()
        rentalPeriod = now - self.time_now
        # hourly bill calculation
        if rentalPeriod!=0:
                bill = round(rentalPeriod) * self.myprices* 7.2 # 7.2kW is the average power used by an EV to charge per hour
                print("Thanks for charging with us, your bill is {}".format(bill))
        else:
            print("Are you sure you charged with us?")
        
            
    
    
    

  
    
    
            
        
        