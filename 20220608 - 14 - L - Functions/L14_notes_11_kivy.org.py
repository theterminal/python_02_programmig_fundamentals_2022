# 20220614 - Python Code - Functions - Lecture
# 11 - kivy.org

from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        return Button(text='Hello World')


TestApp().run()
