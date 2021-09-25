#this file reads the input from the text file and checks each command 
from parking import ParkingLot, Vehicle

does_parking_slot_exist = False
parking_lot = ParkingLot()

#function checks the input command and does the required operations
def command_process(command):
    #command is given in one line, so, we will convert string to list on the basis of space
    command_info = command.strip().split(" ")
    task = command_info[0]

    if task == "Create_parking_lot":
        if (len(command_info) == 2) and (command_info[1].isdigit() is True):
            number_of_slots = int(command_info[1])
            parking_lot.Create_parking_lot(number_of_slots)
            global does_parking_slot_exist
            does_parking_slot_exist = True
        else:
            print("Number of slots(in digits) required")
    
    #if parking lot exists
    elif does_parking_slot_exist == True:
        if task == "Park":
            if (len(command_info) == 4) and (command_info[3].isdigit() is True):
                vehicle_registration_number = command_info[1]
                driver_age = command_info[3]
                vehicle = Vehicle(vehicle_registration_number, driver_age)
                parking_lot.Park(vehicle)
            else:
                print("Registration number and driver's age(in digits) required")
    
        elif task == "Slot_numbers_for_driver_of_age":
            if (len(command_info) == 2) and (command_info[1].isdigit() is True):
                driver_age = command_info[1]
                parking_lot.Slot_numbers_for_driver_of_age(driver_age)
            else:
                print("Driver's age(in digits) required")
        
        elif task == "Slot_number_for_car_with_number":
            if (len(command_info) == 2):
                vehicle_registration_number = command_info[1]
                parking_lot.Slot_number_for_car_with_number(vehicle_registration_number)
            else:
                print("Registration number required")
        
        elif task == "Vehicle_registration_number_for_driver_of_age":
            if (len(command_info) == 2) and (command_info[1].isdigit() is True):
                driver_age = command_info[1]
                parking_lot.Vehicle_registration_number_for_driver_of_age(driver_age)
            else:
                print("Driver's age(in digits) required")
        
        elif task == "Leave":
            if (len(command_info) == 2) and (command_info[1].isdigit() is True):
                slot_number = int(command_info[1])
                parking_lot.Leave(slot_number)
            else:
                print("Slot number(in digits) required")
        
        else:
            print("Invalid Command")
    
    #if parking lot is not present
    else:
        print("Parking Lot does not exist")
        

#reading input from text file
with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    command_process(line)
    