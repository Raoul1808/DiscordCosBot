# Importation de librairies Python + Discord.py
import discord
from discord.ext import commands
import random
from math import *
from random import *

# Création d'un Cog (aka extension de bot)
class MathsModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def calc(self, ctx, *, expression=None):
        if not expression:
            await ctx.send(":warning: Je ne peux pas calculer du vide ...")
            return
        if expression.find("import ") != -1:
            await ctx.send(":x: N'essayez surtout pas d'importer une librairie ...")
            return
        if expression.find("input(") != -1:
            await ctx.send(":x: Je ne peux pas exécuter les méthodes `input()`")
            return
        try:
            await ctx.send(f"```\n{expression} = {eval(expression)}```")
        except ZeroDivisionError:
            await ctx.send(":warning::warning::warning: **C'EST UN CRIME DE DIVISER PAR 0, EFFACEZ-MOI IMMÉDIATEMENT CE MESSAGE !!!!**")
        except Exception:
            await ctx.send(":x: J'ai rencontré une erreur durant le calcul, vérifiez qu'il soit correctement écrit")


def setup(bot):
    bot.add_cog(MathsModule(bot))