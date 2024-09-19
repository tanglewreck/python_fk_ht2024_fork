"""Kivy Hello World (2) implemented in pure Python (no kv file)"""

import sys
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

Window.size = (500, 500)


class HelloWorld(BoxLayout):
    """The root widget. Inherits BoxLayout"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class HelloWorldApp(App):
    """The App"""
    label_1_text = StringProperty("Hell0")
    label_2_text = StringProperty("W0rld")
    button_1_text = StringProperty("Press here to quit")

    def __init__(self, **kwargs):
        """This is here just for show"""
        super().__init__(**kwargs)

    def _update_rect(self, instance=None, value=None):
        """Update size and position of a widget's canvas"""
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def _quit_button_callback(self, instance=None, value=None):
        """Say good bye (with a delay)"""
        self.label_1.text = "[color=#ff0000]BYE[/color]"
        self.label_2.text = "[color=#cc5500]bye![/color]"
        self.button_1.text = "[color=#ffff00](quitting...)[/color]"
        delay = 2
        Clock.schedule_once(lambda foo: sys.exit(0), delay)

    def build(self):
        """Assemble the widgets"""
        self.root_widget = HelloWorld(orientation="vertical",
                                      spacing=20,
                                      padding=150)
        with self.root_widget.canvas.before:
            Color(0.9, 0.88, 0.82, 0.5)
            self.root_widget.rect = Rectangle(pos=self.root_widget.pos,
                                              size=self.root_widget.size)
        # Listen to size and position changes
        self.root_widget.bind(pos=self._update_rect, size=self._update_rect)

        # Define and add some widgets
        self.label_1 = Label(text=f"[i]{self.label_1_text}[/i]",
                             color=(0.1, 0.7, 0.9, 0.5),
                             outline_color=(1, 0, 0, 0.25),
                             font_size=100,
                             markup=True)

        self.label_2 = Label(text=f"[b]{self.label_2_text}[/b]",
                             color=(0, 1, 0, 0.5),
                             font_size=150,
                             markup=True)

        self.button_1 = Button(text=self.button_1_text,
                               color=(1, 1, 1, 1),
                               background_color=(0.05, 0.5, 1, 1),
                               markup=True,
                               on_release=self._quit_button_callback)

        self.root_widget.add_widget(self.label_1)
        self.root_widget.add_widget(self.label_2)
        self.root_widget.add_widget(self.button_1)

        # Change the background colour of the labels
        # and make them listen to changes of
        # position and size
        with self.label_1.canvas.before:
            Color(0.1, 0.3, 0.2, 0.25)  #
            self.label_1.rect = Rectangle(pos=self.label_1.pos,
                                          size=self.label_1.size)
        self.label_1.bind(pos=self._update_rect, size=self._update_rect)

        with self.label_2.canvas.before:
            Color(0.2, .5, .72, 0.9)  #
            self.label_2.rect = Rectangle(pos=self.label_2.pos,
                                          size=self.label_2.size)
        self.label_2.bind(pos=self._update_rect, size=self._update_rect)

        # with self.button_1.canvas.after:
        #    Color(0.01, 0.05, 0.02, 1)  #
        #    self.button_1.rect = Rectangle(pos=self.button_1.pos,
        #                                   size=self.button_1.size)
        # self.button_1.bind(pos=self._update_rect, size=self._update_rect)

        return self.root_widget


if __name__ == "__main__":
    """If we're not imported, run..."""
    hello_world_app = HelloWorldApp()
    hello_world_app.run()
    # OR: HelloWorldApp().run()
