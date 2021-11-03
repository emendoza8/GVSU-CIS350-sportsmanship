import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import NoTransition, ScreenManager, Screen, TransitionBase
from kivy.core.clipboard import Clipboard
import time
from kivy.lang import Builder



Builder.load_string("""
<LoginScreen>:
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_x':.5,'center_y':.5}
        size_hint:.5,1

        Label:
            text: "SportsmanShip Fantasy Football"
        Label:
            size_hint:.1,.1
            pos_hint: {'center_x':.5,'center_y':.5}
            text: "Enter Team Name Below"
        BoxLayout:
            orientation: 'horizontal'
            TextInput:
                id: team_name
                size_hint:.5,.3
                pos_hint: {'center_x':.5,'center_y':.5}
                multiline: False
            Button:
                size_hint:.3,.3
                text: "Save"
                pos_hint: {'center_x':.5,'center_y':.5}
                on_press:
                    
                    
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: "Ready for Draft"
            CheckBox:
                on_active:
                    root.manager.current = "draft_screen"
<DraftScreen>:
    BoxLayout:
        Button:
            text: "Go to Back"
            on_press:
                root.manager.current = "login_screen"

<TimeDelay>
    BoxLayout:
        Label:
            text: "Draft is Beginning..."
       

""")



screen_manager = ScreenManager(transition=NoTransition())

class LoginScreen(Screen):
    pass


class DraftScreen(Screen):
    pass

#class TimeDelay(Screen):
    #time.sleep(5)
    #screen_manager.switch_to(DraftScreen())

screen_manager.add_widget(LoginScreen(name="login_screen"))
#screen_manager.add_widget(TimeDelay(name="delay"))
screen_manager.add_widget(DraftScreen(name="draft_screen"))

class program(App):
    def build(self):
        

        return screen_manager

if __name__ == '__main__':
    program().run()
