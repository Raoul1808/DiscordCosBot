# Importation des librairies Python + Discord.py
import discord
from discord.ext import commands
import random

# Importation de fichiers locaux
import config
import checks


# Objet "bot" qui représente le bot. Essentiel
bot = commands.Bot(command_prefix=config.botPrefix)

# Chargement des extensions situées dans le dossier "cogs"
bot.load_extension("cogs.MathsModule")


# Évènement : se lance à la connexion à Discord
@bot.event
async def on_connect():
    print("Connected to Discord")


# Évènement : se lance quand le bot est identifié sur Discord et est entièrement opérationnel
@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user} ; {bot.user.id}")


# Évènement : se lance quand une erreur non gérée s'est produite dans n'importe quelle partie du code (incluant les fichiers externes et les librairies)
@bot.event
async def on_command_error(ctx, error):
    if not isinstance(error, commands.CommandNotFound):
        await ctx.send(f"```python\n{error}```")


# Commande (avec check) : Recharge tous les fichiers de commandes externes
@bot.command(name="reload", description="Recharge des extensions. Utilisable seulement par des Développeurs de confiance")
@commands.check(checks.isTrustedDeveloper)
async def _reload(ctx, cog=None):
    if cog:
        try:
            bot.reload_extension(f"cogs.{cog}")
            await ctx.send(f"{cog} rechargé avec succès !")
            return
        except commands.ExtensionNotFound:
            await ctx.send(":warning: Cette extension n'existe pas")
            return
    await ctx.send(":x: Je n'ai pas encore la capacité de recharger toutes les extensions")


# Lance le bot.
# TOUTES LES LIGNES APRES CELLE-CI SERONT IGNORÉES JUSQU'A L'EXTINCTION DU BOT
bot.run(config.TOKEN)