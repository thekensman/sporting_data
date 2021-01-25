# sporting_data

You are being asked to create an API for a startup specializing a new and exciting game: BallSport! In BallSport each player can be assigned one of five positions: Catcher, Pitcher, Runner, Jumper, and Hitter. And because of the specialized nature of this game, each player can perform only within their given position.

The startup has asked you to integrate with two data providers they have contracted with: SportTastic and SuperPlayer. Each of these providers contains vital information about the players in the top six teams in the league. 

You are being asked to aggregate this data in an API and return it via three endpoints:
1. List all Players: this should return all the data for every player in a consistent format without duplicating any data. Bonus points if you implement sorting and pagination.
2. Single Player Bio Information: this should return the id, first name, last name, team, position, height, weight, jersey, and start year of a given player when passed the player id in the URL.
3. Single Player stats: this should return the id, catch total, hit total, pitch total, run total, jump total, and current year when passed the player id in the url.

We will be looking for your use of models via a library like pydantic or something similar:

https://pydantic-docs.helpmanual.io/usage/models/

You can see the raw responses from SportTastic and SuperPlayer here:

https://github.io/thekensman/sporting_data/sporttastic.json

https://github.io/thekensman/sporting_data/superplayer.json
