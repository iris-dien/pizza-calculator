from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen



class CustomerScreen(Screen):
    """
        This class will be the customer page for the app
    """



    lbl_hawaiian_pizza_price = NumericProperty(0)
    lbl_cheese_pizza_price = NumericProperty(0)
    lbl_pepperoni_pizza_price = NumericProperty(0)



    txt_hawaiian_pizza_quanity = NumericProperty(0)
    txt_cheese_pizza_quanity = NumericProperty(0)
    txt_pepperoni_pizza_quanity = NumericProperty(0)


    hawaiian_order = 0
    cheese_order = 0
    pepperoni_order = 0

    sales_tax_amount = NumericProperty(0)
    total_order = NumericProperty(0)
    grand_total = NumericProperty(0)
    

    def hawaiian_quanity_on_change(self):
        if(self.ids.txt_hawaiian_pizza_quanity.text is not""):
            self.hawaiian_order = int(self.ids.txt_hawaiian_pizza_quanity.text) * float(self.lbl_hawaiian_pizza_price)
        
            self.calculate_total_order()

        else:

            self.ids.txt_hawaiian_pizza_quanity.text = "0"

    def cheese_quanity_on_change(self):
        if(self.ids.txt_cheese_pizza_quanity.text is not ""):
            self.cheese_order = int(self.ids.txt_cheese_pizza_quanity.text) * float(self.lbl_cheese_pizza_price)

            self.calculate_total_order()
        else:
            self.ids.txt_cheese_pizza_quanity.text = "0"


    def pepperoni_quanity_on_change(self):
        if(self.ids.txt_pepperoni_pizza_quanity.text is not ""):
            self.pepperoni_order = int(self.ids.txt_pepperoni_pizza_quanity.text) * float(self.lbl_pepperoni_pizza_price)

            self.calculate_total_order()
        else:
            self.ids.txt_pepperoni_pizza_quanity.text = "0"


    def calculate_total_order(self):
        self.total_order = self.hawaiian_order +\
            self.cheese_order + self.pepperoni_order

        self.calculate_sales_tax_amount()

    def calculate_sales_tax_amount(self):
        """
        # 4. calculate tax (assume 8%)


        TODO: make tax rate dynamic
        """

        tax_rate = .08



        self.sales_tax_amount = self.total_order * tax_rate

        self.calculate_grand_total()


    def calculate_grand_total(self):
        self.grand_total = self.total_order + self.sales_tax_amount
      
    def welcome(self):
        # go tom welcome screem
        self.manager5.current = "welcome_screen"