from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        
        # Add a welcome label
        screen.add_widget(MDLabel(text="Welcome to Snapp Driver", halign="center"))
        
        # Add a start button
        screen.add_widget(MDRaisedButton(text="Start", pos_hint={"center_x": 0.5, "center_y": 0.4}))
        
        return screen

if __name__ == "__main__":
    MainApp().run()