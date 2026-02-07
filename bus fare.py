class busfare:
    def __init__(self,fare):
        self.fare=fare
       

class sub(busfare):
    def __init__(self,passengers,fare):
        super().__init__(fare)
        self.passengers=passengers
        self.total_fare=self.fare*self.passengers
        
        


totalfare=sub(55,100)
print(totalfare.total_fare)
