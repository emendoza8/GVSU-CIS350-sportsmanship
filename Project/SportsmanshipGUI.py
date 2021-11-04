from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatIconButton,MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.textfield import MDTextFieldRect,MDTextField
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.tab import MDTabs,MDTabsBase
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import MDList, ThreeLineListItem,OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock 
from kivy.core.window import Window

#Window.size = (500,900)

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

        MDFloatLayout:
            md_bg_color: 0,0,0,.5
            MDTextFieldRect:
                id: teamname
                hint_text: 'Enter Team Name:'
                mode: 'rectangle'
                max_text_length: 20
                pos_hint: {'center_x': .45, 'center_y': .6}
                size_hint:.5,.1
                multiline: False

            MDRaisedButton:
                text: 'Save'
                halign: 'center'
                pos_hint: {'center_x': .8, 'center_y': .595}
                on_press:
                    teamName = teamname.text           

            MDRaisedButton:
                text: 'Ready to Draft'
                halign: 'center'
                pos_hint: {'center_x': .5, 'center_y': .1}
                on_press:
                    root.manager.current = 'draftScreen'

<DraftScreen>:
    name: 'draftScreen'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title:'Draft'
            halign: 'center'
            pos_hint: {'center_x': .5, 'center_y': 1}
        MDList:
            id: 'players'
        MDFloatLayout:
            MDRaisedButton:
                text: 'Next'
                halign: 'center'
                pos_hint: {'center_x': .5, 'center_y': .5}
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
            on_tab_switch: app.on_tab_switch(*args)
           

<Tabs>:
    MDLabel:
        halign: 'center'
        Tab:
            id: draft
            text: 'Draft'
        Tab:
            id: myteam
            text: 'My Team'
            

"""
#creates the loginscreen screen
class LoginScreen(Screen):
    pass
#creates the draftscreen screen
class DraftScreen(Screen):
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
        screen = Screen()

        self.screen_build = Builder.load_string(screen_helper)
        screen.add_widget(self.screen_build)

        return screen
    #adds all the tabs as widgets to the main screen
    def on_start(self):
        self.screen_build.get_screen('mainMenu').ids.tabs.add_widget(Tab(text = 'Draft'))
        self.screen_build.get_screen('mainMenu').ids.tabs.add_widget(Tab(text = 'My Team'))
        self.screen_build.get_screen('mainMenu').ids.tabs.add_widget(Tab(text = 'Opp Team'))
    #determines what occurs when a tab is switched on the main screen (currently nothing )
    def on_tab_switch(self,instance_tabs,instance_tab,instance_tab_label,tab_text):
        currentTab = instance_tab.text
        #if(currentTab == 'My Team'):
            #self.root.current = 'loginScreen'

#runs the app if it is called as main
if __name__ == '__main__':
    MainApp().run()
