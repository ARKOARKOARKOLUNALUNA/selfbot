#====================
# tut to use
#====================
 # get a token and create a .env file and dmlog.txt 
 # make sure ur token isnt surrounded by any "" and stuff
 # change  != 1385063037454651422: to the user id u want the acc to respond to "1385063037454651422" is my id change it!
 # this is really basic so u should be able to understand
 # put this into your terinal python -m pip install discord.py-self , python -m pip install python-dotenv  and then run those and then do python main.py in ur termal after! and it should work
 # 

#=============
# changelog
#=============
# + 3/21/26
# + simple self bot script 
# + added tut to get bot token etc
# + right now it just reads messages and prints them i think ima test 
# + i got it to log messages after like 15 mins
# + ima save this print(f"{message.author}: {message.content}")
# + made it to log uhh messages in a file called dmlog.txt imad add more
# + made it so it wipes dmlog.txt with key word wipelog
# + made it so that when u say .menu it sends stuff on the acc
# + fixed so it logs messages and does other functions at the same time |2/21 6:23pm|
# + added auto react how can ppl not figure this out its 2 lines 😭
# + 3/22/26
# + added uh menu boxes and reactions working on so that it will auto react when u send an emoji
# + removed that, trying to make ghost ping set off with "ghost"
# + made ghost ping work
# + 3/23/26
# + added auto timeout using from datetime import timedelta to control times and shit
# + cleaned up teh code a little and deleted auto dm was annyoing the code is still at the bottom 
# +


#-----------------------------------------------------------------------------------------------------
#  i think im done with this project idk what to add :sob:, its been fun using python more! ty eva
#-----------------------------------------------------------------------------------------------------


import os
import json
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
from datetime import timedelta


load_dotenv()
UserToke = os.getenv("UserToken")

bot = commands.Bot(command_prefix="!", self_bot=True)

#==================
# comamands
#==================

@bot.event
async def on_ready():
    print("succesfully logged in")


@bot.event
async def on_message(message):
    if message.author.id != 1432525246325457062: #this is my id change it!
        return
    with open("dmlog.txt", "a", encoding="utf-8") as f:
     f.write(f"{message.author}: {message.content}\n")
     f.flush()
     print("messages logged to: dmlog.txt")
     

     with open("dmlog.txt", "r", encoding="utf-8") as f:
        logContent = f.read()
     if message.content.lower() == "wipelog":
       with open("dmlog.txt", "r", encoding="utf-8") as f:
            logContent = f.read()
            print(logContent)
            await message.channel.send(f"Deleted logs \n\n- made by arko! ")
            open("dmlog.txt", "w").close()
            print("wiped log")

    if message.content.lower() == ".menu":
     await message.channel.send("\n1. Message Log \n2. Ghost Ping \n3. Auto React")
       
    if message.content.lower() == "ghost":
        msg = await message.channel.send("<@1145818847870460047>")
        await msg.delete()
        print("ghost pinged!")

    if message.author.id == 1432525246325457062:
       member = message.guild.get_member(1432525246325457062)
       if member:
            await member.timeout(timedelta(minutes=10))
            await message.channel.send(f"{member.name} tried talking LOL\n https://media.discordapp.net/attachments/1046259533569331310/1048557228816347207/A0B58B30-1C2F-4AB7-AD6A-C0DD220C942D.gif?ex=69c31a44&is=69c1c8c4&hm=86fb2335dc1a0d4040407191e0889d9e09768243a391266b06283c40fd336ac2&    \n this was inspired by evass")
            print(f"Muted {member.name} for 10 mins.")



if UserToke is None:
    print("cant find anything in the env file check code 1-25")
else:
    print("tryying to log in")
    try:
        bot.run(UserToke)
    except TypeError: 
      bot.run(UserToke, bot=False)


# this was made by arko!
# https://cutz.lol/arko




#---------------------------------
# auto react turn this off for now
#---------------------------------
 #   if message.author.id == 1385063037454651422:
   #   await message.add_reaction("☠️")
     # print("auto react works")



#----------------------------------------------
# illcome back to this (also this doesnt work)
#----------------------------------------------
# watermark = "-Arko Self Bot"
        # user = bot.get_user(1385063037454651422)
        # if message.content.lower("Dm me"):
        
        
           # await user.send(f"wow i can send u dms from typing anywhere {watermark}")
           # print("sent private dm")


#---------------------------------
# auto dm removing cause annyoing
#---------------------------------

# watermark = "-Arko Self Bot"
   # user = bot.get_user(1432525246325457062)
   # await user.send(f"wow i can send u dms from typing anywhere {watermark}")
   # print("sent private dm")
