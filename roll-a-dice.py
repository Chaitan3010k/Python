
import random
response = "y"
while(response == "y"):
    yes_or_no = input("Press Y to Roll the dice again and press N to exit: ")
    response = yes_or_no.lower()
    if(response == "y"):
        random_number = random.randint(1, 6)
        if(random_number == 1):
            print("[- - -]")
            print("[     ]")
            print("[  1  ]")
            print("[     ]")
            print("[- - -]")
        if(random_number == 2):
            print("[- - -]")
            print("[     ]")
            print("[2   2]")
            print("[     ]")
            print("[- - -]")
        if(random_number == 3):
            print("[- - -]")
            print("[3    ]")
            print("[  3  ]")
            print("[    3]")
            print("[- - -]")
        if(random_number == 4):
            print("[- - -]")
            print("[4   4]")
            print("[     ]")
            print("[4   4]")
            print("[- - -]")
        if(random_number == 5):
            print("[- - -]")
            print("[5   5]")
            print("[  5  ]")
            print("[5   5]")
            print("[- - -]")
        if(random_number == 6):
            print("[- - -]")
            print("[6   6]")
            print("[6   6]")
            print("[6   6]")
            print("[- - -]")                    
    else:
        print("The End :)")    
