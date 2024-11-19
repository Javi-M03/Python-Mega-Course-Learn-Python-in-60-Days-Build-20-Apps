import pandas as pd

df = pd.read_csv("hotels.csv",dtype={"id":str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pd.read_csv("card_security.csv",dtype=str)

"""
User can see list of hotels
User can book hotels
User can get reservation tickets
"""


class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id,"name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
       availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
       if availability == "yes":
           return True
       else:
           return False 


class ReservationTicket:
    def __init__(self,customer_name,hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object


    def generate(self): 
        content =  f"""
                    Thank you for your reservation!
                    Here is your booking data!:
                    Name: {self.customer_name}
                    Hotel: {self.hotel.name}
                    """
        return content

class CreditCard:
    def __init__(self,number):
        self.number = number
        

    def validate(self,expiration,holder,cvc):
        card_data = {"number":self.number, "expiration": expiration,
                     "holder":holder, "cvc":cvc}
        if card_data in df_cards:
            return True
        else:
            return False
        
class SecureCreditCard(CreditCard):
    def authenticate(self,given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else: 
            return False

class Spa(Hotel):
    def spa_reservation(self):
        anwser = input("Do you want to book an spa reservation?")
        if anwser == "yes":
            print("your reservation is booked")
        else: 
            print("Have a nice day!")


        

print(df)
hotel_ID = input("Enter the id of an hotel: ")
hotel = Spa(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number = "1234567890123456")
    if credit_card.validate(expiration = "12/26", holder = "JOHN SMITH",cvc= "123"):
        if credit_card.authenticate("mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name,hotel)
            print(reservation_ticket.generate())
            hotel.spa_reservation()
        else:
            print("CreditCard authentication Fail")
    else:
        print("There was a problem with your credit card")
else:
    print("Hotel is not free")

