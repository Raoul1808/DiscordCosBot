# Fichier contenant tous les "checks" utilisés à travers tous les fichiers du bot
# Un "check" est une fonction personnalisée donnée au bot avant de lancer une commande.
# Si le résultat retourné est False (faux/négatif), la commande ne s'exécutera pas.


# Importation des librairies Python + Discord.py
import discord
from discord.ext import commands

# Importation des fichiers locaux
import config


# Check : si tel membre est porteur du rôle "Développeur de confiance"
async def isTrustedDeveloper(ctx):
    trustDev = ctx.guild.get_role(config.trustDevRole)
    return trustDev in ctx.author.roles