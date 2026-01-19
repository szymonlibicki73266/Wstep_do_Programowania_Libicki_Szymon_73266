import random

lucky_number = random.randint(1, 100)
print(f"Szczęśliwy numerek grupy: {lucky_number}")

birth_years = [1995, 1996, 1998, 2000, 1997, 1999, 2001]
lucky_year = random.choice(birth_years)
print(f"Szczęśliwy rocznik: {lucky_year}")

lottery_numbers = random.sample(range(1, 50), 6)
print(f"Wylosowane liczby w Dużym Lotku: {sorted(lottery_numbers)}")