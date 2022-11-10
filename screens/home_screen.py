from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from screens.login_screen import build_login_screen


global layout


def build_home_screen(main_layout):
    global layout
    layout = main_layout

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

    return layout


def open_login_screen(instance):
    layout.clear_widgets()  # limpa todos os elementos da tela
    return build_login_screen(layout)
