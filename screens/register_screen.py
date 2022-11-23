from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from cliente import Cliente
import screens.home_screen

global layout
global name_text_input
global cpf_text_input
global email_text_input
global tel_text_input
global password_text_input


def build_register_screen(main_layout):
    global layout
    global name_text_input
    global cpf_text_input
    global email_text_input
    global tel_text_input
    global password_text_input

    layout = main_layout

    store_name_label = Label(
        text='24/7 Store',
        font_size=96,
        bold=True,
        color=(0, 0, 0, 1),
        pos=(0, 1080 / 3)
    )

    name_label = Label(
        text='Nome:',
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .4, 'top': .7}
    )

    name_text_input = TextInput(
        foreground_color=(1, 1, 1, 1),
        multiline=False,
        height=30,
        background_normal='',
        background_color=(0, 0, 0, 1),
        size_hint=(.2, .04),
        pos_hint={'x': .42, 'top': .718},
        halign='center'
    )

    cpf_label = Label(
        text='CPF:',
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .4, 'top': .6}
    )

    cpf_text_input = TextInput(
        foreground_color=(1, 1, 1, 1),
        multiline=False,
        height=30,
        background_normal='',
        background_color=(0, 0, 0, 1),
        size_hint=(.2, .04),
        pos_hint={'x': .42, 'top': .618},
        halign='center'
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

    tel_label = Label(
        text='Telefone:',
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .393, 'top': .4}
    )

    tel_text_input = TextInput(
        foreground_color=(1, 1, 1, 1),
        multiline=False,
        height=30,
        background_normal='',
        background_color=(0, 0, 0, 1),
        size_hint=(.2, .04),
        pos_hint={'x': .42, 'top': .418},
        halign='center'
    )

    password_label = Label(
        text='Senha:',
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .4, 'top': .3}
    )

    password_text_input = TextInput(
        foreground_color=(1, 1, 1, 1),
        multiline=False,
        password=True,
        height=30,
        background_normal='',
        background_color=(0, 0, 0, 1),
        size_hint=(.2, .04),
        pos_hint={'x': .42, 'top': .318},
        halign='center'
    )

    register_button = Button(
        text='Cadastrar-se',
        font_size=32,
        bold=True,
        size_hint=(.15, .10),
        pos_hint={'x': .425, 'top': .2},
        background_normal='',
        background_color=(0.66, 0.33, 0.33, 1)
    )

    register_button.bind(on_release=user_register)

    layout.add_widget(store_name_label)
    layout.add_widget(name_label)
    layout.add_widget(name_text_input)
    layout.add_widget(cpf_label)
    layout.add_widget(cpf_text_input)
    layout.add_widget(email_label)
    layout.add_widget(email_text_input)
    layout.add_widget(tel_label)
    layout.add_widget(tel_text_input)
    layout.add_widget(password_label)
    layout.add_widget(password_text_input)
    layout.add_widget(register_button)

    return layout


def user_register(instance):
    name = name_text_input.text
    cpf = cpf_text_input.text
    email = email_text_input.text
    tel = tel_text_input.text
    password = password_text_input.text

    if name == '' or cpf == '' or email == '' or tel == '' or password == '':
        popup = Popup(title='Erro',
                      content=Label(text='Preencha todos os campos!'),
                      pos_hint={'x': .4, 'top': .8},
                      size_hint=(None, None), size=(400, 400))
        popup.open()
    else:
        user = Cliente.cria_cliente(name, cpf, email, tel, password)

        if user.id is not None:
            layout.clear_widgets()
            return screens.home_screen.build_home_screen(layout)
