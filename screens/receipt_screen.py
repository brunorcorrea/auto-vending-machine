from kivy.uix.button import Button
from kivy.uix.label import Label
import screens.home_screen
from datetime import datetime

global layout
global client
global sale


def show_products(qtd, label):
    global products_label
    global products_qtd
    global products_add_button

    cont = 10
    for i in range(len(label)):
        product_label = Label(
            text='{0} - {1} unidade(s)'.format(label[i].text, qtd[i].text),
            font_size=24,
            color=(0, 0, 0, 1),
            size_hint=(0, 0),
            pos_hint={'x': .145, 'top': .65 - cont/100}

        )

        cont += 5
        layout.add_widget(product_label)


def build_receipt_screen(main_layout, user, last_sale, cart_qtd, cart_label):
    global layout
    global total_value
    global client
    global sale
    layout = main_layout
    client = user
    sale = last_sale

    store_name_label = Label(
        text='24/7 Store',
        font_size=96,
        bold=True,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .15, 'top': .92}
    )

    client_label = Label(
        text='Cliente:',
        font_size=24,
        bold=True,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .08, 'top': .74}
    )

    name_label = Label(
        text='Nome: {0}'.format(client.nome),
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .1, 'top': .7}
    )

    cpf_label = Label(
        text='CPF: {0}'.format(client.cpf),
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .115, 'top': .67}
    )

    date_label = Label(
        text='Data: {0}\nHorário: {1}'.format(sale.data.strftime("%d-%m-%Y"), sale.data.strftime("%H:%M:%S")),
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .85, 'top': .8}
    )

    products_label = Label(
        text='Produtos:',
        font_size=24,
        bold=True,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .08, 'top': .60}
    )

    total_value = Label(
        text='Total: R$ {:.2f}'.format(float(sale.valor_total)),
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .785, 'top': 0.18}
    )

    return_home_button = Button(
        text='Tela Inicial',
        font_size=32,
        bold=True,
        size_hint=(.2, .10),
        pos_hint={'x': .75, 'top': 0.15},
        background_normal='',
        background_color=(0.66, 0.33, 0.33, 1)
    )

    return_home_button.bind(on_release=return_home)

    layout.add_widget(store_name_label)
    layout.add_widget(client_label)
    layout.add_widget(name_label)
    layout.add_widget(cpf_label)
    layout.add_widget(date_label)
    layout.add_widget(products_label)
    layout.add_widget(total_value)
    layout.add_widget(return_home_button)

    show_products(cart_qtd, cart_label)


def return_home(instance):
    layout.clear_widgets()
    return screens.home_screen.build_home_screen(layout)
