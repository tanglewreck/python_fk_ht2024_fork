"""Hello World (1)"""

from kivy.app import App
from kivy.uix.label import Label

class HelloWorldApp(App):
    def build(self):
        return Label(text="Hello World (1)")

# hello_world_app = HelloWorld()
# hello_world_app().run()

HelloWorldApp().run()

