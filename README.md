# bot-template
A bot template using discord.py so you can create your own Discord bot!


discord.py is an API wrapper for discord. We will be using it to create a bot.
We will host our bot for free on Heroku.

# hosting
We will be using Heroku to host our bot. Start by creating a Heroku account. Create an application. 
Add a buildpack and choose Python. Next, head over to the tab that looks like a gear. Find the section "Config Vars". Under 'key', you're going to put "CLIENT_TOKEN" and for 'value', you're going to put your bots token. Add another row, but this time under key, put "PREFIX". Under 'value', put your bots token.
Now, you're going to link your Github repository with your bots code to this Heroku app. 
Go to the tab with the arrow. Scroll to the bottom and click 'Deploy Code'. Next, go to the tab that looks like a dashboard, and turn your bot on by clicking the pencil, turning your app on, and pressing 'Done'. 
After this, you should have a functional bot. If not, go to 'More' on the Heroku dashboard and click 'View Logs'. Find the error and fix it.
