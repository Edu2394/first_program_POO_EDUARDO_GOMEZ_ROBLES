from models_ import *
#CREATION OB OBJECTS
p1 = Person(1001, "John", "john@mail.com", "1111111111")
p2 = Person(1002, "Alice", "alice@mail.com", "2222222222")
p3 = Person(1003, "Bob", "bob@mail.com", "3333333333")
p4 = Person(1004, "Clara", "clara@mail.com", "4444444444")
p5 = Person(1005, "David", "david@mail.com", "5555555555")
p6 = Person(1006, "Emma", "emma@mail.com", "6666666666")
p7 = Person(1007, "Leo", "leo@mail.com", "7777777777")
p8 = Person(1008, "Nina", "nina@mail.com", "8888888888")
p9 = Person(1009, "Oscar", "oscar@mail.com", "9999999999")
p10 = Person(1010, "Paula", "paula@mail.com", "0000000000")


u1=User(1, "Carlos Méndez", "carlos@gmail.com", "2221110001", 120,[])
u2=User(2, "Ana López", "ana@gmail.com", "2221110002", 80,[])
u3=User(3, "Luis Torres", "luis@gmail.com", "2221110003", 200,[])
u4=User(4, "María Pérez", "maria@gmail.com", "2221110004", 50,[])
u5=User(5, "Sofía Ramírez", "sofia@gmail.com", "2221110005", 95,[])
u6=User(6, "Daniel Cruz", "daniel@gmail.com", "2221110006", 30,[])
u7=User(7, "Fernanda Ruiz", "fer@gmail.com", "2221110007", 60,[])
u8=User(8, "Jorge Herrera", "jorge@gmail.co", "2221110008", 150,[])
u9=User(9, "Valeria Soto", "vale@gmail.com", "2221110009", 40,[])
u10=User(10, "Ricardo Díaz", "ricardo@gmail.com", "2221110010", 300,[])

e1 = Employee(101, 1, "Admin", "admin1@mail.com", "1000000000", "admin", "Morning")
e2 = Employee(102, 2, "Admin", "admin2@mail.com", "1000000001", "admin", "Evening")
e3 = Employee(103, 3, "Worker1", "worker1@mail.com", "1000000002", "staff", "Morning")
e4 = Employee(104, 4, "Worker2", "worker2@mail.com", "1000000003", "staff", "Evening")
e5 = Employee(105, 5, "Worker3", "worker3@mail.com", "1000000004", "STAFF", "Night")
e6 = Employee(106, 6, "Worker4", "worker4@mail.com", "1000000005", "cleaner", "Morning")
e7 = Employee(107, 7, "Worker5", "worker5@mail.com", "1000000006", "cleaner", "Evening")
e8 = Employee(108, 8, "Worker6", "worker6@mail.com", "1000000007", "staff", "Night")
e9 = Employee(109, 9, "Admin", "admin3@mail.com", "1000000008", "admin  ", "Morning")
e10 = Employee(110, 10, "Worker7", "worker7@mail.com", "1000000009", "staff", "Evening")

sp1 = Space(301, "General Area 1", "Floor 1")
sp2 = Space(302, "General Area 2", "Floor 2")
sp3 = Space(303, "General Area 3", "Floor 3")
sp4 = Space(304, "General Area 4", "Floor 4")
sp5 = Space(305, "General Area 5", "Floor 5")
sp6 = Space(306, "General Area 6", "Floor 1")
sp7 = Space(307, "General Area 7", "Floor 2")
sp8 = Space(308, "General Area 8", "Floor 3")
sp9 = Space(309, "General Area 9", "Floor 4")
sp10 = Space(310, "General Area 10", "Floor 5")

