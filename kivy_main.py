from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from cliente import Cliente
from database import *


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.login_button = Button(text='Fazer Login', font_size=14)
        self.login_button.bind(on_press=self.fazer_login)
        self.add_widget(self.login_button)

    def fazer_login(self, instance):
        # fazer login
        print(Cliente.autentica_cliente(bd, self.username.text, self.password.text))


class HomeScreen(GridLayout):

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='24/7 Store', font_size=25))
        self.add_widget(Label(text='Disponível a qualquer momento!', font_size=12))
        self.add_widget(Label(text='password'))


class MyApp(App):

    def build(self):
        return HomeScreen()
        # return LoginScreen()


if __name__ == '__main__':
    global bd
    bd = Database()
    bd.create_database()
    MyApp().run()
