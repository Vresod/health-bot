import discord

health_roles = ["751857572377788477", "751857546238885958", "751857518451359754", "751857495017783366", "751857471035015299", "751857433155993791", "751857402420396114", "751857379804446871", "751857355909759005", "751857317380620448"]

def reduce_health(member):
	for role in member.roles:
		if role in health_roles:
			current_health = health_roles.index(role)
	member.remove_role(client.role_from_id(current_health))
	member.add_role(client.role_from_id(health_roles[current_health - 1]))
	return current_health - 1

def gain_health(member):
	for role in member.roles:
		if role in health_roles:
			current_health = health_roles.index(role)
	member.remove_role(client.role_from_id(current_health))
	member.add_role(client.role_from_id(health_roles[current_health + 1]))
	return current_health + 1

