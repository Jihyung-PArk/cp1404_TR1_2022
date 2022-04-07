from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class Score(App):

    def build(self):
        Window.size = (300, 100)
        self.title = "Score"
        self.root = Builder.load_file('score.kv')
        return self.root

    def score(self):
        if 100 >= self.check_valiable() >= 85:
            self.root.ids.score_output.text = "High Distinction"
            return self.root.ids.score_output.text

        elif 84 >= self.check_valiable() >= 75:
            self.root.ids.score_output.text = "Distinction"
            return self.root.ids.score_output.text

        elif 74 >= self.check_valiable() >= 65:
            self.root.ids.score_output.text = "Credit"
            return self.root.ids.score_output.text

        elif 64 >= self.check_valiable() >= 50:
            self.root.ids.score_output.text = "Pass"
            return self.root.ids.score_output.text

        else:
            self.root.ids.score_output.text = "False"
            return self.root.ids.score_output.text


    def check_valiable(self):
        try:
            score_input = int(self.root.ids.score_input.text)
            return score_input
        except ValueError:
            return ""
Score().run()