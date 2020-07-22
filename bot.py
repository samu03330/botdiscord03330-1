import discord
import random
import time
import os
from discord.ext import commands, tasks

client = commands.Bot(command_prefix='?')

class BotData:
    def __init__(self):
        self.reaction_role = 682584980223950931
        self.reaction_message = 735496901910200390

botdata = BotData()

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == botdata.reaction_message.id and botdata.reaction_role != None:
        await payload.member.add_roles(botdata.reaction_role)

@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == botdata.reaction_message.id and botdata.reaction_role != None:
        await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(botdata.reaction_role)


@client.command()
async def set_reaction_role(ctx, message_id=None, role_id=None):
    for channel in ctx.guild.channels:
        try:
            botdata.reaction_message = await channel.fetch_message(int(message_id))
            break

        except:
            pass

    if botdata.reaction_message == None:
        await ctx.send("Non è stato possibile trovare il messaggio indicato.")
        

    else:
        await ctx.send("Il messaggio è stato settato correttamente")
       

    try:
        botdata.reaction_role = ctx.guild.get_role(int(role_id))

    except:
        botdata.reaction_role = None

    if botdata.reaction_role == None:
        await ctx.send("Non è stato possibile trovare il ruolo assegnato.")
        time.sleep(10)
        await ctx.channel.purge(limit=2)

    else:
        await ctx.send("Hai impostato tutto correttamente")
        time.sleep(10)
        await ctx.channel.purge(limit=2)




@client.event
async def on_ready():
    print("Il Bot è Online") 
    stato=discord.Status.online
    await client.change_presence(status=stato,activity=discord.Activity(type=discord.ActivityType.watching, name="developing by 💯Samu💯ツ#2826"))





'''#Cogs

@client.command()
async def load(extension):
    try:
         client.load_extension(extension)
         print('Loaded {}'.format(extension))
    except Exception as error:
         print('{} cannot be loaded. [{}]'.format(extension, error))



@client.command()
async def unload(extension):
    try:
         client.unload_extension(extension)
         print('Unloaded {}'.format(extension))
    except Exception as error:
         print('{} cannot be unloaded. [{}]'.format(extension, error))


if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))'''



#Messaggio in DM

@client.command()
async def prova(ctx):
    await ctx.author.send('ciao mamma')




#clear chat

@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)



@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument ):
        await ctx.send('inserisci il numero di messaggi da eliminare')




@client.event
async def on_comand_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Seleziona un comando valido')




#kick utenti

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)



#ban utenti   

'''@client.command()
async def ban(ctx,membro : discord.Member,*,reason=None):
    log=ctx.guild.get_channel(727552935231488072)
    await membro.ban(reason=reason)
    embed=discord.Embed(
        title="BANNATO",
        description=f'{membro.name} è stato bannato per: {reason}',
        colour=discord.Colour.blue()
    )
    embed.set_footer(text='niente')
    await log.send(embed=embed)''' 



#ban utenti 2

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')



#unban utenti 

@client.command()
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')


    for ban_entry in banned_user:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')


client.run(os.environ['discord_token'])

