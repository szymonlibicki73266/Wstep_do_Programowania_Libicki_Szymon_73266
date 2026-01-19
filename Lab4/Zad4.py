def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)
    print(f"Twoje BMI wynosi: {bmi:.2f}")
    if bmi < 18.5:
        print("Masz niedowagę.")
    elif 18.5 <= bmi < 25:
        print("Masz prawidłową wagę.")
    elif 25 <= bmi < 30:
        print("Masz nadwagę.")
    else:
        print("Masz otyłość.")