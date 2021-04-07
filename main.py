# Import des librairies Python + Discord.py
import discord
from discord.ext import commands
import random
from os import listdir, path, getcwd

# Import de fichiers locaux
import config
import checks


# Objet "bot" qui représente le bot. Essentiel
bot = commands.Bot(command_prefix=config.botPrefix)


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
    if isinstance(error, commands.CheckFailure):
        await ctx.send(":x: On dirait que vous n'avez pas les permissions requises pour exécuter cette commande ...")
        return
    if not isinstance(error, commands.CommandNotFound):
        await ctx.send(f":x: Une erreur s'est produite dans le code ...\n```python\n{error}```")


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
    failed = False
    message = "Rechargement des modules"
    error = None
    for cog in listdir(path.join(getcwd(), "cogs")):
        if cog.endswith('Module.py'):
            if failed:
                message += "\n:x: "+cog.replace('.py', '')
                continue
            try:
                bot.reload_extension(f"cogs.{cog.replace('.py', '')}")
                message += "\n:white_check_mark: " + cog.replace('.py', '')
            except Exception as e:
                message += "\n:warning: " + cog.replace('.py', '')
                error = e
                failed = True
    await ctx.send(message)
    if error:
        raise error


# Chargement automatique des modules listés dans le dossier "cogs". Critère de sélection : fichiers finissant par "Module.py"
for cog in listdir(path.join(getcwd(), "cogs")):
    if cog.endswith('Module.py'):
        try:
            bot.load_extension(f"cogs.{cog.replace('.py', '')}")
            print(f"{cog.replace('.py', '')} loaded successfully")
        except Exception as e:
            print(f"{cog.replace('.py', '')} failed to load")
            raise e



# Lance le bot.
# TOUTES LES LIGNES APRES CELLE-CI SERONT IGNORÉES JUSQU'A L'EXTINCTION DU BOT
bot.run(config.TOKEN)