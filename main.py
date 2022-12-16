import discord

# TODO REVIEW outside the class ?
intents = discord.Intents.all()


# TODO Review Class MyClient in file main ????
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 1050685802662858823


    async def on_ready(self):
        print("Bereit")

    # giving roles
    # TODO REVIEW Method (on_raw_reaction) are identical. Use parameters and fusion those methods is a single one.
    async def on_raw_reaction_add(self, payload):
        # print("couocou")
        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name == "🤓":
            role = discord.utils.get(guild.roles, name="nerd")  # here give role code
            await payload.member.add_roles(role)

    # deleting roles
    async def on_raw_reaction_remove(self, payload):
        # print("couocou")
        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == "🤓":
            role = discord.utils.get(guild.roles, name="nerd")  # here give role code
            await member.remove_roles(role)


client = MyClient(intents=intents)

# TODO Review : this key have to be stored outside the code
client.run('MTA0MjczOTM3NTIwMjYzNTgyNg.GiuK7A.rl6ZSkQVMVbcA7RFG19v314cobYCfnE7juwwyM')
