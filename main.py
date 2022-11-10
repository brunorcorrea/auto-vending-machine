from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from cliente import Cliente
from database import *

Window.clearcolor = (0.85, 0.85, 0.85, 1)
Window.maximize()

layout = FloatLayout(
    size=(1920, 1080)
)


class MyApp(App):

    def build(self):
        return layout


class LoginScreen:
    layout = FloatLayout(
        size=(1920, 1080)
    )

    def __init__(self):
        store_name_label = Label(
            text='24/7 Store',
            font_size=96,
            bold=True,
            color=(0, 0, 0, 1),
            pos=(0, 1024 / 3),
        )

        email_label = Label(
                text='Email',
                font_size=24,
                color=(0, 0, 0, 1),
                pos=(1440 / 2 + 1440 * 0.2, 1024 / 8)
            )

        layout.add_widget(
            TextInput(
                pos=(0, 1024 / 8)
            )
        )

        layout.add_widget(store_name_label)
        layout.add_widget(email_label)


def open_login_screen(instance):
    layout.clear_widgets()  # limpa todos os elementos da tela
    return LoginScreen()


class HomeScreen:
    store_name_label = Label(
        text='24/7 Store',
        font_size=96,
        bold=True,
        color=(0, 0, 0, 1),
        pos=(0, 1024 / 3),
    )

    slogan_label = Label(
        text='Disponível a qualquer momento!',
        font_size=32,
        color=(0, 0, 0, 1),
        pos=(0, 1024 / 4)
    )

    signin_button = Button(
        text='Cadastrar-se',
        font_size=32,
        bold=True,

        size_hint=(.15, .10),
        pos=(1440 / 2 + 1440 * 0.075, 1024 / 10),
        background_normal='',
        background_color=(0.66, 0.33, 0.33, 1)
    )

    login_button = Button(
        text='Já é cliente? Entrar',
        font_size=20,
        bold=True,
        color=(0, 0, 0, 1),
        size_hint=(.4, .10),
        pos=(1440 / 2 - 0.09 * 1440, 1024 / 26),
        background_normal='',
        background_color=(0, 0, 0, 0)
    )

    login_button.bind(on_release=open_login_screen)

    layout.add_widget(store_name_label)
    layout.add_widget(slogan_label)
    layout.add_widget(signin_button)
    layout.add_widget(login_button)


if __name__ == '__main__':
    global bd
    bd = Database()
    bd.create_database()
    MyApp().run()
