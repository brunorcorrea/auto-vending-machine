from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from model.cliente import Cliente
from screens.products_cart_screen import build_product_cart_screen

global layout
global email_text_input
global password_text_input


def build_login_screen(main_layout):
    global layout
    global email_text_input
    global password_text_input

    layout = main_layout

    store_name_label = Label(
        text='24/7 Store',
        font_size=96,
        bold=True,
        color=(0, 0, 0, 1),
        pos=(0, 1080 / 3)
    )

    email_label = Label(
        text='Email:',
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .4, 'top': .5}
    )

    email_text_input = TextInput(
        foreground_color=(1, 1, 1, 1),
        multiline=False,
        height=30,
        background_normal='',
        background_color=(0, 0, 0, 1),
        size_hint=(.2, .04),
        pos_hint={'x': .42, 'top': .518},
        halign='center'
    )

    password_label = Label(
        text='Senha:',
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .4, 'top': .4}
    )

    password_text_input = TextInput(
        foreground_color=(1, 1, 1, 1),
        multiline=False,
        password=True,
        height=30,
        background_normal='',
        background_color=(0, 0, 0, 1),
        size_hint=(.2, .04),
        pos_hint={'x': .42, 'top': .418},
        halign='center'
    )

    login_button = Button(
        text='Login',
        font_size=32,
        bold=True,
        size_hint=(.15, .10),
        pos_hint={'x': .425, 'top': .2},
        background_normal='',
        background_color=(0.66, 0.33, 0.33, 1)
    )

    login_button.bind(on_release=user_login)

    layout.add_widget(store_name_label)
    layout.add_widget(email_label)
    layout.add_widget(email_text_input)
    layout.add_widget(password_label)
    layout.add_widget(password_text_input)
    layout.add_widget(login_button)

    return layout


def user_login(instance):
    email = email_text_input.text
    password = password_text_input.text

    user = Cliente.autentica_cliente(email, password)

    if user is not None:
        layout.clear_widgets()
        return build_product_cart_screen(layout, user)
    # TODO else add popup
