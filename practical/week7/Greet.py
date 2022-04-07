from kivy.app import App
from kivy.lang import Builder

class Greet(App):

    def builder(self):
        self.title = "Greet"
        self.root = builer.load_file('Greet.kv')
        return self.root

    def greet(self):
        self.root.ids.output_name.text = "Hello " + self.root.ids.input_name.text

    def clear(self):
        self.root.ids.output_name = ""
        self.root.ids.input_name = ""



Greet().run()