from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class ManagerScreen(Screen):
    txt_cheese_pizza_price = StringProperty("0")
    txt_hawaiian_pizza_price = StringProperty("0")
    txt_pepperoni_pizza_price = StringProperty("0")
    
    def welcome(self):
        self.manager.current = "welcome_screen"


    def save(self):
        print("In ManagerScreen - save(), ")

        # assigns value in customer screen
        customer_screen = self.manager.get_screen("customer_screen")
        customer_screen.lbl_cheese_pizza_price = self.ids.txt_cheese_pizza_price.text

        customer_screen.lbl_hawaiian_pizza_price = self.ids.txt_hawaiian_pizza_price.text

        customer_screen.lbl_pepperoni_pizza_price = self.ids.txt_pepperoni_pizza_price.text

        #go to customer screen
        self.manager.current = "customer_screen"


