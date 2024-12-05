from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.clock import Clock

UI = '''
MDScreenManager:
    MDScreen:
        Widget:
            id : square
            size_hint : None, None
            size : 100, 100
            pos : 100, 100
            canvas:
                Color : 
                    rgba : 135/255, 31/255, 120/255, 1
                Rectangle:
                    size : self.size
                    pos : self.pos
        
        Widget:
            id : triangle
            size_hint : None, None
            size : 100, 100
            pos : 350, 100
            canvas:
                Color : 
                    rgba : 227/255, 11/255, 93/255, 1
                Mesh:
                    vertices : [self.x + 0, self.y + 0, 0, 0, self.x + self.width/2, self.y + self.width/2, 0, 0, self.x + self.width, self.y + 0, 0, 0]
                    indices : 0, 1, 2
                    mode : "triangle"                        
        
        Widget:
            id : circle
            size_hint : None, None
            size : 100, 100
            pos : 600, 100
            canvas:
                Color : 
                    rgba :255/255, 255/255, 0/255, 1
                Ellipse:
                    size : self.size
                    pos : self.pos
        
'''

class App(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.start_animation, 3)

    def start_animation(self, dt):
        Animation(pos = (250, 70), size = (300, 300), duration = 2).start(self.root.ids.square)
        Animation(pos = (250, 370), size = (300, 300), duration = 2).start(self.root.ids.triangle)
        Animation(pos = (380, 400), size = (50, 50), duration = 2).start(self.root.ids.circle)
        

    def build(self):
        ui = Builder.load_string(UI)
        return ui

if(__name__ == "__main__"):
    App().run()
