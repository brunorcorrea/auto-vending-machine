from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


global layout


def build_login_screen(main_layout):
    global layout
    layout = main_layout

    store_name_label = Label(
        text='24/7 Store',
        font_size=96,
        bold=True,
        color=(0, 0, 0, 1),
        pos=(0, 1024 / 3),
    )

    email_label = Label(
            text='Email:',
            font_size=24,
            color=(0, 0, 0, 1),
            pos=(0, 100)
        )

    layout.add_widget(
        TextInput(
            foreground_color=(1, 1, 1, 1),
            multiline=False,
            size_hint=(.2, None),
            height=30,
            background_normal='',
            background_color=(0, 0, 0, 1),
            pos=(0, 100)
        )
    )

    password_label = Label(
        text='Senha:',
        font_size=24,
        color=(0, 0, 0, 1),
        pos=(0, 0)
    )

    layout.add_widget(
        TextInput(
            foreground_color=(1, 1, 1, 1),
            multiline=False,
            size_hint=(.2, None),
            height=30,
            background_normal='',
            background_color=(0, 0, 0, 1),
            pos=(0, 200)
        )
    )

    login_button = Button(
        text='Login',
        font_size=32,
        bold=True,

        size_hint=(.15, .10),
        pos=(0, 0),
        background_normal='',
        background_color=(0.66, 0.33, 0.33, 1)
    )

    layout.add_widget(store_name_label)
    layout.add_widget(email_label)
    layout.add_widget(password_label)
    layout.add_widget(login_button)

    return layout
