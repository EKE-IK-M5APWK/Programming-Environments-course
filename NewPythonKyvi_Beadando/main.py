from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from cryptography.fernet import Fernet


class MainWindow(Screen):
    pass


class ReportWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("ui.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()