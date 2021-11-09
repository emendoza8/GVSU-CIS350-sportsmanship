from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatIconButton,MDRaisedButton,MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.textfield import MDTextFieldRect,MDTextField
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.tab import MDTabs,MDTabsBase
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import MDList, ThreeLineListItem,OneLineListItem,OneLineAvatarIconListItem
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock 
from kivy.core.window import Window

#Uncomment this to see app in a phone size window
#Window.size = (400,600)

#screen_helper create all of the different screens including Login,Draft,and the Main Menu and uses the build in KivyMd tool to add textboxes,labels,etc
screen_helper = """
ScreenManager:
    LoginScreen:
    DraftScreen:
    MainMenu:

<LoginScreen>:
    id: loginScreen
    name: 'loginScreen'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'SportsmanShip Fantasy Football'
            halign: 'center'
            pos_hint: {'center_x': .5, 'center_y': 1}
            left_action_items: [['menu']]

        MDBoxLayout:
            orientation: 'horizontal'
            MDTextFieldRect:
                id: teamname
                hint_text: 'Enter Team Name:'
                mode: 'rectangle'
                max_text_length: 20
                size_hint:.5,.15
                multiline: False

            MDFillRoundFlatButton:
                text: 'Save'
                on_press:
                    teamName = teamname.text
        MDFloatLayout:

            MDFillRoundFlatButton:
                text: 'Ready to Draft'
                halign: 'center'
                pos_hint: {'center_x': .5, 'center_y': .1}
                on_release:
                    root.manager.current = 'draftScreen'

<DraftScreen>:
    name: 'draftScreen'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title:'Draft'
            halign: 'center'
            pos_hint: {'center_x': .5, 'center_y': 1}
        MDBoxLayout:
            orientation: 'horizontal'
            MDLabel:
                halign: 'center'
                pos_hint: {'center_x': .5, 'center_y': .5}
                id: counter
                text: '30'
        MDBoxLayout:
            orientation: 'vertical'
            MDTextFieldRound:
                id: playerName
                hint_text: 'Search by player name:'
                mode: 'rectangle'
                halign: 'center'
                pos_hint: {'center_x': .5, 'center_y': .5}
                max_text_length: 20
                size_hint: .8,.2
                multiline: False
            ScrollView:
                MDList:
                    id: container
                    divider: 'Full'

        MDFloatLayout:
            MDFillRoundFlatButton:
                text: 'Skip'
                halign: 'center'
                pos_hint: {'center_x': .8, 'center_y': .5}
                on_press:
                    root.manager.current = 'mainMenu'
    

<MainMenu>:
    name: 'mainMenu'
    MDBoxLayout:    
        orientation: 'vertical'

        MDToolbar:
            title: 'Main Menu'
            halign: 'center'
            pos_hint: {'center_x': .5, 'center_y': 1}
            left_action_items: [['menu']]
        MDTabs:
            id: tabs
            Tab:
                text: 'Home'
                id: homeTab
                MDLabel:
                    text: 'home'
            Tab:
                text: 'MyTeam'
                id: myTeamTab
                MDLabel:
                    text:'team'
            Tab:
                text: 'OppTeam'
                id: oppTeamTab
                MDLabel:
                    text:'oppteam'
           
<Tabs>:
            

"""
#creates the loginscreen screen
class LoginScreen(Screen):
    pass
#creates the draftscreen screen
class DraftScreen(Screen):

    def on_enter(self):
        Clock.schedule_interval(self.update_label,1)
        for i in range(20):
            self.ids.container.add_widget(OneLineAvatarIconListItem(text="player {}".format(i)))
    def update_label(self, *args):
        if(self.ids.counter.text == str(int(0))):
            self.ids.counter.text = str(int(30))
        else:
            self.ids.counter.text = str(int(self.ids.counter.text) - 1)
    pass
#creates the main menu screen
class MainMenu(Screen):
    pass
#creates the tabs for the main menu screen
class Tab(FloatLayout, MDTabsBase):
    pass

#creates a variable for the screen manager and then adds all of the different screens to it as widgets
sm = ScreenManager()
sm.add_widget(LoginScreen(name='loginScreen'))
sm.add_widget(DraftScreen(name='draftScreen'))
sm.add_widget(MainMenu(name='mainMenu'))

#Main class the builds the app and returns the screen that includes the screen manager
class MainApp(MDApp):
    #builds the app and returns the screen
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        screen = Screen()

        self.screen_build = Builder.load_string(screen_helper)
        screen.add_widget(self.screen_build)

        return screen

#runs the app if it is called as main
if __name__ == '__main__':
    MainApp().run()
