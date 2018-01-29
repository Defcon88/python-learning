games=["starfox","mario","zelda","minecraft","contra"]

for game in games:
	print(game)

print("\nThese are the first two games: " + str(games[:2]))
print("\nThese are the next two games: " + str(games[2:4]))
print("\nThis is the last game: " + str(games[-1:]))

