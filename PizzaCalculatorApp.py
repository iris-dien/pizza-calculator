from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager 
from WelcomeScreen  import WelcomeScreen 
from ManagerScreen import ManagerScreen
from CustomerScreen import CustomerScreen


class PizzaCalculatorApp(App): 
    
    screen_manager = ScreenManager()

    def build(self): 
        self.title = " Iris' Pizza Calculator" 
        welcome_screen = WelcomeScreen(name="welcome_screen")
        manager_screen = ManagerScreen(name="manager_screen")
        customer_screen = CustomerScreen(name="customer_screen")

        
        
        self.screen_manager.add_widget(welcome_screen) 
        self.screen_manager.add_widget(manager_screen)
        self.screen_manager.add_widget(customer_screen)

        return self.screen_manager 

if(__name__ == "__main__"):
    PizzaCalculatorApp().run() 


          