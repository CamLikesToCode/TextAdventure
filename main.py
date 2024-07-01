import random
action = input("Enter attack: ")
time = 1

# STATS
attack_stats = {"Power": 200, "Energy": 100, "Health": 475, "Rest": 50}

zombie_stats = {"Health": 500, "Power": 125, "Rest": 50, "Name": "zombie", "Img":r"zombie.txt"}
enemy1_stats = {"Health": 600, "Power": 250, "Energy": 500, "Rest": 10, "Name": "dragon", "Img": r"dragon.txt"}
werewolf_stats = {"Health": 700, "Power": 150, "Rest": 50, "Name": "werewolf", "Img": r"ww.txt"}

dwarf_stats = {"Health": 150, "Power": 75}
wizard_stats = {"Health": 450, "Power": 225}
restlimit = 350
powerlimit = 300
enemy1 = "dragon"

enemieslist = [enemy1_stats, zombie_stats, werewolf_stats]
enemynum = random.randint(0,2)
enemy = enemieslist[enemynum]



'''
if enemynum == 0: #dragon
    enemytxt = open(r"dragon.txt", "r")
if enemynum == 1: #zombie
    enemytxt = open(r"zombie.txt", "r")
if enemynum == 2: #werewolf
    enemytxt = open(r"ww.txt", "r")
'''

# attack function
def attack(stats, enemystats, enemyname):

    powerGenerator = random.uniform(0.5, 2)
    newPower = powerGenerator * stats["Power"]
    newPower = round(newPower)
    print("The " + enemyname + " suffers a " + str(newPower) + " health blow!")
    enemystats["Health"] = enemystats["Health"] - newPower

    print("Your health: " + str(stats["Health"]))
    print("Enemies' health: " + str(enemystats["Health"]) + "\n")

    if healthcheck(enemystats["Health"]):
        enemyPowerGenerator = random.uniform(.5, 2)
        eNewPower = enemyPowerGenerator * enemystats["Power"]
        eNewPower = round(eNewPower)

        print("The " + enemyname + " comes back with a " + str(eNewPower) + " health hit!!")
        stats["Health"] = stats["Health"] - eNewPower

        print("Your health: " + str(stats["Health"]))
        print("Enemies' health: " + str(enemystats["Health"]) + "\n")

# health checker function
def healthcheck(health):
    return health > 0

# training function
def train():
    if attack_stats["Power"] < powerlimit:
        print("You have decided to exit the fight and train.")
        print("To gain power, you fight other small enemies, you cannot rest.")

        if attack_stats["Power"] <= 300:
            attack(attack_stats, dwarf_stats, "dwarf")

            if healthcheck(attack_stats['Health']) and not healthcheck(dwarf_stats['Health']):
                print("You defeated your training enemy! Your power increased by 100")
                attack_stats['Power'] = attack_stats["Power"] + 100
                dwarf_stats["Health"] = 150

        elif attack_stats["Power"] > 300:
            attack(attack_stats, wizard_stats, "wizard")

            if healthcheck(attack_stats['Health']) and not healthcheck(wizard_stats['Health']):
                print("You defeated your training enemy! Your power increased by 150")
                attack_stats['Power'] = attack_stats["Power"] + 150
                wizard_stats["Health"] = 450


    if attack_stats["Power"] >= powerlimit:
        print("Your power is too high to train.")

def rest(enemystats):
    if attack_stats["Health"] <= restlimit:
        rest_generator = random.uniform(0.5, 2)
        new_rest = rest_generator * attack_stats["Rest"]
        new_rest = round(new_rest)
        print("You decide to exit the battle and rest up.")
        resting = input("\n1 to start fighting, 2 to rest")

        if resting == "2":
            print("Your health went up by " + str(new_rest))
            attack_stats["Health"] = attack_stats["Health"] + new_rest

            print("Your health: " + str(attack_stats["Health"]))
            print("Enemies' health: " + str(enemystats["Health"]) + "\n")

            enemyrestgen = random.uniform(.5, 2)
            enemyrest = enemyrestgen * enemystats["Rest"]
            enemyrest = round(enemyrest)
            enemystats["Health"] = enemystats["Health"] + enemyrest

        elif resting == "1":
            print("Back into the battefield you go!")

            print("Your health: " + str(attack_stats["Health"]))
            print("Enemies' health: " + str(enemystats["Health"]) + "\n")

    elif attack_stats["Health"] > restlimit:
        print("You don't need to rest now, tough it out and get back into the battlefield.")

# attack
while action == "attack" and healthcheck(attack_stats["Health"]) and (healthcheck(enemy1_stats["Health"])
                                                                   or healthcheck(zombie_stats["Health"]) or healthcheck(werewolf_stats["Health"])):

    if healthcheck(enemy["Health"]):
        print("You are fighting a..." + enemy["Name"])
        print(enemy)
        print(open(enemy["Img"], "r").read())



        while healthcheck(attack_stats["Health"]) and healthcheck(enemy["Health"]):
            attackOption = input("\nEnter 1 to attack, 2 to rest, 3 to train ")

            if attackOption == "1":
                attack(attack_stats, enemy, enemy["Name"])

                if attack_stats["Health"] <= 0:
                    print("\nUnfortunately, you fell victim to the " + enemy["Name"] + ". Game over.")

                elif enemy["Health"] <= 0:
                    restlimit = restlimit + 150
                    powerlimit = powerlimit + 150
                    enemieslist.pop(enemynum)
                    if len(enemieslist) == 0:
                        print("You beat all of the toughest enemies! For now...")
                    else:
                        enemynum = random.randint(0, len(enemieslist) - 1)
                        enemy = enemieslist[enemynum]
                        print("Your bravery and battle skills have brought you to a victory!")
                    break

            # rest
            elif attackOption == "2":
                rest(enemy)

            # train
            elif attackOption == "3":
                train()

'''
    #ZOMBIE
    elif healthcheck(zombie_stats["Health"]):
                print("You are fighting a... zombie!")
                print(zombie_stats)

                while healthcheck(attack_stats["Health"]) and healthcheck(zombie_stats["Health"]):
                    attackOption = input("\nEnter 1 to attack, 2 to rest, 3 to train ")
                    # fixme add something for if an attack option will not happen.
                    # --------- ATTACKING -----------
                    if attackOption == "1":

                        attack(attack_stats, zombie_stats, "zombie")

                        if attack_stats["Health"] <= 0:
                            print("\nUnfortunately, you fell victim to the zombie. Game over.")
                        elif zombie_stats["Health"] <= 0:
                            print("Your bravery and battle skills have brought you to a victory!")
                            restlimit = restlimit + 150
                            powerlimit = powerlimit + 150
                            # train
                    if attackOption == "3":
                        train()

                    # rest
                    if attackOption == "2":
                        rest(zombie_stats)
'''
