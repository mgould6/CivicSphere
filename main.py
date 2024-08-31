from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class CivicSphereLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="Welcome to CivicSphere!"))

class CivicSphereApp(App):
    def build(self):
        return CivicSphereLayout()

if __name__ == "__main__":
    CivicSphereApp().run()
