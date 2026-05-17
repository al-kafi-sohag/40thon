# =========================
# 1. Simple BMI Calculator
# =========================

print("..........Simple BMI Calculator..........")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")