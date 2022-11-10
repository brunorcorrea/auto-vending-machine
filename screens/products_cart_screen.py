from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from database import Database

global layout
global db
db = Database()


def show_product():
    products = db.find_all_products()
    cont = 10
    for product in products:
        product_label = Label(
            text=product[1] + " R$" + str(product[5]),  # nome
            font_size=24,
            color=(0, 0, 0, 1),
            size_hint=(0, 0),
            pos_hint={'x': .15, 'top': .5 - cont/100}

        )

        qtd_product = Label(
            text=str(product[4]),  # quantidade
            font_size=24,
            color=(0, 0, 0, 1),
            size_hint=(0, 0),
            pos_hint={'x': .25, 'top': .5 - cont/100}
        )

        add_product = Button(
            text='+',
            font_size=24,
            color=(0, 0, 0, 1),
            size_hint=(0, 0),
            size=(100, 100),
            pos_hint={'x': .3, 'top': .5 - cont/100}
        )
        cont += 5
        layout.add_widget(product_label)
        layout.add_widget(qtd_product)
        layout.add_widget(add_product)


def build_product_cart_screen(main_layout, user):
    global layout
    layout = main_layout

    store_name_label = Label(
        text='24/7 Store',
        font_size=96,
        bold=True,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .15, 'top': .92}
    )

    user_label = Label(
        text='Bem vindo, {0}.'.format(user.nome),
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'right': 0.9, 'top': .95}
    )

    total_value = Label()

    finish_sale_button = Button(
        text='Finalizar Compra',
        font_size=32,
        bold=True,
        size_hint=(.2, .10),
        pos_hint={'x': .75, 'top': 0.15},
        background_normal='',
        background_color=(0.66, 0.33, 0.33, 1)
    )

    layout.add_widget(store_name_label)
    layout.add_widget(user_label)
    layout.add_widget(finish_sale_button)

    show_product()
