import discord 
from discord.ext import commands


class Mods(commands.Cog):
    """Moderation commands for moderating and maintaining the decorm of the server"""
    
    def __init__(self,client):
        self.client = client
    
    # clear command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,amount : int):
        """The clear command purges messages from channel, if possible"""
        if amount < 1:
            m = discord.Embed(description="Please enter in valid positive numbers.",color=discord.Color.red())
            await ctx.channel.send(embed=m,delete_after=5)
        elif amount == 1:
            with ctx.channel.typing():
                await ctx.channel.purge(limit = amount+1)
                await ctx.channel.send(embed=discord.Embed(description=f"✅ I have deleted `{amount} message`!",color=discord.Color.blue()),delete_after=5)
        else:
            with ctx.channel.typing():
                await ctx.channel.purge(limit = amount+1)
                await ctx.channel.send(embed=discord.Embed(description=f"✅ I have deleted `{amount} messages`!",color=discord.Color.blue()),delete_after=5)
    @clear.error
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            m = discord.Embed(description='Please specify the number of messages to clear.',color = discord.Color.red())
            await ctx.channel.send(embed=m,delete_after=5)
        if isinstance(error, commands.MissingPermissions):
            m = discord.Embed(description=f"❌ You dont have permission to delete messages.",color=discord.Color.red())
            await ctx.channel.send(embed=m,delete_after=5)

    # kick command
    @commands.command(aliases=['k'])
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member: discord.Member,*,reason= None):
        """use to kick member from server"""
        await member.kick(reason=reason)
        await ctx.channel.send(embed=discord.Embed(description=f'👟 {member} has been kicked!',color=discord.Color.green()))
    @kick.error
    async def kick_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(embed=discord.Embed(description='❌ You dont have permission to kick.',color=discord.Color.red()),delete_after=5)

    # ban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member: discord.Member,*,reason= None):
        """use to ban member from server"""
        await member.ban(reason=reason)
        await ctx.channel.send(embed=discord.Embed(description=f'✅ {member} has been banned!',color=discord.Color.green()))
    @ban.error
    async def ban_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(embed=discord.Embed(description='❌ You dont have permission to ban.',color=discord.Color.red()),delete_after=5)

    # unban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,*,member):
        banned_users = await ctx.guild.bans()
        member_name,member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name,user.discriminator) == (member_name,member_discriminator):
                await ctx.guild.unban(user)
            m = discord.Embed(description=f'✅ {user.name}#{user.discriminator} has been unbanned!',color=discord.Color.green())
            await ctx.channel.send(embed=m,delete_after=5)
    @unban.error
    async def unban_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(embed=discord.Embed(description='❌ You dont have permission to unban.',color=discord.Color.red()),delete_after=5)
def setup(client):
    client.add_cog(Mods(client))