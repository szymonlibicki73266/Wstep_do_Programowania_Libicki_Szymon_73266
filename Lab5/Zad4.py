from datetime import datetime, timedelta

# Data ostatnich laboratoriów
last_lab_date = datetime(2023, 10, 1)  # Przykładowa data
# Data kolokwium
exam_date = datetime(2023, 12, 15)  # Przykładowa data

# Obliczanie dni od ostatnich laboratoriów
days_since_last_lab = (datetime.now() - last_lab_date).days

# Obliczanie dni do kolokwium
days_until_exam = (exam_date - datetime.now()).days

# Wyświetlanie wyników
print(f"Ilość dni od ostatnich laboratoriów: {days_since_last_lab} dni")
print(f"Ilość dni do kolokwium: {days_until_exam} dni")