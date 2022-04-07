from kivy.app import App
from kivy.lang import Builder

class TemperatureConvertor(App):

    def build(self):
        self.title = "Temperature Converter"
        self.root = Builder.load_file('temperature_convert.kv')
        return self.root

    def celsius(self):
        fahrenheit = self.check_valiable() * 9.0 / 5 + 32
        self.root.ids.output_num.text = "{:.2f} F".format(fahrenheit)
        return self.root.ids.output_num.text

    def fahrenheit(self):
        celsius = 5 / 9 * (self.check_valiable() - 32)
        self.root.ids.output_num.text = "{:.2f}C".format(celsius)
        return self.root.ids.output_num.text

    def quit (self):
        self.root.ids.output_num.text = "quit"
        return quit()

    def check_valiable (self):
        try:
            value = int(self.root.ids.input_num.text)
            return value
        except ValueError:
            return 0


TemperatureConvertor().run()