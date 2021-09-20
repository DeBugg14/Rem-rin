import discord
import random
import requests
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # 8ball
    @commands.command(name='8ball', description='Let the 8 Ball Predict!\n')
    async def _8ball(self, ctx, *, question):
        """Answers your question"""
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]
        response = random.choice(responses)
        embed = discord.Embed(
            title="The Magic 8 Ball has Spoken!", color=discord.Color.blue(),timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name='Question: ', value=f'{question}', inline=True)
        embed.add_field(name='Asked by:', value=f'{ctx.author}', inline=False)
        embed.add_field(name='Answer: ', value=f'{response}', inline=False)
        await ctx.send(embed=embed)
    
    @_8ball.error
    async def _8ball_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            pass
    
    # meme
    @commands.command()
    async def meme(self,ctx):
        "sends meme"
        r = requests.get('https://memes.blademaker.tv/api?lang=en')
        res = r.json()
        m = discord.Embed(color=discord.Color.blue())
        m.add_field(name=f'{res["title"]}',value=f'`posted by: {res["author"]}`',inline=False)
        m.add_field(name='Subreddit: ',value=f'`{res["subreddit"]}`')
        m.set_image(url=res["image"])
        m.set_footer(text=f'👍:{res["ups"]}  👎:{res["downs"]} ')
        await ctx.channel.send(embed=m)

    #avatar
    @commands.command()
    async def avatar(self,ctx, member : discord.Member=None):
        if member is None:
            m = discord.Embed(title=f'{ctx.author}',url=ctx.author.avatar_url,color=discord.Color.blue(),timestamp=ctx.message.created_at)
            m.set_image(url=ctx.author.avatar_url)
            await ctx.channel.send(embed=m)
        else:
            m = discord.Embed(title=f'{member}',url=member.avatar_url,color=discord.Color.blue(),timestamp=ctx.message.created_at)
            m.set_image(url=member.avatar_url)
            await ctx.channel.send(embed=m)
    
    # ping
    @commands.command()
    async def ping(self,ctx):
        embed = discord.Embed(title='🏓Pong!',description=f'\tLatency: {round(self.client.latency*1000)} ms',color=discord.Color.blue())
        await ctx.send(embed=embed,delete_after=5)
    
def setup(client):
    client.add_cog(Fun(client))
