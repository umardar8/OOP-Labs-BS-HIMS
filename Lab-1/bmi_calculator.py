# BMI = Body Mass Index
# It uses weight and height of patient to check their fat condition (overweight, underweight, healthy)
# Formula: BMI = Weight(kg) / Height(m) * Height(m)

patient_height_m = 1.75
patient_weight_kg = 75

patient_bmi = patient_weight_kg / (patient_height_m * patient_height_m)

print("Height of Patient: ", patient_height_m)
print("Weight of Patient: ", patient_weight_kg)
print(f"Patient BMI: {patient_bmi:.2f}")