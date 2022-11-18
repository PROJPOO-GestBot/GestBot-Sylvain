import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

        
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('susPhrase'):
        await message.channel.send('se masdak le code pénal')
    elif message.content == "give me fun":
        role = discord.utils.get(message.guild.roles, name="fun") #role by id and not by name
        await message.author.add_roles(role)
        await message.channel.send('here is a bunch of fun commin for ya')




client.run('MTA0MjczOTM3NTIwMjYzNTgyNg.GiuK7A.rl6ZSkQVMVbcA7RFG19v314cobYCfnE7juwwyM')