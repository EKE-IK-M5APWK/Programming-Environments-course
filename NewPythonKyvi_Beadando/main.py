import json
import os
import tkinter as tk
from tkinter import simpledialog
from kivy.app import App
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, ListProperty, BooleanProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from pysondb import db

import subprocess


def getN(value):
    a = db.getDb("scp_database.json")
    return a.get(value)


def getAll():
    a = db.getDb("scp_database.json")
    return a.getAll()


def updateById(username, what_to_update):
    a = db.getDb("scp_database.json")
    a.updateById(username, what_to_update)


class LoginWindow(Screen):
    title = "SCP Login"

    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        value = getAll()
        access = False
        print(value)
        for item in value:
            if item["username"] == self.username.text and item["password"] == self.password.text:
                if item["level"] >= 4:
                    access = True
                    sm.current = "report"
                else:
                    root = tk.Tk()
                    root.withdraw()
                    user_inp = simpledialog.askstring(title="O5 Clearance",
                                                      prompt="Clearance level elevation. Give me your key:")
                    if user_inp == "O5":
                        updateById(item["id"], {"level": 4})
                        print(item["id"], "-> Level:4")
                        access = True
                        sm.current = "report"

        if not access:
            pop = Popup(title='Incorrect entry',
                        content=Label(
                            text='Access Denied! Check your input and you clearance level and try again.'),
                        size_hint=(None, None), size=(500, 500))
            pop.open()

    @staticmethod
    def registration():
        sm.current = "reg"


class RegWindow(Screen):
    title = 'Registration'
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def clear(self):
        self.username.text = ""
        self.password.text = ""

    @staticmethod
    def back():
        sm.current = "login"

    def submit(self):
        if len(self.username.text) > 0 and len(self.password.text) > 0:
            var = getAll()
            available = True
            for item in var:
                if item["username"] == self.username.text:
                    pop = Popup(title='Error',
                                content=Label(text="Username Already Exits!"),
                                size_hint=(None, None), size=(400, 400))
                    pop.open()
                    available = False
            if available:
                data = {'username': self.username.text, 'password': self.password.text, 'level': 1}
                a = db.getDb("scp_database.json")
                a.add(data)
                sm.current = "login"
                pop = Popup(title='Registration successfully',
                            content=Label(text="Registration successfully!"),
                            size_hint=(None, None), size=(400, 400))
                pop.open()
                available = False
        else:
            pop = Popup(title='Error',
                        content=Label(text="Check if all field is filled!"),
                        size_hint=(None, None), size=(400, 400))
            pop.open()


class ReportWindow(Screen):
    title = "SCP Report"
    scp = ObjectProperty(None)

    @staticmethod
    def data():
        sm.current = "database"

    def search(self):
        if len(self.scp.text) > 0:
            self.scp.text = str(self.scp.text).zfill(3)
            print(self.scp.text)
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
    title = "SCP Login"
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
