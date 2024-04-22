import random
action = input("Enter attack: ")
time = 1



#STATS
#  Health = how much it takes away from enemy, power = how much power/energy you need to do that action.
attack_stats = {"Power": 200, "Energy": 100, "Health": 475, "Rest": 50}
enemy1_stats = {"Health": 800, "Power": 250, "Energy": 500, "Rest": 25}
dwarf_stats = {"Health": 150, "Power": 75}
enemy1 = "dragon"


#Attack
if action == "attack" and attack_stats["Health"] != 0 or enemy1_stats["Health"] != 0:
    print("You are fighting a... " + enemy1 + "!")
    print(enemy1_stats)
    while attack_stats["Health"] > 0 and enemy1_stats["Health"] > 0:
        attack = input("\nEnter 1 to attack, 2 to rest, 3 to train")

        # --------- ATTACKING -----------
        if attack == "1":
            # critical_hits = random.randint(1, 2)
            powerGenerator = random.uniform(0.5, 2)
            newPower = powerGenerator * attack_stats["Power"]
            newPower = round(newPower)
            print("The dragon suffers a " + str(newPower) + " health blow!")
            enemy1_stats["Health"] = enemy1_stats["Health"] - newPower

            print("Your health: " + str(attack_stats["Health"]))
            print("Enemies' health: " + str(enemy1_stats["Health"]) + "\n")

            enemy1PowerGenerator = random.uniform(.5, 2)
            eNewPower = enemy1PowerGenerator * enemy1_stats["Power"]
            eNewPower = round(eNewPower)
            print("The dragon comes back with a " + str(eNewPower) + " health hit!!")
            attack_stats["Health"] = attack_stats["Health"] - eNewPower

            print("Your health: " + str(attack_stats["Health"]))
            print("Enemies' health: " + str(enemy1_stats["Health"]) + "\n")

            # Check to see if health is 0 or below
            if attack_stats["Health"] <= 0:
                print("\nUnfortunately, you fell victim to the dragon. Game over.")
            elif enemy1_stats["Health"] <= 0:
                print("Your bravery and battle skills have brought you to a victory!")

        # ---------- RESTING ------------
        # fixme resting for the dragon - everytime I rest the dragon will increase health by its value
        elif attack == "2" and attack_stats["Health"] <= 150:
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

        elif attack == "2" and attack_stats["Health"] > 150:
            print("You don't need to rest now, tough it out and get back into the battlefield.")

        # ------ TRAINING --------
        elif attack == "3":
            print("You have decided to exit the fight and train.")
            print("To gain power, you fight other small enemies, you cannot rest.")

            if attack_stats["Power"] <= 300:


                # Me
                powerGenerator = random.uniform(0.5, 1)
                newPower = powerGenerator * attack_stats["Power"]
                newPower = round(newPower)

                # Enemy
                train_enemy = random.uniform(1, 2)
                te_new_power = train_enemy * dwarf_stats["Power"]
                te_new_power = round(te_new_power)

                print("\nYou will be fighting a dwarf.")

                if dwarf_stats["Health"] != 0 or attack_stats != 0:
                    print("You attack the dwarf using " + str(newPower) + " power!")

                    dwarf_stats["Health"] = dwarf_stats["Health"] - newPower

                    print("\nYour health: " + str(attack_stats["Health"]))
                    print("Dwarf's health: " + str(dwarf_stats["Health"]))

                    print("\nThe dwarf fights back with a " + str(te_new_power) + " hit!!")

                    print("\nYour health: " + str(attack_stats["Health"]))
                    print("Dwarf's health: " + str(dwarf_stats["Health"]))

