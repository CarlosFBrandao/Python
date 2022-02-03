from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Tarefas(Screen):
    def __init__(self,tarefas = [],**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard = self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
        return True
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def addWidget(self):
        text = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text = text))
        self.ids.texto.text = ''

class Tarefa(BoxLayout):
    def __init__(self, text = '', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Test(App):
    def build(self):
        return Gerenciador()

Test().run()