# -*- coding: utf-8 -*-
"""
Bot 2 Discord
"""

import discord
import os


class DiscordBot:
    def __init__(self):
        #basic set of intents, not sure exactly what we need
        self.intents = discord.Intents(messages = True, typing = False, presences = False)
        
        #Need to have the token by here, not sure exactly how we're going to save/load them
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        
        #create the client
        self.client = discord.Client(self.intents)
        
        #run the client
        self.client.run(self.TOKEN)
    
    async def on_ready(self):
        user = self.client.user
        print(f'{ user } has connected to Discord!')
        
    
        
    