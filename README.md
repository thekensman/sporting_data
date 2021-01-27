# sporting_data

You are being asked to create an API for a startup specializing in a new and exciting game: BallSport! In BallSport each player can be assigned one of five positions: Catcher, Pitcher, Runner, Jumper, and Hitter. 

The startup has asked you to integrate with two data providers they have contracted with: SportTastic and SuperPlayer. Each of these providers contains vital information about the players in the top six teams in the league. 

You are being asked to aggregate this data in an API and return it via three endpoints:
1. List all Players: this should return all the data for every player in a consistent format without duplicating any data. Bonus points if you implement sorting and pagination.
2. Single Player Bio Information: this should return the id, first name, last name, team, position, height, weight, jersey, and start year of a given player when passed the player id in the URL.
3. Single Player Stats: this should return the id, catch total, hit total, pitch total, run total, jump total, and current year when passed the player id in the url.

We will be looking for your use of models via a library like pydantic or something similar:

https://pydantic-docs.helpmanual.io/usage/models/

You can see the raw responses from SportTastic and SuperPlayer here:

https://thekensman.github.io/sporting_data/sporttastic.json

https://thekensman.github.io/sporting_data/superplayer.json

You can start the application by running `sporting_data/app/app.py` in a debugger of your choice or through command line. If you do use the command line you will need to add the `sporting_data` directory to your PYTHONPATH. You can hit the API via the following routes:

http://localhost:5000/players

http://localhost:5000/players/_id_/bio

http://localhost:5000/players/_id_/stats

Note: Your run functions must return two elements: the response body and response code. Bonus points if you include handling for errors if the user passes in an id that is not found.
