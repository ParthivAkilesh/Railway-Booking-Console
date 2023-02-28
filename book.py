import random
from waitinglist import WaitingList



class Book:
    
    
    def __init__(self, db):
        self.db = db
        self.w = WaitingList(self.db)
        # print(self.db.data)
       
       
    def getTickets(self, ticketCount, trains, dep, arr, stations, count=1):
        
        # print("staions: ", stations)
        # print("trains: ", trains)
        tickets = []
        for j in range(ticketCount):
            tnum = trains[dep].pop()
            for st in stations[stations.index(dep)+1:stations.index(arr)]:
                # print("Station :   **  : ",st, trains[st])
                try:
                    trains[st].remove(tnum)
                except:
                    trains[dep].append(tnum)
                    self.getTickets(ticketCount, trains, dep, arr, stations)
            seat = input(f"Enter the name of the passenger {count}: ")  
            tickets.append((tnum, seat))
            count+=1 
            # print(tickets)
        # print("data book: ", self.db.data)
        return tickets      
    
    
    def checkTrain(self, dep, arr):
        
        stations = ["cbe", "s1", "s2", "s3", "s4", "s5", "che"]
        if dep not in stations or arr not in stations:
            print("Invalid Station")
            return False, False
        travel = "up" if stations.index(dep) < stations.index(arr) else "down"
        if travel == "down": 
            stations = stations[::-1]
        trains = self.db.data[travel]
        ticketCount = int(input("Enter the number of tickets: "))
        availCount = min([len(trains[st]) for st in stations[stations.index(dep):stations.index(arr)]])
        if availCount < ticketCount:
            print("Trains not available")
            waitConfirm = self.w.wait(ticketCount, availCount)
            if waitConfirm:
                tickets = self.getTickets(availCount, trains, dep, arr, stations)
                wbid = f"WBID{random.randint(1000, 9999)}{ticketCount-availCount}"
                wbloc = f"{dep}-{arr}"
                # w.waitBook(tickets)
                # print(wbid, tickets)
                return (wbid, wbloc), tickets
            else: return False, False

        print("Trains available")
        tickets = self.getTickets(ticketCount, trains, dep, arr, stations)
        # print(tickets)
        ticketID = f"TicketID{random.randint(1000, 9999)}"
        return ticketID, tickets
                    
            
    def updateBooked(self, ticketID, tickets):
        
        if "WB" in ticketID[0]:
            self.db.booked[ticketID[0]] = tickets
            self.db.waiting[ticketID[0]] = (ticketID[0][-1], ticketID[1])
        else:
            self.db.booked[ticketID] = tickets            
                   
            
      
    def book_ticket(self):
        print("Book Ticket")
        dep = input("Enter the departure station: ")
        arr = input("Enter the arrival station: ")
        ticketID, tickets = self.checkTrain(dep, arr)
        print("CONFIRMED  :  ", ticketID, tickets)
        
        if not ticketID and not tickets:
            return False, False
            
        self.updateBooked(ticketID, tickets)
        # print("waiting:  ", self.db.waiting)
        
        return ticketID, tickets
        
    
        