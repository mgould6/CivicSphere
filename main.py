import pyrebase
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

# Firebase configuration
firebase_config = {
    "apiKey": "AIzaSyAk5UlH4Z6wQprmOgJcGZcBMMLAkElLnA8",
    "authDomain": "civicsphere-677b3.firebaseapp.com",
    "databaseURL": "https://civicsphere-677b3-default-rtdb.firebaseio.com/",
    "projectId": "civicsphere-677b3",
    "storageBucket": "civicsphere-677b3.appspot.com",
    "messagingSenderId": "861875090749",
    "appId": "1:861875090749:web:0d051d9da9b6845145c154"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

class CivicSphereLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text="Welcome to CivicSphere!"))

        self.email_input = TextInput(hint_text="Enter email", multiline=False)
        self.add_widget(self.email_input)

        self.password_input = TextInput(hint_text="Enter password", password=True, multiline=False)
        self.add_widget(self.password_input)

        self.sign_up_button = Button(text="Sign Up")
        self.sign_up_button.bind(on_press=self.sign_up)
        self.add_widget(self.sign_up_button)

        self.sign_in_button = Button(text="Sign In")
        self.sign_in_button.bind(on_press=self.sign_in)
        self.add_widget(self.sign_in_button)

def sign_up(self, instance):
    email = self.email_input.text
    password = self.password_input.text
    try:
        user = auth.create_user_with_email_and_password(email, password)
        self.show_popup("Success", "User created successfully!")
    except Exception as e:
        error_message = str(e)
        if "EMAIL_EXISTS" in error_message:
            self.show_popup("Error", "The email address is already in use.")
        elif "WEAK_PASSWORD" in error_message:
            self.show_popup("Error", "The password is too weak.")
        else:
            self.show_popup("Error", error_message)


    def sign_in(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            self.show_popup("Success", "Signed in successfully!")
        except Exception as e:
            self.show_popup("Error", str(e))


    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical')
        popup_label = Label(text=message)
        popup_button = Button(text="Close", size_hint_y=None, height=50)
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_button)
        popup = Popup(title=title, content=popup_layout, size_hint=(0.75, 0.5))
        popup_button.bind(on_press=popup.dismiss)
        popup.open()

class CivicSphereApp(App):
    def build(self):
        return CivicSphereLayout()

if __name__ == "__main__":
    CivicSphereApp().run()
