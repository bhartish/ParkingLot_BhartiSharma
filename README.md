<h1>Parking Lot </h1><br>
<h2>Submitted by Bharti Sharma</h2>

<h2>Problem Statement</h2>
We own a parking lot that can hold up to ‘n’ cars at any given point in time. Each slot is given a number starting at one increasing with increasing distance from the entry point in steps of one. We want to create an automated ticketing system that allows our customers to use our parking lot without human intervention.
When a car enters the parking lot, we want to have a ticket issued to the driver. The ticket issuing process includes:- 
<br><br>
1. We are taking note of the number written on the vehicle registration plate and the age of the driver of the car.
<br>
2. And we are allocating an available parking slot to the car before actually handing over a ticket to the driver (we assume that our customers are kind enough to always park in the slots allocated to them).
<br><br>

The customer should be allocated a parking slot that is nearest to the entry. At the exit, the customer returns the ticket, marking the slot they were using as being available.
Due to government regulation, the system should provide us with the ability to find out:-

    -> Vehicle Registration numbers for all cars which are parked by the driver of a certain age.
    -> Slot number in which a car with a given vehicle registration plate is parked. 
    -> Slot numbers of all slots where cars of drivers of a particular age are parked.

We get the input by reading input.txt directly.The file will contain a set of commands separated by a newline, we need to execute the commands in order and produce output.
<hr>

There are three files present :<br>
    1. main.py : Input is read in this file, and each command is processed here.<br>
    2. parking.py : All the classes and their methods are defined in this file.<br>
    3. input.txt : This text file contains input as set of commands seperated by a new line.<br>
<br><br>
I have solved the problem with the help of min heap, as min heap will give us the nearest available slot while parking a car in O(1) time complexity.
Also, I have used three dictionaries which are helping me in maintaining the mapping of:<br>
    1. Registration number and slot number<br>
    2. Slot number and Vehicle<br>
    3. Driver's age and registration number<br>

I have also considered the case if we have not created parking lot and running any other command, so, it will give us a message that "Parking Lot does not exist".

<hr>
<h2>Input:- </h2>


    Create_parking_lot 6
    Park KA-01-HH-1234 driver_age 21
    Park PB-01-HH-1234 driver_age 21
    Slot_numbers_for_driver_of_age 21
    Park PB-01-TG-2341 driver_age 40
    Slot_number_for_car_with_number PB-01-HH-1234
    Leave 2
    Park HR-29-TG-3098 driver_age 39
    Vehicle_registration_number_for_driver_of_age 18
    
<h2>Output:- </h2><br>

![image](https://user-images.githubusercontent.com/52272286/134781083-3cae3889-4ca6-491e-844a-663d794d39c8.png)





