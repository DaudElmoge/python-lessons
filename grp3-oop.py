class Phone:
    tax_rate=0.10
    discount=0.05
    def __init__(self,name,serial_number,color,price):
        self._name=name
        self._serial_number=serial_number
        self.color=color
        self.price=price

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
    def price(self,new_price):
        if not new_price > 0:
            self.price=new_price
            raise ValueError("Price cannot ve zero")
        
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
    

            
             