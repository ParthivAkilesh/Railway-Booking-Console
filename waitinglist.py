# from book import Book
from database import DataBase
import random

# b = Book()


class WaitingList:
    
    def __init__(self, db):
        self.tickets = None
        self.avail = None
        self.db = db
        
    def wait(self, ticketCount, availCount):
        
        self.tickets = ticketCount
        self.avail = availCount
        print("Waiting List")
        print("Tickets Available: ", self.avail)
        print("Tickets Required: ", self.tickets)
        ch = input(f"Do you want to book {self.avail} tickets and go under waiting list for remaining {self.tickets-self.avail}? (Y/N)")
        if ch == "Y":
            return True
        else:
            print("We can notify you when tickets are available")
            return False
        
        
    def waitSeat(self, count, key, cancelled, dep, arr):
          
        self.db.booked[key].extend([i for i in cancelled[:count]])
        cbook = [i for i in cancelled[:count]]
        stations = ["cbe", "s1", "s2", "s3", "s4", "s5", "che"]
        travel = "up" if stations.index(dep) < stations.index(arr) else "down"
        if travel == "down": 
            stations = stations[::-1]
        for i in cbook:
            for st in stations[stations.index(dep):stations.index(arr)]:
                self.db.data[travel][st].remove(i[0])
        return
        
        
        
    def waitBook(self,cancelled, dep, arr):
        
        tkSize = len(cancelled)
        if len(self.db.waiting) == 0:
            return 
        while tkSize > 0:
            # print("Waiting List   ", self.db.waiting, self.db.waiting.keys())
            if len(list(self.db.waiting.values()))>0:
                waitTk = list(self.db.waiting.values())[0][0]
                waitLoc = list(self.db.waiting.values())[0][1]
                waitLoc = waitLoc.split("-")
                # print("wait Loc: ", waitLoc)
                waitKey = list(self.db.waiting.keys())[0]
                if int(waitTk) > tkSize:
                    self.db.waiting[waitKey] -= tkSize
                    self.waitSeat(tkSize, waitKey, cancelled, dep, arr)
                    # print("booked waiting: ", self.db.booked)
                    # print("updated data: ", self.db.data)
                    return
                else:
                    self.waitSeat(int(waitTk), waitKey, cancelled, waitLoc[0], waitLoc[1])
                    self.db.bookedWaiting.append(waitKey)
                    del self.db.waiting[waitKey]
                    tkSize -= int(waitTk)
                    # print("checking:   ", self.db.waiting, tkSize)
                    # print("booked waiting: ", self.db.booked)
                    # print("updated data: ", self.db.data)
                    if tkSize == 0:
                        return
                    else:
                        continue
            else:
                return
                
        # print("booked waiting: ", self.db.booked)
        # print("updated data: ", self.db.data)
        return
            
            
        
        
        
        
        
        
        
        