fz1 = Food_Zone(201, "Snack Zone 1", "First Floor")
fz2 = Food_Zone(202, "Snack Zone 2", "Second Floor")
fz3 = Food_Zone(203, "Snack Zone 3", "Third Floor")
fz4 = Food_Zone(204, "Snack Zone 4", "Fourth Floor")
fz5 = Food_Zone(205, "Snack Zone 5", "Fifth Floor")
fz6 = Food_Zone(206, "Snack Zone 6", "First Floor")
fz7 = Food_Zone(207, "Snack Zone 7", "Second Floor")
fz8 = Food_Zone(208, "Snack Zone 8", "Third Floor")
fz9 = Food_Zone(209, "Snack Zone 9", "Fourth Floor")
fz10 = Food_Zone(210, "Snack Zone 10", "Fifth Floor")

s1 = Screen(1, "Screen 1", "First Floor", "IMAX", True)
s2 = Screen(2, "Screen 2", "First Floor", "Normal",  False)
s3 = Screen(3, "Screen 3", "Second Floor", "VIP",  True)
s4 = Screen(4, "Screen 4", "Second Floor", "Normal",  False)
s5 = Screen(5, "Screen 5", "Third Floor", "IMAX",  True)
s6 = Screen(6, "Screen 6", "Third Floor", "Normal",  False)
s7 = Screen(7, "Screen 7", "Fourth Floor", "VIP",  True)
s8 = Screen(8, "Screen 8", "Fourth Floor", "Normal",  False)
s9 = Screen(9, "Screen 9", "Fifth Floor", "IMAX",  True)
s10 = Screen(10, "Screen 10", "Fifth Floor", "Normal",  False)

m1 = Movie("Inception", 148, "+13", "Sci-Fi")
m2 = Movie("Titanic", 195, "-18", "Romance")
m3 = Movie("Avengers", 143, "+13", "Action")
m4 = Movie("Joker", 122, "+18", "Drama")
m5 = Movie("Frozen", 102, "-18", "Animation")
m6 = Movie("Interstellar", 169, "+13", "Sci-Fi")
m7 = Movie("Gladiator", 155, "+18", "Action")
m8 = Movie("Coco", 105, "-18", "Animation")
m9 = Movie("Batman", 140, "+13", "Action")
m10 = Movie("Up", 96, "-18", "Animation")

f1 = Function(1, m1, s1, datetime.strptime("2026-06-01 18:00:00", format_pattern), 100)
f2 = Function(2, m2, s2, datetime.strptime("2026-06-01 20:00:00", format_pattern), 90)
f3 = Function(3, m3, s3, datetime.strptime("2026-06-02 16:00:00", format_pattern), 110)
f4 = Function(4, m4, s4, datetime.strptime("2026-06-02 21:00:00", format_pattern), 95)
f5 = Function(5, m5, s5, datetime.strptime("2026-06-03 17:00:00", format_pattern), 85)
f6 = Function(6, m6, s6, datetime.strptime("2026-06-03 19:00:00", format_pattern), 120)
f7 = Function(7, m7, s7, datetime.strptime("2026-06-04 18:30:00", format_pattern), 130)
f8 = Function(8, m8, s8, datetime.strptime("2026-06-04 15:00:00", format_pattern), 80)
f9 = Function(9, m9, s9, datetime.strptime("2026-06-05 20:30:00", format_pattern), 115)
f10 = Function(10, m10, s10, datetime.strptime("2026-06-05 14:00:00", format_pattern), 75)


