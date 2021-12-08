
## Overview
The purpose of this document is to outline the requirements needed to implement certain features into our application. By organizing our requirements here we can assure they are all met so the application can run smoothly.

## Functional Requirements

1. Draft Feature
  	1. R1: The draft feature shall allow the user to choose from a list of the top 250 current ranked NFL players.
  	2. R2: The draft feature shall display each players name and position.
  	3. R3: The draft feature shall contain a timer and current number of players drafted to the users team.
  	4. R4:The draft feature shall allow the user to skip the draft and be taken to the main menu screen at any point in the drafting process.
  	5. R5: The draft feature shall end when the user has a team of 9 players.
2. Data storage
  	1. R6: The data of all players names shall be stored in lists.
  	2. R7: The data of the users drafted team shall be stored in a list seperate from the list of all players.
  	3. R8: The data of the users drafter team shall be updated when selected to allow the player to exit the draft with their selected team at anytime.
  	4. R9: The data of each players fantasy points shall be stored in a list seperate from the list of all players in the form of integers.
  	5. R10: The data that will be displayed on the draft screen shall be stored in a list seperate from the list of all players.
3. Team Name Feature:
  	1. R11: The user's teamname shall be stored in a string variable
  	2. R12: The user's teamname shall be updated when the save button is pressed and is changed to the text in the text input.
  	3. R13: The user's teamname shall be set to "No Teamname Entered" if the user does not enter a teamname.
  	4. R14: The user's teamname shall be displayed on the toolbar on the main menu screen.
  	5. R15: The user's teamname shall not be changed once the user has entered the draft screen.
	
## Non-Functional Requirements

1. Draft Feature
  	1. R1: The draft feature shall only allow the user 30 seconds to make a pick before a player is randomly drafted to their team.
  	2. R2: The draft feature shall only allow the user to chose a given player one time.
  	3. R3: The draft feature shall consist of 9 rounds before the team is locked in.
  	4. R4: The draft feature shall contain a counter that starts at 0 and increased by one eachtime a player is drafted.
  	5. R5: The draft feature shall not allow a user to draft a team smaller than 0 players.
2. Data Pulling 
    	1. R6: The program shall store one total fantasy points per one player name.
    	2. R7: The program shall store 250 players.
    	3. R8: The program shall calculate the total team points by adding all total points of the players drafted.
    	4. R9: The program shall increase the total player index by one each time a player is pulled into a list.
    	5. R10: The program shall store a players information in the same index across all stats.
3. Display
  	1. R11: The teamname text input shall allow up to 20 characters.
  	2. R12: The draft timer shall increase by one every 1 second.
  	3. R13: The screen size shall be set to 400x600.
  	4. R14: The Kivy list shall increase by one every time a player is drafted.
  	5. R15: The Kivy list for user's team shall not be greater than 9.  
