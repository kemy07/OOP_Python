class product:
    def enter (self , name , price , pdate):
        self.name = name
        self.price = price
        self.pdate = pdate
    def display(self):
        print("Name : " , self.name)
        print("Price : " , self.price)
        print("Pdate : " , self.pdate)
class DailyProduct (product):
    def enter (self , name , price , pdate , expired):
        super().enter(name , price , pdate)
        self.expired = expired
    def display(self):
        super().display()
        print("Expired Date : " , self.expired)


def main ():
    p = product ()
    p.enter("Tv" , 1000 , "1-1-2023")
    p.display()
    d = DailyProduct()
    d.enter("milk" , 1000 , "1-1-2020" , "1-1-2024")
    d.display()
if __name__ == '__main__':
    main()