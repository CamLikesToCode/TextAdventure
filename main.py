import random
action = input("Enter attack/rest/train")
time = 1


#STATS
#  Health = how much it takes away from enemy, power = how much power/energy you need to do that action.
attack_stats = {"Power": 200, "Energy": 100, "Health": 300, "Rest": 50}
enemy1_stats = {"Health": 1000, "Power": 250, "Energy": 500, "Rest": 25}
enemy1 = "dragon"


#Attack
if action == "attack" and attack_stats["Health"] != 0 or enemy1_stats["Health"] != 0:
    print("You are fighting a... " + enemy1 + "!")
    print(enemy1_stats)
    while attack_stats["Health"] > 0 and enemy1_stats["Health"] > 0:
        attack = input("\nEnter 1 to attack, 2 to rest")
        #ATTACKING
        if attack == "1":
            # critical_hits = random.randint(1, 2)

            powerGenerator = random.uniform(0.5, 2)
            newPower = powerGenerator * attack_stats["Power"]
            newPower = round(newPower)
            print("The dragon suffers a " + str(newPower) + " health blow!")
            enemy1_stats["Health"] = enemy1_stats["Health"] - newPower

            enemy1PowerGenerator = random.uniform(.5, 2)
            eNewPower = enemy1PowerGenerator * enemy1_stats["Power"]
            eNewPower = round(eNewPower)
            print("The dragon comes back with a " + str(eNewPower) + " health hit!!")
            attack_stats["Health"] = attack_stats["Health"] - eNewPower

            # Check to see if health is 0 or below
            if attack_stats["Health"] <= 0:
                print("\nUnfortunately, you fell victim to the dragon. Game over.")
            elif enemy1_stats["Health"] <= 0:
                print("Your bravery and battle skills have brought you to a victory!")

        #resting
        # fixme resting for the dragon - everytime I rest the dragon will increase health by its value
        elif attack == "2" and attack_stats["Health"] <= 150:
            rest_generator = random.uniform(0.5, 2)
            new_rest = rest_generator * attack_stats["Rest"]
            new_rest = round(new_rest)
            print("You decide to exit the battle and rest up.")
            resting = input("\n1 to keep resting, 2 to start fighting")
            if resting == "1":
                print("Your health went up by " + str(new_rest))
                attack_stats["Health"] = attack_stats["Health"] + new_rest

            elif resting == "2":
                print("Back into the battefield you go!")
        elif attack == "2" and attack_stats["Health"] > 150:
            print("You don't need to rest now, tough it out and get back into the battlefield.")
