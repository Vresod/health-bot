#!/usr/bin/env python3
import discord

with open("tokenfile","r") as tokenfile:
    token = tokenfile.read()

# keep this at the end
client.run(token)
