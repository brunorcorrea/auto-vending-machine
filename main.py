from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from cliente import Cliente
from database import *
from screens.home_screen import build_home_screen

Window.clearcolor = (0.85, 0.85, 0.85, 1)
Window.maximize()

layout = FloatLayout(
    size=(1920, 1080)
)


class MyApp(App):

    def build(self):
        return build_home_screen(layout)


if __name__ == '__main__':
    global bd
    bd = Database()
    bd.create_database()
    MyApp().run()
