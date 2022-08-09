
 # Import Necessary Package

 from dronekit import connect, VehicleMode, LocationGlobalRelative
 import time
 def basicTakeOff(altitude):

    """
     Inputs:
        1. altitude             - Takeoff Altitude
    """
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    time.sleep(2)
    vehicle.simple_takeoff(altitude)

    while true:
        print("Reached Height = ", vehicle.location.global_relative_frame.alt)

        if vehicle.location.global_relative_frame.alt>=(altitude - 1.5): 
            break
        time.sleep(1)



    #Connecting the vehicle
    vehicle = connect ('udpin:127.0.0.1.14551', baud=115200)

    #Takeoff the vehicle
    takeOffAltitude = 10
    basicTakeOff(takeOffAltitude)
    print("Reached:",takeOffAltitude, "m")

    #Landing the Vehicle
    vehicle.mode=VehicleMode('LAND')
    print("Landing the Vehicle)
    time.sleep(1)

    print("exiting the code)
    time.sleep(1)
