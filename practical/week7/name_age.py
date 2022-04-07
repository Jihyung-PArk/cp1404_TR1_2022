from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button

class NameAge(App):

    name_text = StringProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list = self.load_file()
        
    def build(self):
        """Build the Kivy GUI."""
        self.title = "Name Age"
        self.root = Builder.load_file('name_age.kv')
        self.create_widgets()
        return self.root
    
    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.list:
            temp_button = Button(text=name)
            temp_button.bind(on_press=self.press_entry)
            self.root.ids.name_button.add_widget(temp_button)

    def press_entry(self, instance):

        name = instance.text
        self.name_text = str(self.list[name])


    def load_file(self):
        list_person = {}
        with open("list.txt") as file:
            for line in file:
                (key, value) = line.split(",")

                list_person[key] = int(value)
        return list_person

NameAge().run()