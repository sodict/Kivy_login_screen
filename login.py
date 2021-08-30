from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class LoginUI(BoxLayout):
    pass


class LoginApp(App):
    def build(self):
        return LoginUI()


if __name__ == '__main__':
    login = LoginApp()
    Window.size=(397,697)
    login.run()