class cashieringsystem:

    def __init__(self, a=0, total=0, recieve=0, change=0, temp=0):

        print("\n\n*****WELCOME TO SIMPLE CASHIERING SYSTEM*****\n")

        self.a = a
        self.total = total
        self.recieve = recieve
        self.change = change
        self.temp = temp

    def foods(self):

        print("*****JUDE'S RESTAURANT MENU*****")

        print("\t\t\t1.Adobo----->30", "\n\t\t\t2.Nilaga----->35", "\n\t\t\t3.Pork Chop--->50", "\n\t\t\t4.Letchon Paksiw---->40",
              "\n\t\t\t5.Cash Out", "\n\t\t\t6.Exit")

        while (1):

            c = int(input("\t\t\tChoose:\n\t\t\t"))

            if (c == 1):

                d = int(input("\t\t\tEnter the quantity:\n\t\t\t"))
                self.total = self.total + 30 * d

            elif (c == 2):
                d = int(input("\t\t\tEnter the quantity:\n\t\t\t"))
                self.total = self.total + 35 * d

            elif (c == 3):
                d = int(input("\t\t\tEnter the quantity:\n\t\t\t"))
                self.total = self.total + 50 * d

            elif (c == 4):
                d = int(input("\t\t\tEnter the quantity:\n\t\t\t"))
                self.total = self.total + 40 * d

            elif (c == 5):
                print("\t\t\ttotal:", self.total)
                if (self.total > 0):
                    recieve = int(input("\t\t\tInput Money Recieve:\n\t\t\t"))
                    print("\t\t\tChange:", recieve - self.total)
                    print("\t\t\t*****Thank You Come Again!!!*****")
                    quit()
            elif (c == 6):
                quit()
            else:
                print("\t\t\tInvalid option")


def main():
    a = cashieringsystem()

    while (1):
        a.foods()


main()