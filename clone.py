import os

import discord
from dotenv import load_dotenv
import random

TOKEN = 'ODM3MTgyNTcwODY0NDQzMzky.YIo1Bg.cgsWXN_orif2AuaN0_PhNv7mDZY'

client = discord.Client()



@client.event
async def on_ready():
    guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in client.guilds:
		# PRINT THE SERVER'S ID AND NAME.
	    print(f"- {guild.id} (name: {guild.name})")
		# INCREMENTS THE GUILD COUNTER.
	    guild_count = guild_count + 1
    print("CricGo is in " + str(guild_count) + " guilds.")
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, welcome to the Discord server!'
    )

@client.event
async def on_message(message):

    async def bat1():
        await message.channel.send('CricGo is going to bowl')
        total = 0
        while (True):
            match = random.randint(1, 6)
            CricGo = random.randint(1, 6)
            await message.channel.send('Play Your Shot:')
            msg3 = await client.wait_for("message", check=check3)
            if int(msg3.content)>6:
                await message.channel.send('You arent allowed to play any number more than 6!\nThe game will restart now')
                break
            else:
                await message.channel.send(f"CricGo plays: {CricGo}")  
                if (CricGo == int(msg3.content)):
                    await message.channel.send("GOTCHA! Number Matched! ...your out!!!")
                    await message.channel.send(f"Your total runs = {total}")
                    break
                total = total + int(msg3.content)          
        await message.channel.send(f'Target for CricGo is {total+1}')
        await message.channel.send('It is CricGos time to bat.')
        ctotal = 0
        while (True):
            while(ctotal<total):                
                cmatch = random.randint(1, 6)
                CricGo = random.randint(1, 6)
                await message.channel.send('Input Your Ball:')
                msg4 = await client.wait_for("message", check=check4)
                if int(msg4.content)>6:
                    await message.channel.send('You arent allowed to play any number more than 6!\nThe game will restart now')
                    break
                await message.channel.send(f"CricGo plays: {CricGo}")
                ctotal = ctotal + CricGo       
                if (CricGo == int(msg4.content)):
                    ctotal = ctotal - CricGo 
                    await message.channel.send("GOTCHA! Number Matched! ...your out!!!")
                    await message.channel.send(f"CricGo's total runs = {ctotal}")
            if ctotal>total:
                await message.channel.send('Yayyyy! You lose!')
                break
            elif total>ctotal:
                await message.channel.send('Congoo You Win!')
                await message.channel.send(f'Well Played {str(message.author)[:-5]}')
                break
            else:
                await message.channel.send('And its a Tie!')
                break 


    async def bat2():
        await message.channel.send('CricGos is going to bat.')
        ctotal = 0
        while (True):
            cmatch = random.randint(1, 6)
            CricGo = random.randint(1, 6)
            await message.channel.send('Input Your Ball:')
            msg4 = await client.wait_for("message", check=check4)
            if int(msg4.content)>6:
                print('You arent allowed to play any number more than 6.The game will restart now')
                break
            await message.channel.send(f"CricGo plays: {CricGo}")
                        
            if (CricGo == int(msg4.content)):
                await message.channel.send("Number Matched! ..out!!!")
                await message.channel.send(f"CricGo's total runs ={ctotal}")
                break
            ctotal = ctotal + CricGo
        await message.channel.send(f'Your Target is {ctotal+1}')
        await message.channel.send('The CricGo is bowling')
        total = 0
        while (True):
            while(total<ctotal):
                match = random.randint(1, 6)
                CricGo = random.randint(1, 6)
                await message.channel.send('Play Your Shot:')
                msg3 = await client.wait_for("message", check=check3)
                if int(msg3.content)>6:
                    await message.channel.send('You arent allowed to play any number more than 6.The game will restart now')
                    break
                await message.channel.send(f"CricGo plays: {CricGo}")   
                total = total + int(msg3.content)
                if (CricGo ==int(msg3.content)):
                    total = total - int(msg3.content)
                    await message.channel.send("Number Matched! ..out!!!")
                    await message.channel.send(f"Your total runs ={total}")    
                    break
            if ctotal>total:
                await message.channel.send('Yayyyy! You lose!')
                break
            elif total>ctotal:
                await message.channel.send('Congoo You Win!')
                await message.channel.send(f'Well Played {str(message.author)[:-5]}')
                break
            else:
                await message.channel.send('And its a Tie!')  
                break                           

    async def toss():
        await message.channel.send('What do You Wanna Choose? (odd/eve):')
        msg = await client.wait_for("message", check=check)
        await message.channel.send('Play your number for the toss(1/2):')
        msg1 = await client.wait_for("message", check=check1)
        if int(msg1.content) >2:
            await message.channel.send('You are only allowed to use 1 and 2.')
            exit()
        else:
            print('bot not taken decison')
            z=random.randint(1,2)
            print('bot taken decison')
            await message.channel.send(f"I've Chosen {z}")

            if msg.content.lower() =='eve':
                if ((int(msg1.content)+z)%2)==0:
                    await message.channel.send('You have Won the Toss')
                    await message.channel.send('What Do You Opt?(bat/bowl)')
                    msg2 = await client.wait_for("message", check=check2)
                    if msg2.content.lower() == 'bat':
                        await bat1()                       
                    elif msg2.content.lower() == 'bowl' :
                        await bat2()                   
                else:
                    await message.channel.send('CricGo has Won the Toss')
                    x=random.choice(['bat','bowl'])
                    if x=='bat':
                        await bat2()
                    elif x=='bowl':
                        await bat1()

            elif msg.content.lower() =='odd':
                if((int(msg1.content)+z)%2)==0:
                    y=random.choice(['bat','bowl'])
                    if y=='bat':
                        await bat2()                    
                    elif y=='bowl':
                        await bat1()                        
                else:
                    await message.channel.send('You have Won the Toss')
                    await message.channel.send('What Do You Opt?(bat/bowl)')
                    msg2 = await client.wait_for("message", check=check2)
                    if msg2.content.lower() == 'bat':
                        await bat1()
                    elif msg2.content.lower() == 'bowl':
                        await bat2() 
                    else:
                        print('Invalid input! The game will restart')
            else:
                await message.channel.send("Invalid Input")

    def check(msg):
        return msg.author == message.author and msg.channel == message.channel and \
        msg.content.lower() in ["odd", "eve"]

    def check1(msg1):
        return msg1.author == message.author and msg1.channel == message.channel and \
        int(msg1.content) in [1, 2]

    def check2(msg2):
        return msg2.author == message.author and msg2.channel == message.channel and \
        msg2.content.lower() in ["bat", "bowl"]

    def check3(msg3):
        return msg3.author == message.author and msg3.channel == message.channel and \
        int(msg3.content) in [1,2,3,4,5,6]

    def check4(msg4):
        return msg4.author == message.author and msg4.channel == message.channel and \
        int(msg4.content) in [1,2,3,4,5,6]

    if message.author == client.user:
        return

    if (message.content == '!hello'):
        response= 'Hey there '+str(message.author)[:-5] 
        await message.channel.send('{}'.format(response))
    
    elif (message.content == '!help'):
        response= 'This is a User vs CricGo cricket game.\n'+'Some Basic rules to begin with :-\n'+'1.You can only enter 1 and 2 for the toss\n'+'2.You can enter numbers from 1 to 6 while batting or bowling\n'+'-- You dont follow the Rules,You Gotta restart!\n'
        await message.channel.send('{}'.format(response))
    
    elif(message.content == '!play'):
        await message.channel.send(f"Cricgo  V/S  {str(message.author)[:-5]}")
        await toss()
    
    elif(message.content == '!info'):
        res = 'CricGo is currently Under Development!\n'+'The commands available are :\n'+'!hello\n'+'!help\n'+'!play\n'+'!info\n'
        await message.channel.send('{}'.format(res))

    
                              

client.run(TOKEN)
