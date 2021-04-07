# Import de librairies Python
import discord
from discord.ext import commands

# Création du cog Sondage
class SondageModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Commande Sondage Fermé (oui/non)
    @commands.command()
    async def ouinon(self, ctx, *, message):
        await ctx.message.delete()
        embed = discord.Embed(title="Sondage", description=message, colour=ctx.author.colour)
        embed.set_footer(text=f"Lancé par {ctx.author.nick}. Réagissez avec ✅ ou ❌")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")


# Ajout du cog au bot
def setup(bot):
    bot.add_cog(SondageModule(bot))