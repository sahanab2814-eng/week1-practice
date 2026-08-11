seats = ["Available", "Booked", "Available", "Available",
         "Booked", "Available", "Booked", "Available"]

for i in range(len(seats)):
    print("Seat", i + 1, ":", seats[i])

n = int(input("Enter seat number: "))

if seats[n - 1] == "Available":
    seats[n - 1] = "Booked"
    print("Seat booked successfully.")
else:
    print("Seat is already booked.")

print("Total Seats:", len(seats))
print("Booked Seats:", seats.count("Booked"))
print("Available Seats:", seats.count("Available"))