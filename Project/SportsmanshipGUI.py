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
import pandas as pd

#Uncomment this to see app in a phone size window
Window.size = (400,600)

#df is a variable that reads in an excel file using pandas (currently reads in top 200 NFL players by fantasy points)
df = pd.read_excel('Test.xlsx', 'Sheet1')

#playerNames and playerPositions are both list that read in different colomns from the excel file
playerNames = df['Player'].values.tolist()
playerPositions = df['FantPos'].values.tolist()

#List that is set to empty and will contain the names displayed of each player and positon
draftDisplayList = []

#loops through the player list and concatinates the name and position together for display purposes
for x in range(0, len(playerPositions)):
    draftDisplayList.append(str(playerNames[x]) + ' (' + str(playerPositions[x]) + ')')

#Holds the users teamname (currently very buggy)
teamName = 'No Teamname Entered'

#List that holds the users team after draft is complete
userTeam = []

#Function that takes in an int and returns the player at that index
def getplayer(i):
    return draftDisplayList[i]

#creates the loginscreen screen
class LoginScreen(Screen):
    pass
#creates the draftscreen screen
class DraftScreen(Screen):
    #When screen is entered this function will start the clock and add widgets to a KivyMD list that displays the players name and position and has a on_press property that calls the select function for the draft
    def on_enter(self):
        Clock.schedule_interval(self.update_label,1)
        #this method takes in 2 parameters player is a string with the players name the other is the instance id of the KivyMD list object which allows you to change the text or even delete that object
        #Method currently appends the selected player to the userTeam list then changes the display name to show that player was drafted then resets the clock and checks if the player has a full team and if so the screen is switched to the mainMenu and the draft feature is no longer accessable 
        def select(player,instance):
            userTeam.append(player)
            instance.text = "Drafted ({})".format(player)
            self.ids.counter.text = str(int(30))
            self.ids.currentTeamSize.text = str(len(userTeam))
            if(len(userTeam) == 16):
                self.parent.current = 'mainMenu'
        for i in range(0,len(draftDisplayList)):
            self.ids.container.add_widget(OneLineAvatarIconListItem(text= str(getplayer(i)), on_press = lambda x: select(x.text,x)))
    #This method can be used to update the timer label so it counts down and resets to 30 when it hits 0
    def update_label(self, *args):
        if(self.ids.counter.text == str(int(0))):
            self.ids.counter.text = str(int(30))
        else:
            self.ids.counter.text = str(int(self.ids.counter.text) - 1)
    pass
#creates the main menu screen
class MainMenu(Screen):
    #When mainmenu screen is entered the list on the myteam tab will be filled with the users drafed players
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
    #builds the app and returns the screen also sets the theme of the app and loads the .kv files
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
