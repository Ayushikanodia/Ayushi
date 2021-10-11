from abc import ABC,abstractmethod

class Service(ABC):
        @abstractmethod
        def laundary(self):
            pass
        @abstractmethod
        def cleaning(self):
            pass
        @abstractmethod
        def ac(self):
            pass
        @abstractmethod
        def wifi(self):
           pass
        @abstractmethod
        def food(self):
            pass

class Facility(Service):
    def laundary():
        return 1000
    def cleaning():
        return 1000
    def ac():
        return 1000
    def wifi():
        return 1000
    def food():
        return 1000
    def display1(self):
        amount=0
        print("Do you want laundary facility")
        l=input("Enter Y or N")
        if l=='Y'or l=='y':
            amt=Facility.laundary()
            amount=amount+amt
        print("Do you need cleaning facility")
        c=input("Enter Y or N")
        if c=='Y'or c=='y':
            amt=Facility.cleaning()
            amount=amount+amt
        print("Do you need Ac faciity")
        ac=input("Enter Y or N")
        if(ac=='Y' or ac=='y'):
            amt=Facility.ac()
            amount=amount+amt
        print("Do you need Wifi facility")
        wifi=input("Enter Y or N")    
        if( wifi=='Y' or wifi=='y'):
            amt=Facility.wifi()
            amount=amount+amt
        print("Do you want food facility")
        food=input("Enter Y or y")
        if food=='Y' or food=='y':
            amount=amount+Facility.food()
        return amount

class OneSitter(Facility):
    def disp(self):
        amt=super().display1()
        amt=amt+5000
        print(f"Total rent which you have to pay: {amt}")
        print("For any other information You can contact via No. +917355645856")

class twoSitter(Facility):
    def disp(self):
         amt=super().display1()
         if amt!=0:
            amt=amt-(amt*0.25)
         amt=amt+3500
         print(f"Total rent which You have to pay :  {amt}")
         print("For any other inforamtion you can contact via No.  +917355645856")

class price():
    def display(self):
        print("\t\t\t\t\tPrice of One Sitter room: 5000")
        print("\t\t\t\t\tprice of Two Sitter room: 3500")
        print("If you will take Two sitter room then you will also get 25% off in the facilities which we provide")
        print("\t\t\t\t\tHere are the facilities: \n \t\t\t\t\tLaundary \n \t\t\t\t\t Cleaning \n\t\t\t\t\t AC\n \t\t\t\t\t WIFI\n \t\t\t\t\t FOOD   ")


print("=======Welcome=======")
print("Please enter your name")
name=input()
print(f"========Hello {name} we welcome you to our PG=========")
print("Do you want to rent a room")
p=price()
ch=input("Enter Y or N")
if ch=='Y' or ch=='y':
    p.display()
    print("Enter the type of room ")
    print("1 Sitter")
    print("2 Sitter")
    type_of_room=int(input())
    if(type_of_room==1):
         s=OneSitter()
         s.disp()
    else :
        s=twoSitter()
        s.disp()
else :
    print("Sorry!! No other Service available")
print("you are done ")
