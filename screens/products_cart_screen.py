import time
import screens.home_screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from database import Database
from venda import Venda
from datetime import datetime

global layout
global stock
global cart
global total_value
global products_label
global products_qtd
global products_add_button
global cart_label
global cart_qtd
global cart_remove_button
global db
global cart_cont
global client
db = Database()
products_label = []
products_qtd = []
products_add_button = []
cart_label = []
cart_qtd = []
cart_remove_button = []
cart_cont = 10


# fazer lista com dict de produtos e quantidade

def fill_stock():
    global stock
    global cart
    stock = dict((x, y) for x, y in db.get_products_id_and_quantity())
    cart = dict((x, y) for x, y in db.get_products_id())
    print(stock)


def show_product_on_cart(label, qtd):
    global cart_label
    global cart_qtd
    global cart_remove_button
    global cart_cont

    product_label = Label(
        text=label,  # nome
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .8, 'top': .65 - cart_cont / 100}

    )

    qtd_product = Label(
        text=str(qtd),  # quantidade
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .9, 'top': .65 - cart_cont / 100}
    )

    remove_product = Button(
        text='-',
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(.022, .03),
        pos_hint={'x': .92, 'top': .664 - cart_cont / 100}
    )

    remove_product.bind(on_release=remove_product_from_cart)

    cart_cont += 5
    cart_label.append(product_label)
    layout.add_widget(product_label)

    cart_qtd.append(qtd_product)
    layout.add_widget(qtd_product)

    cart_remove_button.append(remove_product)
    layout.add_widget(remove_product)


def show_product():
    global products_label
    global products_qtd
    global products_add_button
    products_in_db = db.find_all_products()

    cont = 10
    for product in products_in_db:
        product_label = Label(
            text=product[1] + " R$" + str(product[5]),  # nome
            font_size=24,
            color=(0, 0, 0, 1),
            size_hint=(0, 0),
            pos_hint={'x': .15, 'top': .65 - cont/100}

        )

        qtd_product = Label(
            text=str(stock.get(product[0])),  # quantidade
            font_size=24,
            color=(0, 0, 0, 1),
            size_hint=(0, 0),
            pos_hint={'x': .25, 'top': .65 - cont/100}
        )

        add_product = Button(
            text='+',
            font_size=24,
            color=(0, 0, 0, 1),
            size_hint=(.022, .03),
            pos_hint={'x': .27, 'top': .664 - cont/100}
        )

        add_product.bind(on_release=add_product_to_cart)

        cont += 5
        products_label.append(product_label)
        layout.add_widget(product_label)

        products_qtd.append(qtd_product)
        layout.add_widget(qtd_product)

        products_add_button.append(add_product)
        layout.add_widget(add_product)


def remove_product_from_cart(instance):
    global stock
    global cart
    global total_value

    for i in range(len(cart_remove_button)):
        product_position = i+1
        if instance == cart_remove_button[i]:
            if cart.get(product_position) > 0:
                stock[product_position] += 1
                cart[product_position] -= 1
                total_cost = total_value.text[9:]
                total_value.text = 'Total: R$ {:.2f}'\
                    .format(float(total_cost) - float(db.get_product_value(product_position)[0]))
                products_qtd[i].text = str(stock[product_position])
                cart_qtd[i].text = str(cart[product_position])


def add_product_to_cart(instance):
    global stock
    global cart
    global total_value

    for i in range(len(products_add_button)):
        product_position = i+1
        if instance == products_add_button[i]:
            if stock.get(product_position) > 0:
                stock[product_position] -= 1
                cart[product_position] += 1
                total_cost = total_value.text[9:]
                total_value.text = 'Total: R$ {:.2f}'\
                    .format(float(total_cost) + float(db.get_product_value(product_position)[0]))
                products_qtd[i].text = str(stock[product_position])
                if len(cart_label) > i and cart_label[i] is not None:
                    cart_qtd[i].text = str(cart[product_position])
                else:
                    show_product_on_cart(products_label[i].text, cart[product_position])


def build_product_cart_screen(main_layout, user):
    global layout
    global total_value
    global client
    layout = main_layout
    client = user

    store_name_label = Label(
        text='24/7 Store',
        font_size=96,
        bold=True,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .15, 'top': .92}
    )

    stock_label = Label(
        text='Estoque',
        font_size=24,
        bold=True,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .1, 'top': .6}
    )

    cart_label = Label(
        text='Carrinho',
        font_size=24,
        bold=True,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .75, 'top': .6}
    )

    user_label = Label(
        text='Bem vindo, {0}.'.format(user.nome),
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'right': 0.9, 'top': .95}
    )

    total_value = Label(
        text='Total: R$ {:.2f}'.format(0.00),
        font_size=24,
        color=(0, 0, 0, 1),
        size_hint=(0, 0),
        pos_hint={'x': .785, 'top': 0.18}
    )

    finish_sale_button = Button(
        text='Finalizar Compra',
        font_size=32,
        bold=True,
        size_hint=(.2, .10),
        pos_hint={'x': .75, 'top': 0.15},
        background_normal='',
        background_color=(0.66, 0.33, 0.33, 1)
    )

    finish_sale_button.bind(on_release=finish_sale)

    layout.add_widget(store_name_label)
    layout.add_widget(stock_label)
    layout.add_widget(cart_label)
    layout.add_widget(user_label)
    layout.add_widget(total_value)
    layout.add_widget(finish_sale_button)

    fill_stock()
    show_product()


def finish_sale(instance):
    global cart
    global client
    Venda.carrinho = cart
    Venda.valor_total = total_value.text[9:]
    venda = Venda()
    venda.data = datetime.fromtimestamp(time.time())
    venda.id_cliente = client.id
    venda.valor = Venda.valor_total

    if float(client.saldo) >= float(venda.valor):
        db.make_sale(venda)
        client.saldo -= float(venda.valor)
        db.update_client_balance(client)
        db.sell_sale_products(venda)

        Venda.valor_total = 0.0
        cart = Venda.carrinho = dict((x, y) for x, y in db.get_products_id())

        layout.clear_widgets()
        return screens.home_screen.build_home_screen(layout)
