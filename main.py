
import discord
import random
import asyncio
intents = discord.Intents.default()
intents.presences = True
intents.members = True
Black = ["yall", "i be", "nigga", "god damn it Gage", "Yall", "I be", "Nigga", "God damn it gage", "God damn it Gage", "god damn it gage"]
Mexican = ["Tomas is a pedo", "pedofile", "i got deported", "im playing genshin", "tomas is a pedo", "Pedofile", "I got deported"]
White = ["Fuck you randy", "i got raped", "ford is better", "Nigger", "yall", "fuck you randy", "I got raped", "Ford is better", "nigger", "Yall"]
Asian = ["rice is good ", "your failure", "that is not normal", "do your homework", "Rice is good", "Your failure", "That is not normal", "Do your math homework"]
NorthKoreanBot = ["@941017156987015218 Just Fucked up", "<@941017156987015218> already has the role Shame", "RepublicanBot already has role Shame", "<@941017156987015218> already has role Shame" ]
Gay = ["hey girl", "Hey Girl", "Yass", "yass"]
Blackslurs = ["Nigger", "Slave Boy", "cotton picker", "Monkey", "Alligater Bait shit"]
Mexicanslurs = ["Gardener Boy", "Illegal Trash", "Beaner", "TacoBell speaking shit"]
Asianslurs = ["Chink", "go back to the rice fields", "Ching Chong Bitch", "China Man faggot" ]
Whiteslurs = ["Cracker", "Honky bitch", "pedophile", "Twink"]
Gayslurs = ["Faggot", "Dyke", "Tranny", "Drag Fag"]
client = discord.Client(intents= intents)
@client.event

async def on_message(message):
  mention = message.author.mention
  Black2 = message.content.split(" ")
  print(Black2)
  if message.author == client.user:
        return
  if message.content.startswith("!Test"):
        await message.channel.send("Fuck North Korea")
        print(message.author.name)
  await asyncio.sleep(50)
  if message.content.startswith("and all you guys do is shoot up schools"):
    await asyncio.sleep(50)
    await message.channel.send("Well atleast im not a fuckin COMMIE!")
  if any(word in message.content for word in Black):
   await message.channel.send(f"{mention} Blackslurs{random.randint(0, len(Blackslurs) - 1)}")


  if any(word in message.content for word in White):
     await message.channel.send(f"{mention}{random.randint(0, len(Whiteslurs) - 1)}")
  if any(word in message.content for word in Asian):
     await message.channel.send(f"{mention} Asianslurs{random.randint(0, len(Asianslurs) - 1)}")
  if any(word in message.content for word in Mexican):
     await message.channel.send(f"{mention} Mexicanslurs{random.randint(0, len(Mexicanslurs) - 1)}")
  if any(word in message.content for word in NorthKoreanBot):
    await message.channel.send("All Your Kids be Starving bro. shut the fuck up")
  print(message.content)
  if any(word in message.content for word in Gay):
     await message.channel.send(f"{mention} Gayslurs{random.randint(0, len(Gayslurs) - 1)}")
  while True:
   await message.channel.send("Fuck North Korea")
  await asyncio.sleep(50)
  


#life is nothing but pain and math homework


@client.event
async def on_ready():
    print("time to offend some snowflakes")
    print("Logged IN")
    for member in client.get_all_members():
        if member.activity != None:    
            if  "Logging Data" in str(member.activity.name):
                print(f"{member.name} is playing {member.activity}" )
            else:
                print(f"{member.name} is playing {member.activity}")
                

client.run('OTQxMDE3MTU2OTg3MDE1MjE4.YgP0hQ.lZWwUKIclOY7j1SXB1I_XtfkTow')

