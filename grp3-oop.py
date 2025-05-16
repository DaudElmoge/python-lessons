class Phone:

    phones=[]

    tax_rate=0.10
    discount=0.05
    def __init__(self,name,serial_number,color,price,model):
        self._name=name
        self._serial_number=serial_number
        self.color=color
        self.price=price
        self.model=model
        Phone.phones.append(self)  # Add instance to the class-level list


    def call(self):
        return f"Phone of model {self.model} can call"
    #getter method -> name
    @property
    def name(self):
        return self._name

    #getter method->serial_number
    @property
    def serial_number(self):
        return self._serial_number

    #getter method->price
    @property
    def price(self):
        return self._price

    #Setter->price
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Price cannot be zero or negative")
        self._price = new_price
        
    #methods -> instance
    def get_final_price(self):
        taxed_price=self.price + self.price * Phone.tax_rate
        discounted_price=taxed_price - self.price * Phone.discount
        return discounted_price
    
    @classmethod
    def tax_rate_update(cls,new_tax_rate):
        if not 0 <= new_tax_rate <= 1:
            raise ValueError("Tax rate must be between 0 and 1")
        cls.tax_rate=new_tax_rate

    def __repr__(self):
        return f"<Phone {self._name} {self._serial_number} {self.color} {self.price} {self.model}>"    
    
 #example usage
phone1 = Phone("iPhone", "SN001", "Black", 1200,"14")
phone2 = Phone("Galaxy", "SN002", "Blue", 1000,"S23")

print (phone1.name)
print (phone2.serial_number)   
             
class Samsung(Phone):
    def __init__(self, name="Samsung", serial_number="SN002", color="White", price=1000, model="S23"):
        super().__init__(name, serial_number, color, price, model)

phone2 = Samsung()
print("<Samsung>", phone2.call())

class Iphone(Phone):
    def __init__(self,name="iPhone", serial_number="SN001", color="Black", price=1200, model="14"):
        super().__init__(name, serial_number, color, price, model)

phone1=Iphone()
print("<iPhone>",phone1.call())        

# Show all created phones
print("All phones:", Phone.phones)
        