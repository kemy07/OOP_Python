class Person :
    def insert_info (self , name , age):
        self.name = name
        self.age = age

    def print_info(self):
        print("Name : " ,self.name)
        print("Age : " ,self.age)

def main ():
 first = Person()
 second = Person()
 first.insert_info("kamel", 26)
 second.insert_info("mohamed", 20)
 first.print_info()
 second.print_info()
if __name__ == '__main__':
    main()