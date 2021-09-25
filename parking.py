from collections import defaultdict
import heapq

class Vehicle:
    def __init__(self, registration_number, driver_age):
        self.registration_number = registration_number
        self.driver_age = driver_age

class ParkingLot:
    def __init__(self):
        self.slots_available = []
        self.registration_number_and_slot_dictionary = {}
        self.slot_and_vehicle_dictionary = {}
        self.driver_age_and_registration_number_dictionary = defaultdict(list)

    #Creating the parking lot with specified number of slots
    def Create_parking_lot(self, number_of_slots):
        print("Created parking of " + str(number_of_slots) + " slots")
        for i in range(1, number_of_slots + 1):
            heapq.heappush(self.slots_available, i)
        return True

    #finding the nearest parking slot available
    def find_nearest_parking_slot(self):
        if self.slots_available:
            return heapq.heappop(self.slots_available)
        else:
            return None
    
    #Parking the vehicle
    def Park(self, vehicle):
        slot_number = self.find_nearest_parking_slot()
        #if no slot is available to park
        if slot_number == None:
            print("No parking space available. Sorry for the inconvenience!")
            return 
        print("Car with vehicle registration number \"" + vehicle.registration_number + "\" has been parked at slot number " + str(slot_number))
        self.slot_and_vehicle_dictionary[slot_number] = vehicle
        self.registration_number_and_slot_dictionary[vehicle.registration_number] = slot_number
        self.driver_age_and_registration_number_dictionary[vehicle.driver_age].append(vehicle.registration_number)
        return slot_number

    #finding the slot numbers of all slots where cars of drivers of a particular age are parked
    def Slot_numbers_for_driver_of_age(self, driver_age):
        all_registration_numbers = self.driver_age_and_registration_number_dictionary[driver_age]
        all_slots = []
        for x in all_registration_numbers:
            all_slots.append(self.registration_number_and_slot_dictionary[x])
        #if no slot exists where driver's age is as required
        if all_slots == []:
            print("No slots present where driver's age is " + driver_age)
        else:
            print(", ".join(map(str, all_slots)))
        return all_slots
    
    #finding slot number in which a car with a given vehicle registration plate is parked.
    def Slot_number_for_car_with_number(self, vehicle_registration_number):
        Slot = None
        if vehicle_registration_number in self.registration_number_and_slot_dictionary:
            Slot = self.registration_number_and_slot_dictionary[vehicle_registration_number]
            print(Slot)
            return Slot 
        #if there is no slot present with the required registration number
        else:
            print("No slot found with given registration number")
    
    #finding vehicle Registration numbers for all cars which are parked by the driver of a certain age
    def Vehicle_registration_number_for_driver_of_age(self, driver_age):
        all_registration_numbers = self.driver_age_and_registration_number_dictionary[driver_age]
        #if there is no car present where driver's age is as required
        if all_registration_numbers == []:
            print("No vehicle present where driver's age is " + driver_age)
        else:
            print(", ".join(all_registration_numbers))
        return self.driver_age_and_registration_number_dictionary[driver_age]

    #emptying the slot after a car leaves and marking it available to park 
    def Leave(self, slot_number):
        flag = None
        #finding registration number of the vehicle parked on the given slot
        for registration_number, slot in self.registration_number_and_slot_dictionary.items():
            if slot == slot_number:
                flag = registration_number
        #if any vehicle is found to be parked at the given slot 
        if flag:
            heapq.heappush(self.slots_available, slot_number)
            del self.registration_number_and_slot_dictionary[flag]
            vehicleLeft = self.slot_and_vehicle_dictionary[slot_number]
            self.driver_age_and_registration_number_dictionary[vehicleLeft.driver_age].remove(flag)
            del self.slot_and_vehicle_dictionary[slot_number]
            print("Slot number " + str(slot_number) + " vacated, the car with vehicle registration number \"" + vehicleLeft.registration_number +"\" left the space, the driver of the car was of age " + vehicleLeft.driver_age)
            return True
        #if the slot is already empty
        else:
            print("There is no vehicle parked at this slot.")
            return False

