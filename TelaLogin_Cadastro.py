from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen


class TelaLogin(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [50, 20]
        self.spacing = 10

        Window.clearcolor = (0.7, 0.5, 0.9, 1)
        self.add_widget(Image(source='/Users/aluno.sesipaulista/Documents/TelaLogin_e_Cadastro/img_icone/th-removebg-preview.png'))

        self.add_widget(Label(text='L O G I N', font_size=30, bold=True))

        self.username_input = TextInput(hint_text='Digite o usuário...', multiline=False, size_hint=(None, None),
                                        size=(900, 70))
        self.password_input = TextInput(hint_text='Digite a senha...', password=True, multiline=False,
                                        size_hint=(None, None), size=(900, 70))
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)

        self.buttons_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.login_button = Button(text='Entrar', color=(0, 0, 0.1, 1), size_hint=(None, None), size=(450, 50),
                                   background_color=(100, 100, 100, 100))
        self.login_button.bind(on_press=self.login)
        self.signup_button = Button(text='Cadastre-se', color=(0, 0, 0.1, 1), size_hint=(None, None), size=(450, 50),
                                    background_color=(100, 100, 100, 100))
        self.signup_button.bind(on_press=self.segunda_tela)
        self.buttons_layout.add_widget(self.login_button)
        self.buttons_layout.add_widget(self.signup_button)
        self.add_widget(self.buttons_layout)

    def segunda_tela(self, *args):
        self.parent.parent.current = 'Cadastro'

    def login(self, instance):
        username = self.username_input.text
        senha = self.password_input.text
        print('Nome de Usuário:', username)
        print('Senha:', senha)


class TelaCadastro(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [50, 20]
        self.spacing = 10

        Window.clearcolor = (0.7, 0.5, 0.9, 1)

        self.add_widget(Label(text='C A D A S T R O', font_size=30, bold=True))

        self.nome_input = TextInput(hint_text='Digite o seu nome...', multiline=False, size_hint=(None, None),
                                        size=(900, 70))
        self.email_input = TextInput(hint_text='Digite seu email...', multiline=False,
                                        size_hint=(None, None), size=(900, 70))
        self.celular_input = TextInput(hint_text='Digite seu número de telefone...', multiline=False,
                                        size_hint=(None, None), size=(900, 70))
        self.senha_input = TextInput(hint_text='Digite a senha...', password=True, multiline=False,
                                        size_hint=(None, None), size=(900, 70))
        self.add_widget(self.nome_input)
        self.add_widget(self.email_input)
        self.add_widget(self.celular_input)
        self.add_widget(self.senha_input)

        self.buttons_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.signup_button = Button(text='Cadastrar', color=(0, 0, 0.1, 1), size_hint=(None, None), size=(900, 50),
                                    background_color=(100, 100, 100, 100))
        self.signup_button.bind(on_press=self.primeira_tela)
        self.buttons_layout.add_widget(self.signup_button)
        self.add_widget(self.buttons_layout)

    def primeira_tela(self, *args):
        self.parent.parent.current = 'Login'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        tela_login = TelaLogin()
        tela_cadastro = TelaCadastro()

        screen_login = Screen(name='Login')
        screen_cadastro = Screen(name='Cadastro')

        screen_login.add_widget(tela_login)
        screen_cadastro.add_widget(tela_cadastro)

        sm.add_widget(screen_login)
        sm.add_widget(screen_cadastro)

        return sm


if __name__ == '__main__':
    MyApp().run()