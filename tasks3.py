class passenger_ticket:
    def __init__(self,passenger_name,PNR):
        self.passenger_name=passenger_name
        self.PNR=PNR
    def setpassnger_name(selfself,passenger_name):
        self.passenger_name=passenger_name
    def getpassenger_name(self):
        return self.passenger_name

    def setPNR(self,PNR):
        self.PNR=PNR
    def getPNR(self):
        return self.PNR

    sc=passenger_ticket(self,passenger_name,PNR)
    print("enter the values from the user")
    passenger_name = str(input("enter the passenger name"))
    PNR = int(input("enter the PNR"))  # user will enter the train_id

    print("The passenger name is", sc.getpassenger_name())
    print("The PNR no is", sc.getPNR())
