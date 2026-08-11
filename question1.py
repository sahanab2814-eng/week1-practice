hours = int(input("Enter parking hours: "))

if hours <= 2:
    rate = 30
elif hours >= 3 and hours <= 5:
    rate = 25
else:  
    rate = 20

parking_charge = hours * rate


if parking_charge > 150:
    service_charge = 20
else:
    service_charge = 0

final_amount = parking_charge + service_charge

print("Parking Charge: ₹", parking_charge)
print("Service Charge: ₹", service_charge)
print("Final Amount: ₹", final_amount)