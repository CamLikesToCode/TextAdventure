import random
action = input("Enter attack/rest/train")
time = 1

#STATS
#  Health = how much it takes away from enemy, power = how much power/energy you need to do that action.
attack_stats = {"Power": 200, "Energy": 100, "Health": 300}
enemy1_stats = {"Health": 1000, "Power": 250, "Energy": 500}
enemy1 = "dragon"

#Attack
if action == "attack" and attack_stats["Health"] != 0 or enemy1_stats["Health"] != 0:
    print("You are fighting a... " + enemy1 + "!")
    print(enemy1_stats)
    while attack_stats["Health"] > 0 and enemy1_stats["Health"] > 0:
        attack = input("\nEnter 1 to attack, 2 to rest")
        #ATTACKING
        if attack == "1":
            # fixme Check to see if health is 0
            # critical_hits = random.randint(1, 2)

            powerGenerator = random.uniform(0.5, 2)
            newPower = powerGenerator * attack_stats["Power"]
            newPower = round(newPower)
            print("The dragon suffers a " + str(newPower) + " health blow!")


            enemy1_stats["Health"] = enemy1_stats["Health"] - newPower
            # fixme Health calculations for the dragon
            print("The dragon comes back with a ######250###### health hit!!")
            attack_stats["Health"] = attack_stats["Health"] - enemy1_stats["Power"]

            # Check to see if health is 0 or below
            if attack_stats["Health"] <= 0:
                print("\nUnfortunately, you fell victim to the dragon. Game over.")
            elif enemy1_stats["Health"] <= 0:
                print("Your bravery and battle skills have brought you to a victory!")
        #resting
        elif attack == "2":
            print("You decide to exit the battle and rest up.")
            resting = input("\n1 to keep resting, 2 to start fighting")
            if resting == "1":
                print("Your health went up by 50")
                attack_stats["Health"] = attack_stats["Health"] + 50
            elif resting == "2":
                print("Back into the battefield you go!")
