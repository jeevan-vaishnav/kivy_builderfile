from turtle import color
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('my.kv')
'''Builder.load_string("""
<MyGridLayout>
    name:name
    pizza:pizza
    color:color

    GridLayout:
        cols:1
        size: root.width, root.height
        GridLayout:
            cols:2

            Label:
                text:'Name :'
            TextInput:
                id:name
                multiline:False

            Label:
                text:'Favorite Pizza :'
            TextInput:
                id:pizza
                multiline:False

            Label:
                id:color
                text:'Color :'
            TextInput:
                multiline:False
        Button:
            text:'Submit'
            font_size:32
            on_press:root.press()

""")'''


class MyGridLayout(Widget):

    name = ObjectProperty(None)
    color = ObjectProperty(None)
    pizza = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f"Hello {name}, you like {pizza} pizza and color is {color}")

        # after clicking the submit button cleearing the text box
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class AwesomeApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    AwesomeApp().run()
