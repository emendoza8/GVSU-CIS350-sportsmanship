from kivymd.app import MDApp
from kivy.uix.widget import Widget
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
Window.size = (400,600)

#screen_helper create all of the different screens including Login,Draft,and the Main Menu and uses the build in KivyMd tool to add textboxes,labels,etc

playerList = open("nflPlayers.txt","r")

arr = []
userTeam = []

for i in playerList:
    arr.append(i)

def getplayer(i):
    return arr[i]

#creates the loginscreen screen
class LoginScreen(Screen):
    pass
#creates the draftscreen screen
class DraftScreen(Screen):
    def on_enter(self):
        Clock.schedule_interval(self.update_label,1)
        def select(player,instance):
            userTeam.append(player)
            instance.text = "Drafted ({})".format(player)
            self.ids.counter.text = str(int(30))
            if(len(userTeam) == 16):
                self.parent.current = 'mainMenu'
        for i in range(0,len(arr)):
            self.ids.container.add_widget(OneLineAvatarIconListItem(text= str(getplayer(i)), on_press = lambda x: select(x.text,x)))
    def update_label(self, *args):
        if(self.ids.counter.text == str(int(0))):
            self.ids.counter.text = str(int(30))
        else:
            self.ids.counter.text = str(int(self.ids.counter.text) - 1)
    pass
#creates the main menu screen
class MainMenu(Screen):
    def on_enter(self):
        for i in range(0,len(userTeam)):
            self.ids.container2.add_widget(OneLineAvatarIconListItem(text = userTeam[i]))
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

        self.screen_build = Builder.load_file("Main.kv")
        screen.add_widget(self.screen_build)

        return screen

#runs the app if it is called as main
if __name__ == '__main__':
    MainApp().run()
