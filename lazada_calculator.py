# Points to Ringgit calculator

# Every 45 points = 40 coins
# Every 100 coins = 1.00 ringgit

points = int(input("Enter points: "))
coins = points / 1.125
coins_ringgit = coins / 100

print(f"your points is worth {coins_ringgit:.2f}")


