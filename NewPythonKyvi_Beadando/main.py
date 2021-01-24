import json
import os
import tkinter as tk
from tkinter import simpledialog
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
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


def update(query, what_to_update):
    a = db.getDb("scp_database.json")
    a.update(query, what_to_update)


def deleteById(username):
    a = db.getDb("scp_database.json")
    a.deleteById(username)


class LoginWindow(Screen):
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

    def registration(self):
        sm.current = "reg"


class RegWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def back(self):
        sm.current = "login"

    def submit(self):
        data = {}
        data['username'] = self.username.text
        data['password'] = self.password.text
        data['level'] = 1
        a = db.getDb("scp_database.json")
        a.add(data)
        sm.current = "login"
        print("Registration successfully")


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

class DataBaseWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("ui.kv")
sm = WindowManager()
screens = [LoginWindow(name="login"), ReportWindow(name="report"), RegWindow(name="reg"), DataBaseWindow(name="database")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
