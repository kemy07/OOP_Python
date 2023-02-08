class Fract :

    def enter (self , x , y):
        self.x = x
        self.y = y
    def value (self):
        return self.x / self.y
    def display (self):
        print(str (self.x ) , " / " ,str (self.y) , "= " , self.value())


def main ():
    f = Fract()
    val1 = int (input("Please Enter X : "))
    val2 = int (input("Please Enter Y : "))
    f.enter(val1 , val2)
    f.display()


if __name__ == '__main__':
    main()