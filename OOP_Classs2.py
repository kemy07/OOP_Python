class Rectangle :

    def enter (self , x , y):
        self.x = x
        self.y = y
    def Area(self):
        return self.x * self.y
    def round (self):
        return 2 * (self.x + self.y)
    def display (self):
        print("Width : " , self.x)
        print("Height : " , self.y)

def main ():
    r1 = Rectangle ()
    r2 = Rectangle ()
    # first rectangle object details
    r1.enter(5 , 4)
    print("Area = " , r1.Area())
    print("Round = " , r1.round())
    r1.display()
    # second rectangle object details
    r2.enter(10 , 2)
    print("Area = " , r2.Area())
    print("Round = " , r2.round())
    r2.display()


if __name__ == '__main__':
    main()