pp1 = Promotion("PROMO10", "10% Discount", 10, datetime.strptime("2026-12-31 23:59:59", format_pattern))
pp2 = Promotion("PROMO15", "15% Discount", 15, datetime.strptime("2026-12-31 23:59:59", format_pattern))
pp3 = Promotion("PROMO20", "20% Discount", 20, datetime.strptime("2026-12-31 23:59:59", format_pattern))
pp4 = Promotion("PROMO25", "25% Discount", 25, datetime.strptime("2026-12-31 23:59:59", format_pattern))
pp5 = Promotion("PROMO30", "30% Discount", 30, datetime.strptime("2026-12-31 23:59:59", format_pattern))
pp6 = Promotion("PROMO5", "5% Discount", 5, datetime.strptime("2026-12-31 23:59:59", format_pattern))
pp7 = Promotion("PROMO50", "50% Discount", 50, datetime.strptime("2026-12-31 23:59:59", format_pattern))
pp8 = Promotion("STUDENT", "Student Discount", 12, datetime.strptime("2026-12-31 23:59:59", format_pattern))
pp9 = Promotion("VIP", "VIP Discount", 18, datetime.strptime("2026-12-31 23:59:59", format_pattern))
pp10 = Promotion("WELCOME", "Welcome Bonus", 8, datetime.strptime("2026-12-31 23:59:59", format_pattern))



r1 = Reservation( u1, f1, ["A1","A2"], 200)
r2 = Reservation( u2, f2, ["B1"], 90)
r3 = Reservation( u3, f3, ["C1","C2","C3"], 330)
r4 = Reservation( u4, f4, ["A3"], 95)
r5 = Reservation( u5, f5, ["B2","B3"], 170)
r6 = Reservation( u6, f6, ["C4"], 120)
r7 = Reservation(u7, f7, ["A4","B4"], 260)
r8 = Reservation( u8, f8, ["C2"], 80)
r9 = Reservation( u9, f9, ["A1","B1","C1"], 345)
r10 = Reservation( u10, f10, ["B2"], 75)

