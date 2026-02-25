def calculate_pediatric_dosage(patient_age, adult_dose_mg):
    # Logic: Using Young's Rule - Age / (Age + 12)
    child_dose = (patient_age / (patient_age + 12)) * adult_dose_mg
    # Output: Send the result back to where the function was called
    return round(child_dose, 2)

child_age = 6
std_adult_dose = 500  # mg

recommended_dose = calculate_pediatric_dosage(child_age, std_adult_dose)

print(f"Pediatric Dosage Calculator")
print(f"---------------------------")
print(f"Patient Age: {child_age} years")
print(f"Adult Dose:  {std_adult_dose} mg")
print(f"Result:      {recommended_dose} mg")