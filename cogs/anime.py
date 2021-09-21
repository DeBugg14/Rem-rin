import discord
import animec
import requests
import json
import random
import os
from dotenv import load_dotenv
load_dotenv()
from discord.ext import commands


class Anime(commands.Cog):
    def __init__(self,client):
        self.client = client

    # anime search
    @commands.command(name='anime')
    async def anime_search(self,ctx,*,query):
        """use to get info about anime"""
        try:
            anime = animec.Anime(query)
        except animec.errors.NoResultFound:
            await ctx.channel.send(embed = discord.Embed(description=f"**{ctx.author}**, nothing found.",color=discord.Color.blue()),delete_after=5)
            return
        embed = discord.Embed(title=anime.title_english or anime.name,url=anime.url,description=f'{anime.description}',color=discord.Color.blue(),timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
        embed.add_field(name='Rating',value= str(anime.rating))
        embed.add_field(name='Popularity Ranking',value= str(anime.popularity))
        embed.add_field(name='Favourites',value= str(anime.favorites))
        embed.add_field(name='Genre',value= str(anime.genres))
        embed.add_field(name='Status',value= str(anime.status))
        embed.add_field(name="Type",value=str(anime.type))
        embed.add_field(name='Opening',value = str(anime.opening_themes),inline=False)
        embed.add_field(name='Ending',value=str(anime.ending_themes),inline=False)
        embed.set_thumbnail(url= anime.poster)
        await ctx.channel.send(embed=embed)

    @anime_search.error
    async def anime_search_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            pass
    
    # character search
    @commands.command(aliases=['char','animecharacter','ch'],name='character')
    async def character_search(self,ctx,*,query):
        """use to search anime characters"""
        try:
            char = animec.Charsearch(query)
        except:
            await ctx.channel.send(embed = discord.Embed(description=f"**{ctx.author}**, nothing found.",color=discord.Color.blue()),delete_after=5)
            return
        embed = discord.Embed(title=char.title,url=char.url,color=discord.Color.blue())
        embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
        embed.set_image(url=char.image_url)
        embed.set_footer(text=",\n".join(list(char.references.keys())[:1]))
        await ctx.channel.send(embed=embed)
    
    @character_search.error
    async def character_search_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            pass
    

    # waifu search
    @commands.command(name='waifu')
    async def waifu_search(self,ctx,*,query):
        """use to search waifus

            available query to use-
            1)random1 - returns random waifu in png
            2)random gif - returns random waifu in gif
            3)random2 - returns random waifu in png
            4)cuddle - returns random cuddle in gif
            5)hug - returns random hug in gif
            6)kiss - returns random kiss in gif
            7)lick - returns random lick in gif
            8)pat - returns random pat in gif
            9)smug - returns random smug in gif
            10)bonk - returns random bonk in gif
            11)yeet - returns random yeet in gif
            12)blush - returns random blush in gif
            13)highfive - returns random highfive in gif
            14)handhold - returns random handhold in gif
            15)bite - returns random bite in gif
            16)slap - returns random slap in gif
            17)kick - returns random kick in gif
            18)happy - returns random happy in gif
            19)wink - returns random wink in gif
            20)dance - returns random dance in gif
            21)cringe - returns random cringe in gif
        """
        waifu = animec.Waifu()
        m = discord.Embed(color=discord.Color.blue(),timestamp=ctx.message.created_at)
        if query == 'random1':
            m.set_image(url=waifu.random())
            await ctx.channel.send(embed=m)
        elif query == 'random gif':
            m.set_image(url=waifu.random_gif())
            await ctx.channel.send(embed=m)
        elif query == 'random2':
            m.set_image(url=waifu.waifu())
            await ctx.channel.send(embed=m)
        elif query == 'cuddle':
            m.set_image(url=waifu.cuddle())
            await ctx.channel.send(embed=m)
        elif query == 'hug':
            m.set_image(url=waifu.hug())
            await ctx.channel.send(embed=m)
        elif query == 'kiss':
            if ctx.channel.is_nsfw():
                m.set_image(url=waifu.kiss())
                await ctx.channel.send(embed=m)
            else:
                await ctx.channel.send(embed = discord.Embed(description='Woah! this channels is not nsfw',color=discord.Color.red()),delete_after=5)
        elif query == 'lick':
            m.set_image(url=waifu.lick())
            await ctx.channel.send(embed=m)
        elif query == 'pat':
            m.set_image(url=waifu.pat())
            await ctx.channel.send(embed=m)
        elif query == 'smug':
            m.set_image(url=waifu.smug())
            await ctx.channel.send(embed=m)
        elif query == 'bonk':
            m.set_image(url=waifu.bonk())
            await ctx.channel.send(embed=m)
        elif query == 'yeet':
            m.set_image(url=waifu.yeet())
            await ctx.channel.send(embed=m)
        elif query == 'blush':
            m.set_image(url=waifu.blush())
            await ctx.channel.send(embed=m)
        elif query == 'smile':
            m.set_image(url=waifu.smile())
            await ctx.channel.send(embed=m)
        elif query == 'highfive':
            m.set_image(url=waifu.highfive())
            await ctx.channel.send(embed=m)
        elif query == 'handhold':
            m.set_image(url=waifu.handhold())
            await ctx.channel.send(embed=m)
        elif query == 'bite':
            m.set_image(url=waifu.bite())
            await ctx.channel.send(embed=m)
        elif query == 'slap':
            m.set_image(url=waifu.slap())
            await ctx.channel.send(embed=m)
        elif query == 'kick':
            m.set_image(url=waifu.kick())
            await ctx.channel.send(embed=m)
        elif query == 'happy':
            m.set_image(url=waifu.happy())
            await ctx.channel.send(embed=m)
        elif query == 'wink':
            m.set_image(url=waifu.wink())
            await ctx.channel.send(embed=m)
        elif query == 'dance':
            m.set_image(url=waifu.dance())
            await ctx.channel.send(embed=m)
        elif query == 'cringe':
            m.set_image(url=waifu.cringe())
            await ctx.channel.send(embed=m)
        else:
            await ctx.channel.send(embed=discord.Embed(description='Please enter correct value',color=discord.Color.red()))
        

    # re zero
    @commands.command()
    async def rem(self,ctx):
        """use get best girl rem gifs"""
        apikey = os.getenv('TENOR_TOKEN')
        search = "rem rezero"
        lmt = 18
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %(search, apikey, lmt))
        if r.status_code == 200:
            res = json.loads(r.content)
            giff = random.randint(0,17)
            m = discord.Embed(title='Rem is Fanatical like a Demon!',color=discord.Color.blue(),timestamp=ctx.message.created_at)
            m.set_image(url=res['results'][giff]['media'][0]['gif']['url'])
            await ctx.channel.send(embed=m)
def setup(client):
    client.add_cog(Anime(client))