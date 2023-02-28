from book import Book
from waitinglist import WaitingList




class Cancel:
    
    
    def __init__(self, db):
        self.db = db
        self.id = None
        self.w = WaitingList(self.db)
        
    def addCancelled(self, cancelled, dep, arr):
        stations = ["cbe", "s1", "s2", "s3", "s4", "s5", "che"]
        travel = "up" if stations.index(dep) < stations.index(arr) else "down"
        if travel == "down": 
            stations = stations[::-1]
        for c in cancelled:
            for st in stations[stations.index(dep):stations.index(arr)]:
                self.db.data[travel][st].append(c[0])
        # print("added cancelled: ", self.db.data)
        return
            
        
    def cancel_ticket(self):
        print("Cancel Ticket")
        dep = input("Enter the departure station: ")
        arr = input("Enter the arrival station: ")
        self.id = input("Enter the ticket ID: ")
        if self.id in self.db.booked:
            print("Ticket Found")
            print("Confirm Cancel Ticket (Y/N)")
            if input() == "Y":
                cancelled = self.db.booked[self.id]
                del self.db.booked[self.id]
                self.addCancelled(cancelled, dep, arr)
                self.w.waitBook(cancelled, dep, arr)
                print("Ticket Cancelled")
            else:
                print("Ticket not cancelled")
                
        else:
            print("Invalid Ticket ID")
        return
            