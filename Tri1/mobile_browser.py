import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class SimpleBrowser(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.url_input = TextInput(text='https://', size_hint_y=None, height=50)
        layout.add_widget(self.url_input)
        
        self.go_button = Button(text='GO', size_hint_y=None, height=50)
        self.go_button.bind(on_press=self.load_page)
        layout.add_widget(self.go_button)
        
        self.content_label = Label(text='Content will appear here')
        layout.add_widget(self.content_label)
        
        return layout
    
    def load_page(self, instance):
        try:
            response = requests.get(self.url_input.text)
            self.content_label.text = response.text[:500] + "..."  # Show first 500 chars
        except Exception as e:
            self.content_label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    SimpleBrowser().run()
