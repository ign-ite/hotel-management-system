class HotelFareCalculator:
    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=1800, name='', address='', cindate='', coutdate='', rno=101):
        print("\n\n*****WELCOME TO HOTEL*****\n")
        self.rt = rt
        self.r = r
        self.t = t
        self.p = p
        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    def inputdata(self):
        self.name = input("\nEnter your name:")
        self.address = input("\nEnter your address:")
        self.cindate = input("\nEnter your check in date:")
        self.coutdate = input("\nEnter your checkout date:")
        print("Your room no.:", self.rno, "\n")

    def roomrent(self):
        print("We have the following rooms for you:-")
        print("1.  type A---->rs 6000 PN\-")
        print("2.  type B---->rs 5000 PN\-")
        print("3.  type C---->rs 4000 PN\-")
        print("4.  type D---->rs 3000 PN\-")
        x = int(input("Enter Your Choice Please->"))
        n = int(input("For How Many Nights Will You Stay:"))
        if (x == 1):
            print("you have opted room type A")
            self.s = 6000 * n
        elif (x == 2):
            print("you have opted room type B")
            self.s = 5000 * n
        elif (x == 3):
            print("you have opted room type C")
            self.s = 4000 * n
        elif (x == 4):
            print("you have opted room type D")
            self.s = 3000 * n
        else:
            print("please choose a room")
        print("your room rent is =", self.s, "\n")
    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")

        print("1.water----->Rs20", "2.tea----->Rs10", "3.breakfast combo--->Rs90", "4.lunch---->Rs110",
              "5.dinner--->Rs150", "6.Exit")

        while (1):

            c = int(input("Enter your choice:"))

            if (c == 1):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 20 * d

            elif (c == 2):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 10 * d

            elif (c == 3):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 90 * d

            elif (c == 4):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 110 * d

            elif (c == 5):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 150 * d

            elif (c == 6):
                break;
            else:
                print("Invalid option")

        print("Total food Cost=Rs", self.r, "\n")

    def laundrybill(self):

def main():
    a = HotelFareCalculator()
    while (1):
        print("1.Enter Customer Data")
        print("2.Calculate room rent")
        print("3.Calculate restaurant bill")
        print("4.Calculate laundry bill")
        print("5.Calculate gamebill")
        print("6.Show total cost")
        print("7.EXIT")
        b = int(input("\nEnter your choice:"))
        if (b == 1):
            a.inputdata()
        if (b == 2):
            a.roomrent()
        if (b == 3):
            a.restaurentbill()
        if (b == 4):
            a.laundrybill()
        if (b == 5):
            a.gamebill()
        if (b == 6):
            a.display()
        if (b == 7):
            quit()

main()