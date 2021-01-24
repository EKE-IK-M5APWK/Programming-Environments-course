import os

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from pysondb import db
import subprocess


def getN(value):
    a = db.getDb("scp_database")
    return a.get(value)


def getAll():
    a = db.getDb("scp_database")
    return a.getAll()


def updateById(username, what_to_update):
    a = db.getDb("scp_database")
    a.updateById(username, what_to_update)


def update(query, what_to_update):
    a = db.getDb("scp_database")
    a.update(query, what_to_update)


def add(value):
    a = db.getDb("scp_database")
    a.add(value)


def deleteById(username):
    a = db.getDb("scp_database")
    a.deleteById(username)


class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        value = getAll()
        sm.current = "report"
        # for item in value:
        #     if item["id"] == self.username.text and item["password"] == self.password.text and item["level"] >= 4:
        #         sm.current = "report"
        #     else:
        #         pop = Popup(title='Incorrect entry',
        #                     content=Label(
        #                         text='Access Denied! Check your input and you clearance level and try again.'),
        #                     size_hint=(None, None), size=(500, 500))
        #         pop.open()


    def registration(self):
        sm.current = "reg"





class RegWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    def back(self):
        sm.current = "login"

    def submit(self):
        pass


class ReportWindow(Screen):
    scp = ObjectProperty(None)

    def search(self):
        if len(self.scp.text) > 0:
            result = subprocess.run(['marvin', self.scp.text], stdout=subprocess.PIPE)
            if result.stdout.decode('utf-8') != "":
                pop = Popup(title='Unknown SCP Found',
                            content=Label(text=result.stdout.decode('utf-8')),
                            size_hint=(None, None), size=(400, 400))
                pop.open()
        else:
            os.system("marvin -r")


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("ui.kv")
sm = WindowManager()
screens = [LoginWindow(name="login"), ReportWindow(name="report"), RegWindow(name="reg")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
