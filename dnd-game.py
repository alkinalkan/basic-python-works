import random

def roll_dice(sides):
    return random.randint(1, sides)

def attack(attack_value, defense_value):
    damage = roll_dice(attack_value)
    block = roll_dice(defense_value)
    if damage > block:
        return damage - block
    else:
        return 0

def play_game():
    player_health = 100
    enemy_health = 100

    print("Welcome to the Dungeon!")
    player_name = input("Enter your character's name: ")

    print(f"{player_name}, prepare to battle!")

    while player_health > 0 and enemy_health > 0:
        print(f"\n{player_name}'s Health: {player_health}")
        print(f"Enemy's Health: {enemy_health}\n")

        player_attack = int(input("Enter your attack value (1-20): "))
        player_defense = int(input("Enter your defense value (1-20): "))

        enemy_attack = roll_dice(20)
        enemy_defense = roll_dice(20)

        player_damage = attack(player_attack, enemy_defense)
        enemy_damage = attack(enemy_attack, player_defense)

        player_health -= enemy_damage
        enemy_health -= player_damage

        print(f"\n{player_name} deals {player_damage} damage to the enemy!")
        print(f"The enemy deals {enemy_damage} damage to {player_name}!")

    if player_health <= 0:
        print("\nYou were defeated. Game over!")
    else:
        print("\nCongratulations! You defeated the enemy!")

play_game()
