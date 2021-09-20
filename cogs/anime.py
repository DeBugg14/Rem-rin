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