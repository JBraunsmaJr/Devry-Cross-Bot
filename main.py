# -*- coding: utf-8 -*-
"""
Main file
"""
import Bot2Discord.discordBot as discordBot
import Bot2Teams.TeamsBot as TeamsBot


def main():
    
    #create discord bot
    disBot = discordBot()
    
    #create Teams bot
    teamBot = TeamsBot()
    
    #need to host somewhere here 


if __name__=="__main__":
    main()
