import random
action = input("Enter attack: ")
time = 1



#STATS
#  Health = how much it takes away from enemy, power = how much power/energy you need to do that action.
attack_stats = {"Power": 200, "Energy": 100, "Health": 475, "Rest": 50}
enemy1_stats = {"Health": 800, "Power": 250, "Energy": 500, "Rest": 25}
dwarf_stats = {"Health": 150, "Power": 75}
wizard_stats = {"Health": 450, "Power": 225}
restlimit = 150
powerlimit = 250
enemy1 = "dragon"

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


# attack
if action == "attack" and healthcheck(attack_stats["Health"]) and healthcheck(enemy1_stats["Health"]):
    print("You are fighting a... " + enemy1 + "!")
    print(enemy1_stats)

    while healthcheck(attack_stats["Health"]) and healthcheck(enemy1_stats["Health"]):
        attackOption = input("\nEnter 1 to attack, 2 to rest, 3 to train ")

        # --------- ATTACKING -----------
        if attackOption == "1":

            attack(attack_stats, enemy1_stats, "dragon")

            if attack_stats["Health"] <= 0:
                print("\nUnfortunately, you fell victim to the dragon. Game over.")
            elif enemy1_stats["Health"] <= 0:
                print("Your bravery and battle skills have brought you to a victory!")
                restlimit = restlimit + 150
                powerlimit = powerlimit + 150
        # ---------- RESTING ------------
        # fixme resting for the dragon - everytime I rest the dragon will increase health by its value
        elif attackOption == "2" and attack_stats["Health"] <= restlimit:
            rest_generator = random.uniform(0.5, 2)
            new_rest = rest_generator * attack_stats["Rest"]
            new_rest = round(new_rest)
            print("You decide to exit the battle and rest up.")
            resting = input("\n1 to keep resting, 2 to start fighting ")
            if resting == "1":
                print("Your health went up by " + str(new_rest))
                attack_stats["Health"] = attack_stats["Health"] + new_rest

                print("Your health: " + str(attack_stats["Health"]))
                print("Enemies' health: " + str(enemy1_stats["Health"]) + "\n")

                e1_rest_generator = random.uniform(.5, 2)
                e1_rest = e1_rest_generator * enemy1_stats["Rest"]
                e1_rest = round(e1_rest)
                enemy1_stats["Health"] = enemy1_stats["Health"] + e1_rest

            elif resting == "2":
                print("Back into the battefield you go!")

                print("Your health: " + str(attack_stats["Health"]))
                print("Enemies' health: " + str(enemy1_stats["Health"]) + "\n")

        elif attackOption == "2" and attack_stats["Health"] > 150:
            print("You don't need to rest now, tough it out and get back into the battlefield.")

        # ------ TRAINING --------
        elif attackOption == "3" and attack_stats["Power"] < powerlimit:
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
