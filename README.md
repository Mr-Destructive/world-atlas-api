### An API for World Atlas - the geographical game.

You can check out and play the [World Atlas game](https://mr-destructive.github.io/WorldAtlas). 

Currently it is implemented in without using this API, there are tons of Js  hard coded arrays for that. That would be easy to exploit the game in a real-world scenario.

Soon, this API will be integrated into the app as well.


## API Endpoints 

- **`'/<place>'`** -> for validating the place. 

	- Returns `true` if the place exists in the database.
	- Else returns `false` if it doesn't.
	
	![](https://i.ibb.co/qgM6Tt7/image.png)
	
	![](https://i.ibb.co/DGbVNcd/image.png)
	

- **`'/get/<letter>'`** -> for obtaining an random place with given letter.

	- Returns an place, beginning with the alphabet `letter`
	
	![](https://i.ibb.co/93KPT46/image.png)
	
	![](https://i.ibb.co/QrjQyvt/image.png)

- **`'/list/<letter>'`** -> Obtains a list of all places with given letter.

	- Returns a list of places, beginning with the alphabet `letter`
	
	![](https://i.ibb.co/JdL2hxs/image.png)
	

- **`'/create/<place>'`** -> Enters the place into database.

	- Posts the entered place into the database.  
	
	![](https://i.ibb.co/yVDFxzx/image.png)
