from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (380, 768)
Window.top = 0
Window.left = 986
UI ='''
MDScreenManager:
    MDScreen:
        MDBoxLayout:
            orientation : "vertical"
            spacing : "15dp"
            padding : "15dp"
            MDTextField:
                id : num1
                hint_text : "Enter first number"
                mode : "rectangle"
            MDTextField:
                id : num2
                hint_text : "Enter second number"
                mode : "rectangle"
            MDRaisedButton:
                text : "Calculate"
                font_size : "15sp"
                pos_hint : {"center_x" : 0.5}
                on_release : app.callback()
                elevation : 0
            MDLabel:
                text : "Your result is :"
                height : self.texture_size[1]
                size_hint_y : None
            MDLabel:
                id : result
                text : ""
                height : self.texture_size[1]
                size_hint_y : None
            MDWidget:
'''
class Adder(MDApp):
    def callback(self):
        try: 
            self.root.ids.result.text = str(float(self.root.ids.num1.text) + float(self.root.ids.num2.text))
        except:
            self.root.ids.result.text = "INVALID INPUT!"
    def build(self):
        return Builder.load_string(UI)
root = Adder()
if __name__ == "__main__":
    root.run()