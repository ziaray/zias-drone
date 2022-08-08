####Dependencies###################

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import socket
import exceptions
import argparse
###Function definitions for mission####
##Function to connect script to drone

def connectMyCopter ():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()

    connection_string = args.connect

    vehicle = connect(connection_string, wait_ready=True)

    return vehicle

##Function to arm the drone and takeoff into the air##
def arm_and_takeoff(aTargetAltitude):2
    while not vehicle.is_armable:
        print ("Waiting for vehicle to become armable")
        time.sleep(1)

        #switch vehicle to GUIDED mode and wait for change
        vehicle.mode = VehicleMode("GUIDED"0
        while vehicle.armed==False:
            print ("Waiting for vehicle to become armed.")
            time.sleep(1)

        #Arm vehicle once GUIDED mode is confirmed
        chicle.armed=True
        while vehicle.armed=True
        while vehicle.armed==False:
            print ("waiting for the vehicle to become armed.")
            time.sleep(1)

        vehicle.simple_takeoff(aTargetAltitude)

        while True:("Current Altitude: kd"vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*.95:
            break
        time.sleep(1)

    print("target altitude reached")
    return None
    
    #### Mission###############################

    vehicle=connectMyCopter()
    print ("About to takeoff..")

    vehicle.mode=VehicleMode("GUIDED"0
    arm_and_takeoff(2)##Tell drone to fly 2 meters in the sky
    vehicle.mode=VehicleMode("LAND") ##Once drone reaches altitude,tell it to land

    time.sleep(2)

    print("End of function")
    print("Arducopter version: s"vehicle.version)

    while True:
        time.sleep(2)

    vehicle.close()
    ###END of script