while True:
    print("\n--MENU SYSTEM OF THE CINEMA 'LOS GOMEZ'--\n")
    print("1.PERSON")
    print("2.USER")
    print("3.EMPLOYEE")
    print("4.SPACE")
    print("5.SCREEN")
    print("6.FOOD_ZONE")
    print("7.FUNCTION")
    print("8.MOVIE")
    print("9.PROMOTION")
    print("10.RESERVATION")
    print("11.EXIT")

    x=int(input("\nSELECT A CLASS TO SEE ITS OBJECTS AND METHODS\n"))
    match x:
        case 1:
            print("\n--------PERSON--------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.Prove login\n")  
            print("\n3.Prove logout\n")  
            print("\n4.Prove Update Data\n")  
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    p1.print_object()
                    p2.print_object()
                    p3.print_object()
                    p4.print_object()
                    p5.print_object()
                    p6.print_object()
                    p7.print_object()
                    p8.print_object()
                    p9.print_object()
                    p10.print_object()
                case 2:
                    print("\n-----USE OF LOGIN----- \n")
                    p1.login("john@mail.com")
                case 3:
                    print("\n-----USE OF LOGOUT-----\n ")
                    p2.logout()
                case 4:
                    print("\n-----USE OF UPDATE DATA----- \n")
                    print("\nUSER ORIGINAL:\n")
                    p3.print_object()
                    p3.update_data(1011, "Ricardo", "ricardo@mail.com", "1231231234")
                    print("\nNEW DATA OF THE USER:\n")
                    p3.print_object()
                case _:
                    print("OPTION NOT VALID")      
        case 2:
            print("\n--------USER--------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.CREATE RESERVATION\n")  
            print("\n3.CANCEL RESERVATION\n")  
            print("\n4.CONSULT PROMOTIONS\n")  
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    u1.print_object()
                    u2.print_object()
                    u3.print_object()
                    u4.print_object()
                    u5.print_object()
                    u6.print_object()
                    u7.print_object()
                    u8.print_object()
                    u9.print_object()
                    u10.print_object()
                case 2:
                    print("\n-----USE OF CREATE RESERVATION----- \n")
                    u1.create_Reservation()  
                case 3:
                    print("\n-----USE OF CANCEL RESERVATION-----\n ")
                    u1.cancel_Reservation(u1.Reservation_History[0].id_reservation)
                case 4:
                    print("\n-----USE OF CONSULT PROMOTIONS----- \n")
                    u3.consult_Promotions()
                case _:
                    print("\nOPTION NOT VALID\n")      
        case 3:
            print("\n--------EMPLOYEE--------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.TAKE ENTRY\n")  
            print("\n3.MANAGE FUNCTIONS(ONLY ADMINS)\n")   
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    e1.print_object()
                    e2.print_object()
                    e3.print_object()
                    e4.print_object()
                    e5.print_object()
                    e6.print_object()
                    e7.print_object()
                    e8.print_object()
                    e9.print_object()
                    e10.print_object()
                case 2:
                    print("\n-----USE OF TAKE ENTRY-----\n ")
                    e1.Take_Entry()
                case 3:
                    print("\n-----USE OF MANAGE FUNCTIONS-----\n ")
                    e1.manage_Functions()
                case _:
                    print("\nOPTION NOT VALID\n")      
        case 4:
            print("\n--------SPACE--------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    sp1.print_object()
                    sp2.print_object()
                    sp3.print_object()
                    sp4.print_object()
                    sp5.print_object()
                    sp6.print_object()
                    sp7.print_object()
                    sp8.print_object()
                    sp9.print_object()
                    sp10.print_object()    
        case 5:
                print("\n--------SCREEN-------\n")
                print("\nWhat do you want to do?\n")
                print("\n1.See OBJECTS\n")   
                print("\n2.CHECK AVAILABILITY\n")  
                print("\n3.OBTAIN TYPE\n")  
                print("\n4.CLEAN SPACE\n")  
                print("\n5.ADJUST CAPACITY\n")  
                x1=int(input())
                match x1:
                    case 1:
                        print("\n--------SEE OBJECTS------\n")
                        s1.print_object()
                        s2.print_object()
                        s3.print_object()
                        s4.print_object()
                        s5.print_object()
                        s6.print_object()
                        s7.print_object()
                        s8.print_object()
                        s9.print_object()
                        s10.print_object()
                    case 2:
                        print("\n-----USE OF CHECK AVAILABILITY----- \n")
                        s1. check_Availability()
                    case 3:
                        print("\n-----USE OF OBTAIN TYPE-----\n ")
                        s2.Obtain_Screen()
                    case 4:
                        print("\n-----USE OF CLEAN SPACE----- \n")
                        print(f"\nCAPACITY BEFORE THE CLEAN: {s1.capacity}\n")
                        s1.clean_space()
                        print(f"\nCAPACITY AFTER THE CLEAN: {s1.capacity}\n")
                    case 5:
                        print("\n-----USE OF ADJUST CAPACITY----- \n")
                        print(f"\nCAPACITY BEFORE THE CHANGE: {s1.capacity}\n")
                        s1.adjust_Capacity(10)
                        print(f"\nCAPACITY AFTER THE CHANGE: {s1.capacity}\n")
                    case _:
                        print("\nOPTION NOT VALID\n")    
        case 6:
            
            print("\n--------FOOD ZONE-------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.Sell Product\n")  
            print("\n3.UPDATE STOCK\n")  
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    fz1.print_object()
                    fz2.print_object()
                    fz3.print_object()
                    fz4.print_object()
                    fz5.print_object()
                    fz6.print_object()
                    fz7.print_object()
                    fz8.print_object()
                    fz9.print_object()
                    fz10.print_object()
                case 2:
                    print("\n-----USE OF SELL PRODUCT----- \n")
                    fz1.Sell_product("Popcorns")

                case 3:
                    print("\n-----USE OF UPDATE STOCK----- \n")
                    print(f"\nSTOCK BEFORE THE UPDATE:{fz1.stock["Popcorns"]}\n")
                    fz1.Update_Stock(10,"Popcorns")
                    print(f"\nSTOCK AFTER THE UPDATE:{fz1.stock["Popcorns"]}\n")
                case _:
                    print("\nOPTION NOT VALID\n")      

        case 7:
            print("\n--------FUNCTION-------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.CHECK FREE SEATS\n")  
            print("\n3.OBTAIN FUNCTION DETAILS\n")  
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    f1.print_object()
                    f2.print_object()
                    f3.print_object()
                    f4.print_object()
                    f5.print_object()
                    f6.print_object()
                    f7.print_object()
                    f8.print_object()
                    f9.print_object()
                    f10.print_object()
                case 2:
                    print("\n-----USE OF CHECK FREE SEATS----\n ")
                    f1.free_seats()
                case 3:
                    print("\n-----USE OF OBTAIN FUNCTION DETAILS-----\n ")
                    f2.ObtainFunctionDetails()
                case _:
                    print("OPTION NOT VALID")      
        case 8:
            print("\n--------MOVIE-------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.OBTAIN_SYNOPSIS\n")  
            print("\n3.IS FOR ALL?\n")  
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    m1.print_object()
                    m2.print_object()
                    m3.print_object()
                    m4.print_object()
                    m5.print_object()
                    m6.print_object()
                    m7.print_object()
                    m8.print_object()
                    m9.print_object()
                    m10.print_object()
                case 2:
                    print("\n-----USE OF OBTAIN_SYNOPSIS---- \n")
                    m1.obtain_sinopsis()
                case 3:
                    print("\n-----USE OF IS FOR ALL?----- \n")
                    m2.isforall()
                case _:
                    print("\nOPTION NOT VALID\n")      
        case 9:
            print("\n--------PROMOTION-------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.IS VALID?\n")  
            print("\n3.APPLY DISCOUNT\n")  
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    pp1.print_object()
                    pp2.print_object()
                    pp3.print_object()
                    pp4.print_object()
                    pp5.print_object()
                    pp6.print_object()
                    pp7.print_object()
                    pp8.print_object()
                    pp9.print_object()
                    pp10.print_object()
                case 2:
                    print("\n-----USE OF IS VALID?---- \n")
                    if pp1.is_valid(u1):
                        print("\nThe promotion is valid\n")
                    else:
                        print("\nThe promotion isn't valid\n")
                    
                case 3:
                    print("\n-----USE OF APPLY DISCOUNT-----\n ")
                    print(f"\nAMOUNT BEFORE THE PROMOTION:{r1.amount}\n")
                    pp1.apply_discount(r1)
                    print(f"\nAMOUNT AFTER THE PROMOTION:{r1.amount}\n")
                case _:
                    print("\nOPTION NOT VALID\n")      
        case 10:
            print("\n--------RESERVATION------\n")
            print("\nWhat do you want to do?\n")
            print("\n1.See OBJECTS\n")   
            print("\n2.CONFIRM PAYMENT\n")  
            print("\n3.DO A TICKET\n")  
            print("\n4.APPLY PROMOS\n")  
            x1=int(input())
            match x1:
                case 1:
                    print("\n--------SEE OBJECTS--------\n")
                    r1.print_object()
                    r2.print_object()
                    r3.print_object()
                    r4.print_object()
                    r5.print_object()
                    r6.print_object()
                    r7.print_object()
                    r8.print_object()
                    r9.print_object()
                    r10.print_object()
                case 2:
                    print("\n-----USE OF CONFIRM PAYMENT---- \n")
                    r1.Confirm_Payment()
                    print(f"\nNEW STATUS IS {r1.status}\n")
                    
                case 3:
                    print("\n-----DO A TICKET----- \n")
                    r2.Do_A_ticket()
                case 4:
                    print("\n-----APPLY PROMOS----- \n")
                    r3.apply_promos(pp1)
                case _:
                    print("\nOPTION NOT VALID\n")
        case 11:
            print("\nTHANKS FOR HAVE USED OUR PROGRAM!\n")
            break
            

        case _:
            print("\nOPTION NOT VALID\n")        




