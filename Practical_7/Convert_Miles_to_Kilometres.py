from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class Convert_Miles_to_Kilometres(App):
    """Convert is a kivy app used to convert miles to kilometres"""
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('Convert_Miles_to_Kilometres.kv')
        return self.root
    def calculate_conversion(self, value):
        """This converts miles to kilometres"""
        value = float(value)
        result = value * 1.609344
        self.root.ids.output_label.text = str(result)


Convert_Miles_to_Kilometres().run()