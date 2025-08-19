screens/passenger_page.py
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.driver_page import DriverPage
from screens.passenger_page import PassengerPage
from screens.ride_request_page import RideRequestPage

class SnappDriverApp(MDApp):
    def build(self):
        self.manager = ScreenManager()
        self.manager.add_widget(DriverPage(name="driver"))
        self.manager.add_widget(PassengerPage(name="passenger"))
        self.manager.add_widget(RideRequestPage(name="ride_request"))
        return self.manager

if __name__ == "__main__":
    SnappDriverApp().run()
