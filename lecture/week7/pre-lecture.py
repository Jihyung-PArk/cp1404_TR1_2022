from kivy.app import App
from kivy.lang import Builder

class HelloKv(App):
    def build(self):
        self.title = "Hello world!"
        self.root = Builder.load_file('widget.kv')
        return self.root
HelloKv().run()

