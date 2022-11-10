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

    return layout
