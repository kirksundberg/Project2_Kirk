print("===== PLATFORM ADVENTURE =====")
levels = [1, 2, 3, 4, 5]
coins = [5, 8, 3, 10, 7]
enemies = [2, 4, 1, 5, 3]
power_ups = ["Mushroom", "Star", "Flower", "Mushroom", "Star"]

for i in range(0,5):
    print(f"Level: {levels[i]}\nCoins: {coins[i]}\nEnemies: {enemies[i]}\nPower Up: {power_ups[i]}\n")

print("\n===== PLAYER INFORMATION =====")

player_name = "Hero"
lives = 3
score = 0
total_coins = 0

print(f"Player: {player_name}\nLives: {lives}\nScore: {score}\nTotal Coins: {total_coins}")

print("\n===== LEVEL SCORES =====")
total_score = 0
level_scores = []

for i in range(0,5):
    score = (coins[i] * 10 + enemies[i] * -5)
    if power_ups[i] == "Star":
        score = score + 25
    total_score += score
    level_scores.append(score)
    print(f"Level {i+1} Score: {score}")

print("\n===== ADVENTURE ACTIONS =====")

actions = [0,1,0,2,1]
action_results = []

for i in range(0,5):
    if actions[i] == 2:
        action_results.append("Use Power-Up")
        print(f"Level {levels[i]}: {action_results[i]}")
    elif actions[i] == 1:
        action_results.append("Fight Enemies")
        print(f"Level {levels[i]}: {action_results[i]}")
    else:
        action_results.append("Collect Coins")
        print(f"Level {levels[i]}: {action_results[i]}")

print("\n===== LIFE HISTORY =====")

life_history = []

for i in range(0,5):
    if enemies[i] >= 4:
        lives = lives - 1
        if power_ups[i] == "Star":
            lives = lives + 1
        life_history.append(lives)
    elif enemies[i] < 4:
        life_history.append(lives)
    else:
        life_history.append(lives)

for i in range(0,5):
   print(f"After Level {i + 1}: {life_history[i]} lives")

print("\n===== COIN COLLECTION =====")

bonus_coin_levels = [coin for coin in coins if coin >= 7]
for coin in coins:
    total_coins += coin

print(f"Coins collected: {total_coins}")
print(f"Levels with 7 or more coins: {bonus_coin_levels}")

print("\n===== POWER-UP INVENTORY =====")


inventory = ["Mushroom", "Star", "Flower"]
used_powerups = ["Mushroom", "Star"]
print(f"Starting Inventory: {inventory}")

for item in used_powerups:
    if item == "Mushroom":
        inventory.pop(0)
    elif item == "Star":
        inventory.pop(-2)
    else:
        inventory.pop(1)

print(f"Used Power-Ups: {used_powerups}")
print(f"Remaining Inventory: {inventory}")

print("\n===== LEVEL ANALYSIS =====")

print(f"Total Coins: {total_coins}")
print(f"Most Coins in One Level: {max(coins)}")
print(f"Fewest Coins in One Level: {min(coins)}")
print(f"Average Coins per Level: {(sum(coins))/len(levels)}")
print(f"Total Enemies: {sum(enemies)}")
print(f"Most Enemies in One Level: {max(enemies)}")

print("\n===== HIGH SCORES =====")

high_scores = [num for num in level_scores if num >= 50]
print(f"Scores of 50 or Higher: {high_scores}")

print("\n===== SCORE HISTORY =====")
score_over_time = 0
score_history = []

for num in level_scores:
    score_over_time += num
    score_history.append(score_over_time)

for i in range(0,5):
   print(f"After Level {i + 1}: {score_history[i]}")

print(f"First Two Scores: {[score_history[0],score_history[1]]}")
print(f"Last Two Scores: {[score_history[-2],score_history[-1]]}")

print(f"===== FINAL STATUS =====")
if lives == 0:
    print("Game Over")
elif total_score >= 250:
    print("Adventure Champion")
elif total_score >= 150:
    print("Great Adventure")
else:
    print("Keep Practicing")

print("\n===== ADVENTURE RANKING =====")
print(f"Final Score: {total_score}")
print(f"Final Lives: {lives}")
print(f"Rank: Legend")