import random

## base stats
stats = {"vigor": 5, "vitality": 5, "swiftness": 5, "dexterity": 5}

clan_stat = {
    "Lynxclan": "vigor",
    "Minkclan": "vitality",
    "Wolfclan": "dexterity",
    "Sealclan": "swiftness"
}

size_changes = {
    4: {"vigor": -1, "swiftness": 1},
    5: {"vigor": 1, "swiftness": 1},
    6: {"vigor": 1, "vitality": 1},
    7: {"vigor": 1, "swiftness": -1},
    8: {"vigor": 2, "swiftness": -2},
    9: {"vigor": 3, "swiftness": -3},
    10: {"vigor": 4, "swiftness": -4, "vitality": -2},
}

## halfclan question
halfclan_status = input("Is your cat a halfclan? Y/N. ").upper().strip()
while halfclan_status != "Y" and halfclan_status != "N":
    print("Please type Y or N.")
    halfclan_status = input("Is your cat a halfclan? Y/N. ").upper().strip()
## calculating stats based on clan status
if halfclan_status == "Y":
    clan1 = input("What is your cat's first clan? ").strip().title()
    while clan1 not in clan_stat:
        print("Invalid clan! Please try again.")
        clan1 = input("What is your cat's first clan? ").strip().title()

    clan2 = input("What is your cat's second clan? ").strip().title()
    while clan2 not in clan_stat or clan2 == clan1:
        print("Invalid clan, or it's the same as the first clan! Please try again.")
        clan2 = input("What is your cat's second clan? ").strip().title()

    stats[clan_stat[clan1]] += 1
    stats[clan_stat[clan2]] += 1
else:
    clan = input("What is your cat's clan? Type N/A if a rogue cat. ").strip().title()
    while clan not in clan_stat and clan != "N/A":
        print("Invalid clan! Please try again.")
        clan = input("What is your cat's clan? Type N/A if a rogue cat. ").strip().title()

    if clan == "N/A":
        stats[random.choice(list(stats))] += 1
        stats[random.choice(list(stats))] += 1
    else:
        stats[clan_stat[clan]] += 2

## size
size = int(input("What is your cat's size (1-10)? "))
while size < 1 or size > 10:
    print("Invalid size! Please check our document to select the correct size.")
    size = int(input("What is your cat's size (1-10)? "))

if size <= 3:
    for stat in stats:
        stats[stat] = 2
else:
    for stat, change in size_changes[size].items():
        stats[stat] += change
print(" ")
print("Your current stats are:")
print("STATS:", stats)

stat_log = []
starting_stats = stats.copy()

if size > 3:
    taken = {stat: 0 for stat in stats}

    move = input("Would you like to move points between stats? Y/N. ").upper().strip()
    while move == "Y":
        take_from = input("Take points from which stat? ").strip().lower()
        give_to = input("Give them to which stat? ").strip().lower()
        amount = int(input("How many points? "))

        if take_from not in stats or give_to not in stats:
            print("That's not a stat name. Valid stats are: vigor, vitality, swiftness, dexterity.")
        elif take_from == give_to:
            print("Please pick two different stats.")
        elif amount < 1:
            print("The amount must be at least 1.")
        elif taken[take_from] + amount > 4:
            print("You can only take up to 4 points from each stat.")
        elif stats[take_from] - amount < 0:
            print("A stat can't go below 0.")
        else:
            stats[take_from] -= amount
            stats[give_to] += amount
            taken[take_from] += amount
            print("STATS:", stats)
            move = input("Move more points? Y/N. ").upper().strip()

print("FINAL STATS:", stats)
print()
print("STAT LOG")
if len(stat_log) == 0:
    print("No points were moved.")
else:
    for entry in stat_log:
        print(entry)

print()
print("STARTING STATS:", starting_stats)
print("FINAL STATS:", stats)
print()
print("NET CHANGES")
for stat in stats:
    change = stats[stat] - starting_stats[stat]
    print(f"{stat}: {starting_stats[stat]} -> {stats[stat]} ({change:+})")
