from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from cliente import Cliente
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
        pos=(0, 100)
    )

    email_text_input = TextInput(
        foreground_color=(1, 1, 1, 1),
        multiline=False,
        size_hint=(.2, None),
        height=30,
        background_normal='',
        background_color=(0, 0, 0, 1),
        pos=(0, 200)
    )

    password_label = Label(
        text='Senha:',
        font_size=24,
        color=(0, 0, 0, 1),
        pos=(0, 0)
    )

    password_text_input = TextInput(
        foreground_color=(1, 1, 1, 1),
        multiline=False,
        password=True,
        size_hint=(.2, None),
        height=30,
        background_normal='',
        background_color=(0, 0, 0, 1),
        pos=(0, 100)
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

    login_button.bind(on_release=user_login)

    layout.add_widget(store_name_label)
    layout.add_widget(email_label)
    layout.add_widget(email_text_input)
    layout.add_widget(password_label)
    layout.add_widget(password_text_input)
    layout.add_widget(login_button)

    return layout


def user_login(instance):
    # email = email_text_input.text
    # password = password_text_input.text

    email = "gabriel@email.com"
    password = "12345"

    user = Cliente.autentica_cliente(email, password)

    if user is not None:
        layout.clear_widgets()
        return build_product_cart_screen(layout, user)
    # TODO else add popup
