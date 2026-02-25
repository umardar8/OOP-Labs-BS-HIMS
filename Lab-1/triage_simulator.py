# Triage system is a method for prioritizing and sorting individuals cases or IT issues.

# Our triage system:
# 1. Critical = Heart_rate > 140 or SpO2 < 90%
# 2. Urgent = Heart_rate > 100 or SpO2 < 94%
# 3. Stable = Otherwise 

heart_rate = 110
oxygen_saturation = 92
triage_category = ''

if heart_rate > 140 or oxygen_saturation < 90:
    triage_category = 'Critical'
elif heart_rate > 100 or oxygen_saturation < 94:
    triage_category = 'Urgent'
else:
    triage_category = 'Stable'

print("------Patient BMI Calculator-----")
print(f"Patient Heart Rate: {heart_rate}")
print(f"Patient Oxygen Saturation: {oxygen_saturation}")
print(f"Assigned category: {triage_category}")