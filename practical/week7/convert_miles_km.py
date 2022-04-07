from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


MILES_TO_KM = 1.60934

class ConvertMilesKm (App):

    output_num = StringProperty()

    def build (self):
        self.title = "Convert Miles Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_num = "Result"
        return self.root


    def calculate(self):
        km = self.check_valiable()
        miles = MILES_TO_KM * km
        self.root.ids.output_num.text = str(miles)

    def check_valiable(self):
        try:
            km = float(self.root.ids.input_num.text)
            return km
        except ValueError:
            return 0.0

    def handle_increment (self, num):
        km = self.check_valiable() + num
        self.root.ids.input_num.text = str(km)
        self.calculate()

    def handle_update(self):
        self.calculate()
        self.output_num = self.root.ids.output_num.text

ConvertMilesKm().run()