import random


print("")
print("Trip Generator")
print("")

def dayTrips():
    destinations = ["Sacramento, California", "Denver, Colorado", "Alberta, Canada", "Myrtle Beach, South Carolina"]
    restaurant = ["Texas RoadHouse", "Applebees", "McDonalds", "Dmoninoes"]
    transportation = ["Horse Back Riding - slow but you'll get there. ", "Teleport Portal - Fastest but expensive.", "Hitch Hiking - Longest but cheapest.", "Riding T-Rex - Caution Might Get EATEN!"]
    entertainments = ["Music festival", "Skiing/snowboarding", "Beach", "Casino"]

    des = random_place(destinations)
    res = random_place(restaurant)
    trans = random_place(transportation)
    enter = random_place(entertainments)
    
    comfirmation = True
    while comfirmation == True:

        destin = "Destination: " + des
        restaur = "Restaurant: " + res
        transpor = "Transportation: " + trans
        entertain = "Entertainments: " + enter
        trip = destin, restaur, transpor, entertain

        comfirm(trip)
        
        print("Will this trip be your satisfaction? Yes/No:")
        user_input = input("")

        if user_input == "No":
            print("Which option you're not satisfy?")
            input_remove = input("")
            if input_remove == "Destination":
                removing(destinations, des)
                des = random_place(destinations)
            elif input_remove == "Restaurant":
                removing(restaurant, res)
                res = random_place(restaurant)
            elif input_remove == "Transportation":
                removing(transportation, trans)
                trans = random_place(transportation)
            elif input_remove == "Entertainment":
                removing(entertainments, enter)
                enter = random_place(entertainments)
        elif user_input == "Yes":
            print("")
            print("Thank You! Your Crazy Trip has been booked!")
            print("")
            comfirm(trip)
            print("")
            comfirmation = False
    

def random_place(selected):
    random_places = random.choice(selected)
    return random_places

def removing(what_list_its_in, rand):
    condion = True
    while condion == True:
        being_remove = what_list_its_in.remove(rand)
        what_list_its_in = random_place(rand)
        return being_remove

def comfirm(satisfy_list):
    for all_list in satisfy_list:
        print(all_list)



dayTrips()

