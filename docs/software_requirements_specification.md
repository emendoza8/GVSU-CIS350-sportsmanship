
## Overview
The purpose of this document is to outline the requirements needed to implement certain features into our application. By organizing our requirements here we can assure they are all met so the application can run smoothly.

## Functional Requirements

1. Draft Feature
	1. R1: The draft feature shall randomize which user chooses first and then allow the other user to choose. This order will be switched each round.
	2. R2: The draft feature shall include a search bar to search for players or positions.
	3. R3: The draft feature shall include a list of all players and defenses including their name, position, and team name.
	
2. Roster Setting Interface
	1. R4: The roster setting interface shall get the kickoff time of the first NFL game each week.
	2. R5: The roster setting interface shall prompt the user to submit their roster if any player changes have been made. 
	3. R6: The roster setting interface shall lock all roster movement at kickoff of the first NFL game of each week. 

3. Roster Information
	1. R7: The roster shall only allow 9 players in the starting lineup and 7 players on the bench. 
	2. R8: The roster shall only allow 1 QB, 2 RB, 2 WR, 1 TE, 1 FLX, 1 K, and 1 D/ST in a starting lineup. 
	3. R9: The system shall allow any position player to be rostered at the FLX position, except for quarterback.  
	
## Non-Functional Requirements

1. Draft Feature
	1. R1: The draft feature shall only allow the user 30 seconds to make their pick before a player is randomly drafted to their team.
	2. R2: The draft feature shall only allow each player to choose one player per round.
	3. R3: The draft feature shall consist of 16 rounds before the teams are locked in.
	
2. Roster Setting Interface
	1. R4: The roster setting interface shall respond to clicking the "submit roster" button within two seconds.
	2. R5: The roster setting interface shall be able to respond to touch for selecting, dragging, and dropping players. 
	3. R6: The roster setting interface shall display to the user that their roster must be set at least five minutes prior to the first game of each week. 
3. Scoring
	1. R7: For QB, the system shall give 6 points per TD thrown and 0.04 points per passing yard.
	2. R8: For RB, the system shall give 6 points per rushing TD, 0.1 per rushing yard, and 1 point per reception. 
	3. R9: For WR/TE, the system shall give 6 points per TD reception, 0.1 per receiving yard, and 1 point per reception. 
	4. R10: For Kickers, the system shall give 1 point per PAT made, 3 points per 0-39 yard FG, 4 points per 40-49 yard FG, 5 points per 50-59 yard FG, and 6 points per 60+ yard FG. 
	5. R11: For D/ST, the system shall give 6 points per defensive/special teams TD, 2 points per interception, fumble, safety, or blocked punt/FG, and 1 point per sack. 
 
