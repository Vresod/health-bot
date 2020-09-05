#!/usr/bin/env python3
import discord
import health

with open("tokenfile","r") as tokenfile:
    token = tokenfile.read()
client = discord.Client()

@client.event
async def on_ready():
    print(f"logged in as {client.user}")


# keep this at the end
client.run(token)
