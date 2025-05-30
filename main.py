import discord
from discord.ext import commands
import json
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def balance(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    await open_account(user)
    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    embed = discord.Embed(title=f"{user.name}'s Balance", color=discord.Color.green())
    embed.add_field(name="Wallet", value=f"{wallet_amt}")
    embed.add_field(name="Bank", value=f"{bank_amt}")
    await ctx.send(embed=embed)

@bot.command()
async def deposit(ctx, amount=None):
    if amount is None:
        await ctx.send("Please enter the amount you want to deposit")
        return

    user = ctx.author
    await open_account(user)
    users = await get_bank_data()

    if amount == 'all':
        amount = users[str(user.id)]["wallet"]
    else:
        try:
            amount = int(amount)
        except:
            await ctx.send("Please enter a valid amount")
            return

    if amount > users[str(user.id)]["wallet"]:
        await ctx.send("You don't have that much money in your wallet!")
        return

    if amount < 0:
        await ctx.send("Amount must be positive!")
        return

    users[str(user.id)]["wallet"] -= amount
    users[str(user.id)]["bank"] += amount

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    embed = discord.Embed(title="Deposit Successful", color=discord.Color.green())
    embed.add_field(name="Amount Deposited", value=f"{amount}")
    await ctx.send(embed=embed)

@bot.command()
async def withdraw(ctx, amount=None):
    if amount is None:
        await ctx.send("Please enter the amount you want to withdraw")
        return

    user = ctx.author
    await open_account(user)
    users = await get_bank_data()

    if amount == 'all':
        amount = users[str(user.id)]["bank"]
    else:
        try:
            amount = int(amount)
        except:
            await ctx.send("Please enter a valid amount")
            return

    if amount > users[str(user.id)]["bank"]:
        await ctx.send("You don't have that much money in your bank!")
        return

    if amount < 0:
        await ctx.send("Amount must be positive!")
        return

    users[str(user.id)]["bank"] -= amount
    users[str(user.id)]["wallet"] += amount

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    embed = discord.Embed(title="Withdrawal Successful", color=discord.Color.green())
    embed.add_field(name="Amount Withdrawn", value=f"{amount}")
    await ctx.send(embed=embed)

@bot.command()
async def send(ctx, user: discord.Member, amount=None):
    if amount is None:
        await ctx.send("Please enter the amount you want to send")
        return

    sender = ctx.author
    receiver = user
    await open_account(sender)
    await open_account(receiver)
    users = await get_bank_data()

    try:
        amount = int(amount)
    except:
        await ctx.send("Please enter a valid amount")
        return

    if amount > users[str(sender.id)]["wallet"]:
        await ctx.send("You don't have that much money in your wallet!")
        return

    if amount < 0:
        await ctx.send("Amount must be positive!")
        return

    users[str(sender.id)]["wallet"] -= amount
    users[str(receiver.id)]["wallet"] += amount

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    embed = discord.Embed(title="Transaction Successful", color=discord.Color.green())
    embed.add_field(name="Amount Sent", value=f"{amount}")
    embed.add_field(name="Sent to", value=f"{receiver.name}")
    await ctx.send(embed=embed)

async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)
    return users

if not os.path.exists("mainbank.json"):
    with open("mainbank.json", "w") as f:
        json.dump({}, f)

bot.run("YOUR_BOT_TOKEN")
