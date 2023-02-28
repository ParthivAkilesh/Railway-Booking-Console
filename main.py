import os
import pickle as pk
from database import DataBase
from book import Book
from cancel import Cancel

if os.path.exists("db.pkl"):
    db = pk.load(open("db.pkl", "rb"))
else:
    db = DataBase()
    # print(db.data)
    
def printTkt(tid, tks):
    
    print("##################################")
    print ("{:^10}".format('Ticket Details'))
    print ("{:^10}".format('------------'))
    # print ("{:<10} {:<10}".format('Ticket', 'Details'))
    # print ("{:<10} {:<10}".format('-------', '-------'))
    print ("{:<10} {:<10}".format('Ticket ID: ', tid if len(tid)!=2 else tid[0]))
    print ("{:<10} {:<10}".format('Seat No.', 'Passenger Name'))
    print ("{:<10} {:<10}".format('--------', '-----'))
    print ("{:<10} {:<10}".format('--------', '-----'))
    for tk in tks:
        print ("{:<10} {:<10}".format(tk[0], tk[1]))
        
        
    # print ("{:<10} {:<10}".format('Ticket', 'Details'))
    # print("Ticket ID: ", tid)
    
    # print ("{:<10} {:<10}".format('Seat No.', 'Count'))
    # print ("{:<10} {:<10}".format('--------', '-----'))
    # for tk in tks:
    #     print ("{:<10} {:<10}".format(tk[0], tk[1]))
    print("##################################")
    return
    
    
f = 1
while f:
    
    print("Welcome to the Railway Reservation System")
    c = int(input("1. Book Ticket\n2. Cancel Ticket\n3. Check Waiting List\n4. Exit\nEnter your choice: "))
    if c == 1:
        b = Book(db)
        print("Trains Available: ")
        print("Coimbatore to Chennai : cbe -> s1 -> s2 -> s3 -> s4 -> s5 -> che")
        print("Chennai to Coimbatore : che -> s5 -> s4 -> s3 -> s2 -> s1 -> cbe")
        tid, tks = b.book_ticket()
        
        if not tid and not tks:
            print("Tickets not booked")
            print('Try again')
            continue
        print("Tickets Booked")
        printTkt(tid, tks)
        # print("Ticket ID: ", tid)
        # for tk in tks:
        #     print("Ticket Count: ", tk[1], "Seat Number: ", tk[0])
            
        # print("data: ", db.data)
    elif c == 2:
        c = Cancel(db)
        c.cancel_ticket()
    elif c == 3:
        print("Waiting List Check status")
        wID = input("Enter the waiting list ID: ")
        # print("hasdh: ", db.bookedWaiting)
        if wID in db.waiting:
            print(f"You have {db.waiting[wID][0]} tickets in waiting list")
        elif wID in db.bookedWaiting:
            print("Your tickets are booked")
            print("Ticket ID: ", wID)
            s = [tk[0] for tk in db.booked[wID]]
            print("Seat Numbers: ", s)
            print("You can update the required information at the ticket counter")
                
        else:
            print("No such waiting list ID exists")
    else:
        pk.dump(db, open("db.pkl", "wb"))
        print("**Thank you for using the Railway Reservation System**")
        f = 0