import discord
from discord.ext import commands
import roles
import phases
import voting
import statistics

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

players = []
roles_dict = {}

@bot.command()
async def join(ctx):
    """Присоединение игрока к игре"""
    if ctx.author.name not in players:
        players.append(ctx.author.name)
        await ctx.send(f"{ctx.author.name} присоединился к игре!")
    else:
        await ctx.send("Вы уже в игре!")

@bot.command()
async def start(ctx):
    """Начало игры и распределение ролей"""
    global roles_dict
    if len(players) < 4:
        await ctx.send("Недостаточно игроков для начала игры.")
    else:
        roles_dict = roles.assign_roles(players)
        voting.init_voting(players)
        await ctx.send("Игра началась! Роли распределены. Начинается ночная фаза.")

@bot.command()
async def vote(ctx, target: str):
    """Голосование за исключение игрока"""
    if target not in players:
        await ctx.send("Неверный игрок для голосования.")
    else:
        voting.vote(ctx.author.name, target)
        await ctx.send(f"{ctx.author.name} проголосовал за {target}.")

@bot.command()
async def end_day(ctx):
    """Подсчёт голосов и исключение игрока"""
    excluded = voting.tally_votes()
    if excluded:
        players.remove(excluded)
        statistics.add_kill(excluded)
        await ctx.send(f"{excluded} был исключён из игры!")
    else:
        await ctx.send("Голосование не дало результатов. Ничья.")
    voting.reset_votes()
    phases.next_phase()

@bot.command()
async def show_stats(ctx):
    """Показать игровую статистику"""
    statistics.show_statistics()

bot.run(TOKEN)
