class A :
    def printA (self):
        print("This is Class A")
class B(A):
    def printB(self):
        print("This is Class B")



def main ():
    a = A ()
    b = B ()
    a.printA()
    b.printB()
    b.printA()
if __name__ == '__main__':
    main()