# bot-template
A bot template using discord.py so you can create your own Discord bot!


# what will we use
discord.py is an API wrapper for discord. We will be using it to create a bot.
We will host our bot for free on Heroku.

# read the docs
Read the discord.py documentation at https://discordpy.readthedocs.io
See the discord.py Github repository: https://github.com/rapptz/discord.py
Join the official discord.py server: https://discord.gg/dpy

# creating the bot
Go to https://discordapp.com/developers. Create an application. This will be your bot. Give your bot a name and profile picture. Then go to the 'Bot' tab and 'copy token'. Never share your token. Go to the Oauth2 tab and click the permissions your bot needs. Use the link it generates for you to add the bot to a test server. It will show up as offline.

# coding
Create a GitHub account (if you haven't already). Create a repository, and make sure that it's private. Create 4 files in the repository. Name them 'Procfile', 'requirements.txt', 'runtime.txt', and 'main.py'. View the other files of this repository to see what to put in the files.

# hosting
We will be using Heroku to host our bot. Start by creating a Heroku account. Create an application. 
Add a buildpack and choose Python. Next, head over to the tab that looks like a gear. Find the section "Config Vars". Under 'key', you're going to put "CLIENT_TOKEN" and for 'value', you're going to put your bots token. Add another row, but this time under key, put "PREFIX". Under 'value', put your bots prefix.
Now, you're going to link your Github repository with your bots code to this Heroku app. 
Go to the tab with the arrow. Scroll to the bottom and click 'Deploy Code'. Next, go to the tab that looks like a dashboard, and turn your bot on by clicking the pencil, turning your app on, and pressing 'Done'. 
After this, you should have a functional bot. If not, go to 'More' on the Heroku dashboard and click 'View Logs'. Find the error and fix it.

# faq
1. Yes, this is completely free.
2. Yes, you could do this on your phone if you don't have a computer
3. A Syntax Error usually means you missed an indentation, (), [], "", '', etc. Same if your code stopped changing colors.
4. If your bot is offline, go to 'More' on your Heroku dashboard, and look at the logs. Most errors are simple to fix. If you want your bot online again right away, make sure that automatic deploys are disabled, and delete the problematic code. Deploy the app again, and work on the code that didn't run.
5. You should never share your token since people can use it to do bad things with your bot. Make sure that your repository is private, and that you never share it.

# help command
discord.py comes with a default help command. You can find information about it here: https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96
