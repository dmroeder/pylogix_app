import kivy
import pylogix
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainUI(GridLayout):

    def __init__(self, **kwargs):
        super(MainUI, self).__init__(**kwargs)
        self.cols = 1

        self.comm = pylogix.PLC()

        self.layout = GridLayout(cols=2, row_force_default=True,
                            row_default_height=60)

        # Load fields for reading
        self.layout.add_widget(Label(text="IP Address"))
        self.ip_address = TextInput(multiline=False, text="192.168.1.10")
        self.layout.add_widget(self.ip_address)
        self.layout.add_widget(Label(text="Tag Name"))
        self.tag_name = TextInput(multiline=False, text="MyDINT")
        self.layout.add_widget(self.tag_name)

        # Load fields for writing
        self.layout.add_widget(Label(text="Write Value"))
        self.write_value = TextInput(multiline=False, text="0")
        self.layout.add_widget(self.write_value)

        # Add Read button
        self.read_button = Button(text="Press to Read")
        self.read_button.bind(on_press=self.read)
        self.layout.add_widget(self.read_button)

        # Add Write button
        self.write_button = Button(text="Press to Write")
        self.write_button.bind(on_press=self.write)
        self.layout.add_widget(self.write_button)

        self.add_widget(self.layout)

        # result label
        self.result = Label(text="Result:")
        self.add_widget(self.result)

    def read(self, instance):
        """
        Read a tag
        """
        ip = self.ip_address.text
        self.comm.IPAddress = ip
        tag = self.tag_name.text
        ret = self.comm.Read(tag)

        #print("Tag:{} Val:{}".format(ret.TagName, ret.Value))
        self.result.text = "Tag:{} - Value:{}".format(ret.TagName, ret.Value)

    def write(self, instance):
        """
        Write a value to a tag
        """
        tag = self.tag_name.text
        val = self.write_value.text

        ret = self.comm.Write(tag, val)
        self.result.text = "Wrote {} to {}, result={}".format(ret.Value, ret.TagName, ret.Status)

class MyApp(App):
    def build(self):
        return MainUI()

if __name__ == "__main__":
    MyApp().run()