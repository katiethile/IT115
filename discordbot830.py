'''Importing the class libraries to be able to interact with one another and to have the functions of the libraries embedded. Importing the token file. Importing the random class library to be able to randomly generate something and use the random functions.''' 

import discord 
import os 
import random
from ec2_metadata import ec2_metadata

'''Printing out the ec2 metadata region and instance id to make sure they are properly working.'''
print(ec2_metadata.region)
print(ec2_metadata.instance_id)

'''Here, we are creating a discord client to send a request to discord API. We are also using the load_dotenv function to import environment variables.Then, for the token variable, we are getting and initializing our environment token'''
client = discord.Bot()
token = os.getenv('TOKEN')

'''Here is when the event for the client is triggered, when they are ready to be logged in. The on_ready function event is used, provided by the discord API. Once our API client has initialized this event will trigger, perfoming the given operation. The name of the bot is printed'''
@client.event 
async def on_ready(): 
	print("Logged in as a bot {0.user}".format(client))

'''This is event drawn by the client passing in information needed to process. The creation of 3 variables/objects which in turn will output a message into a string.'''
@client.event 
async def on_message(message): 
	username = str(message.author).split("#")[0] 
	channel = str(message.channel.name) 
	user_message = str(message.content) 

	print(f'Message {user_message} by {username} on {channel}') 

	if message.author == client.user: 
		return

#If the channel name is random, then run a bunch of conditional statements that checks the lower case values of the word you want to check.
	if channel == "random": 
		if user_message.lower() == "hello there" or user_message.lower() == "hello there": 
			await message.channel.send(f'Sooner! {username} Thanks for logging in') 
			return
		elif user_message.lower() == "until another time": 
			await message.channel.send(f'Goodbye! {username} Until the next time you log in!') 
		elif user_message.lower() == "you're still here?": 
			await message.channel.send("Why are you still here?") 



'''How the bot in run, by calling the on_ready event, passing in the token as a argument'''
client.run(token)
