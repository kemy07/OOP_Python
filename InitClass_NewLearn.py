class Student :
    # def entre (self , name , num , age):
    #     self.name = name
    #     self.num = num
    #     self.age = age
    def __init__(self ):
          self.name = input("please Enter Name")
          self.num = input("please Enter num")
          self.age = int (input("please Enter age"))

    def display(self):
        print("Name : " , self.name)
        print("Num : " , self.num)
        print("Age : " , self.age)
def main ():
    s1 = Student()
    s2 = Student()
    # s1.entre("kamel" , 111 , 22)
    # s2.entre("ahmed" , 222 , 30)
    s1.display()
    s2.display()


if __name__ == '__main__':
    main()