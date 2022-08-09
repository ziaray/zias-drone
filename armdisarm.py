# Importing necessary Packages
from dronekit import connect, VehicleMode

# Connecting the Vehicle
vehicle = connect('udpin:127.0.0.1:14551', baud=115200)

# Initially Changing the Vehicle to GUIDED mode
vehicle.mode = VehicleMode("GUIDED")

while True:
    armCommand = input()

    if armCommand == "ARM":
    vehicle.armed = True
                      
    if armCommand == "DISARM":
    vehicle.armed = False
