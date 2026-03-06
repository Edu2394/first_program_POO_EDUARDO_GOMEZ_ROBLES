from datetime import datetime
format_pattern = "%Y-%m-%d %H:%M:%S"
class Person():
    
    def __init__(self,id_person,name,email,telephone):
        self.name=name
        self.email=email
        self.id_person=id_person
        self.telephone=telephone
    def login(self,email):
        if self.email==email:
            print(f"\nWelcome {self.name} to our online system\n")
        else:
             print(f"\nYour email is incorrect or you did not register yet\n")
    def logout(self):
        print(f"\nGoodbye {self.name} , come back whenever you want\n")

    def update_data(self,id_person,name,email,telephone):
        self.name=name
        self.email=email
        self.id_person=id_person
        self.telephone=telephone
        print(f"\nThe data was updated succesfully\n")
    def print_object(self):
        print(f"\nID:{self.id_person}\t|\t{self.name}\t|\t{self.email}\t|\tTEL:{self.telephone}\t\n")
class User(Person):
    def __init__(self,id_person,name,email,telephone,Fidelity_points,Reservation_History):
       super().__init__(id_person,name,email,telephone)
       self.Fidelity_points=Fidelity_points
       self.Reservation_History=Reservation_History
    def create_Reservation(self):
   
        print(f"\nStarting reservation process..\n")
        print(f"\nUser:{self.name} (Points:{self.Fidelity_points})")
        print(f"\nWhat movie want to watch?\n")
        print(f"\nThe avaliable movies are:\n")
        for movie in Movie.list_movies:
            print(f"\n{movie.title}\n")
        movie_selected=input("\nSelect one\n")
        print(f"\nWhich function?\n")
        print(f"\nThe avaliable functions are:\n")
        for function in Function.list_functions:
            if function.movie.title==movie_selected:
                print(f"\nTHE FUNCTION WITH ID {function.id_function}\n")
        function_selected=int(input("\nSelect one id_function\n"))
        for function in Function.list_functions:
            if(function.id_function==function_selected):
                funct=function
        if funct.screen.capacity>0:
            print(f"\nThe avaliable seats are:\n")
            for seats,status in funct.screen.seats.items():
                print(f"\n{seats} {status}\n")
            number_seats=int(input((f"\nHow many seats?\n")))
            if( (funct.screen.capacity-number_seats)>=0):
                list_seats_reservation=[]
                for i in range(number_seats):
                        while True:
                            seatt=input(f"\nWhich seat?\n")
                            if funct.screen.seats[seatt]=="Available":
                                funct.screen.seats[seatt]="Used"
                                list_seats_reservation.append(seatt)
                                funct.screen.capacity-=1
                                break
                            else:
                                print(f"\nThis seat is used,select other\n")
                Reservation_=Reservation(self,funct,list_seats_reservation,funct.Standard_cost*number_seats)
                self.Reservation_History.append(Reservation_)
                print("\nVISUALIZE RESERVATION\n")
                Reservation_.print_object()               
        else:
            print(f"\nThere aren't seats available\n")     
    def print_object(self):
        print(f"\nID:{self.id_person}\t|\t{self.name}\t|\t{self.email}\t|\t{self.telephone}\t|\tPOINTS:{self.Fidelity_points}\t\n")
    def consult_Promotions(self):
        print(f"\nThe current promotions are:\n")
        for promotion in Promotion.list_promotions:
            print(f"\n{promotion.Code}\n")
    def cancel_Reservation(self,id_reservation):
        print(f"\nCanceling reservation with ID: {id_reservation}\n")
        for resr in self.Reservation_History:
            if resr.id_reservation==id_reservation:
                resr.status="CANCELED"
                resr.function.screen.capacity+=len(resr.seats)
                for f in resr.seats:
                    if f in  resr.function.screen.seats.keys():
                        resr.function.screen.seats[f]="Available"
                print(f"\nReservation canceled successfully\n")
                print("\nCHANGE OF THE STATUS:\n")
                resr.print_object()

class Employee(Person):
     def __init__(self,id_person,id_employee,name,email,telephone,Rol,Schedule):
       super().__init__(id_person,name,email,telephone)
       self.Schedule=Schedule
       self.Rol=Rol
       self.id_employee=id_employee
     def Take_Entry(self):
        self.entry_time = datetime.now()
        print(f"\n{self.name} entered at {self.entry_time}\n")
     
     def manage_Functions(self):
         if self.Rol!="admin":
             print(f"\nYou don't have access to this method!\n")
         else:
             print(f"\nWhat do you want to do?:\n ")
             print(f"\n1.Add Functions\n ")
             print(f"\n2.Add movies \n")
             print(f"\n3.Add promotions\n ")
             x=int(input("\nSelect an option\n"))
             match x:
                 case 1:
                     id_function=int(input((f"\nWhat is the id of the function do you want to add?\n")))
                     title_movie=input((f"\nWhat is the title movie of the function do you want to add?\n"))
                     duration=int(input((f"\nWhat is the duration of the  movie  do you want to add?\n")))
                     clasification=input((f"\nWhat is the clasification of the  movie  do you want to add?\n"))
                     gender=input((f"\nWhat is the gender the  movie do you want to add?\n"))
                     n_movie=Movie(title_movie,duration,clasification,gender)
                     id_space=int(input((f"\nWhat is the id of the screen of the function do you want to add?\n")))
                     name=input((f"\nWhat is the name of the screen of the function do you want to add?\n"))
                     ubication=input((f"\nWhat is the ubication of the screen of the function do you want to add?\n"))
                     type=input((f"\nWhat is the type of the screen of the function do you want to add?\n"))
                     IsVip=input((f"\nIt is VIP the screen of the function do you want to add?\n"))
                     if IsVip=="YES" or  IsVip=="Yes" or  IsVip=="yes":
                         Isvip=True
                     elif IsVip=="NO" or  IsVip=="No" or  IsVip=="no":
                         Isvip=False
                     n_screen=Screen(id_space,name,ubication,type,Isvip)
                     Schedule_of_Start=input((f"\nWhat is the Schedule of start of the function do you want to add?\n"))
                     Schedule_of_Start=datetime.strptime(Schedule_of_Start, format_pattern)
                     Standard_cost=int(input((f"\nWhat is the Standard cost of the function do you want to add?\n")))
                     n_function=Function(id_function,n_movie,n_screen,Schedule_of_Start,Standard_cost)
                     print("\n-----IMPLEMENTATION OF NEW FUNCTION--------\n")
                     n_function.print_object()
                     
                 case 2:
                     title=input((f"\nWhat is the title of the movie do you want to add?\n"))
                     duration=input((f"\nWhat is the duration of the  movie  do you want to add?\n"))
                     clasification=input((f"\nWhat is the clasification of the  movie  do you want to add?\n"))
                     gender=input((f"\nWhat is the gender the  movie do you want to add?\n"))
                     n_movie=Movie(title,duration,clasification,gender)
                     print("\n-----IMPLEMENTATION OF NEW MOVIE--------\n")
                     n_movie.print_object()
                   
                 case 3:
                     Code=input((f"\nWhat is the Code of the promotion do you want to add?\n"))
                     Description=input((f"\nWhat is the Description of the promotion  do you want to add?\n"))
                     Discount=float(input((f"\nWhat is the Discount of the promotion  do you want to add?\n")))
                     Expiry_date=input((f"\nWhat is the Expiry_date of the promotion do you want to add?\n"))
                     Expiry_date=datetime.strptime(Expiry_date, format_pattern)  
                     n_promotion=Promotion(Code,Description,Discount,Expiry_date)
                     print("\n-----IMPLEMENTATION OF NEW PROMOTION--------\n")
                     n_promotion.print_object()
                 case _:
                     print(f"\nThis isn't an option!\n")
     def print_object(self):
        print(f"\nID:{self.id_person}\t|\t{self.name}\t|\t{self.email}\t|\tTEL:{self.telephone}\t|\tID_EMPLOYEE:{self.id_employee}\t|\tROL:{self.Rol}\t|\tSCHEDULE:{self.Schedule}\t\n")
class Space():
    def __init__(self,id_space,name,ubication):
        self.name=name
        self.ubication=ubication
        self.id_space=id_space
    def check_Availability(self):
        return 0
    
    def clean_space(self):
        return 0
    def print_object(self):
        print(f"\nID:{self.id_space}\t|\t{self.name}\t|\tUBICATION: {self.ubication}\t\n")
class Screen(Space):
    def __init__(self,id_space,name,ubication,type,IsVip):
       super().__init__(id_space,name,ubication)
       self.type=type
       self.capacity=12
       self.IsVip=IsVip
       self.original_capacity=12
       self.seats={"A1":"Available","A2":"Available","A3":"Available","A4":"Available","B1":"Available","B2":"Available","B3":"Available","B4":"Available","C1":"Available","C2":"Available","C3":"Available","C4":"Available"}
    def check_Availability(self):
        if self.capacity>0:
            print(f"\nThe screen still has {self.capacity} seats\n")
        else:
            print(f"\nThere aren't free seats\n")
    def adjust_Capacity(self,Seats_on_used):
        self.capacity-=Seats_on_used
        print(f"\nThe availability of seats has changed\n")
    def Obtain_Screen(self):
        print(f"\nThe screen is {self.type}\n")
    def clean_space(self):
        for seats,availability in self.seats.items():
         self.seats[f"{seats}"]="Available"
        self.capacity=self.original_capacity
    def print_object(self):
        print(f"\nID:{self.id_space}  | {self.name} | UBICATION: {self.ubication} | TYPE:{self.type} | CAPACITY: {self.capacity} SEATS  | IS VIP? :{self.IsVip} \n")
class Food_Zone(Space):
    def __init__(self,id_space,name,ubication):
       super().__init__(id_space,name,ubication)
       self.products=["Popcorns","Ice cream","Candys"]
       self.stock={"Popcorns":30,"Ice cream":40,"Candys":10}
    def Sell_product(self,Product):
        number_S=int(input(f"\nYou are going to buy {Product}, How many?\n"))
        print(f"\nYou have bought {number_S} {Product}\n ")
        return number_S
    def Update_Stock(self,number_S,Product):
            self.stock[f"{Product}"]-=number_S
     
    def print_object(self):
        print(f"\nID:{self.id_space}  | {self.name} | UBICATION: {self.ubication} \n")
        print("\nAVAILABLE PRODUCTS AND THEIR STOCK:\n")
        for p,t in self.stock.items():
            print(f"{p} | {t}")
class Movie():
    list_movies=[]
    def __init__(self,title,duration,clasification,gender):
        self.title=title
        self.duration=duration
        self.clasification=clasification
        self.gender=gender
        Movie.list_movies.append(self)
    def add_movies(self,movie_):
        Movie.list_movies.append(movie_)
    def obtain_sinopsis(self):
        print(f"\nThis movie is {self.title} of {self.duration} minutes,also it has clasification {self.clasification} with a gender {self.gender}\n")
    def isforall(self):
        if self.clasification=="+18":
            print(f"\nThis movie is not for all people\n")
        elif self.clasification=="-18":
            print(f"\nThis movie is  for all people\n")
    def print_object(self):
        print(f"\nTITLE:{self.title}\t|\tDURATION OF {self.duration} MINUTES\t|\tCLASIFICATION: {self.clasification}\t|\tGENDER:{self.gender} \n")
class Function():
    list_functions=[]
    def __init__(self,id_function,movie,screen,Schedule_of_Start,Standard_cost):
        self.id_function=id_function
        self.movie=movie
        self.screen=screen
        self.Schedule_of_Start=Schedule_of_Start
        self.Standard_cost=Standard_cost 
        Function.list_functions.append(self)
    def add_functions(self,functions_):
        Function.list_functions.append(functions_)
    def free_seats(self):
        print(f"\nThere are {self.screen.capacity} seats avaliable\n")
    def ObtainFunctionDetails(self):
        print(f"\nThe function with id{self.id_function}, has {self.movie.title} movie on screen {self.screen.name}, and it starts at {self.Schedule_of_Start} with a cost of {self.Standard_cost}\n")
    def print_object(self):
        print(f"ID:{self.id_function}")
        print("\nDATA OF THE MOVIE:\n")
        self.movie.print_object()
        print("\nDATA OF THE SCREEN\n") 
        self.screen.print_object()
        print(f"\nSCHEDULE OF START : {self.Schedule_of_Start}\t|\tSTANDARD COST : {self.Standard_cost}\n")

class Promotion():
     list_promotions=[]
     def __init__(self,Code,Description,Discount,Expiry_date):
        self.Code=Code
        self.Description=Description
        self.Discount=Discount
        self.Expiry_date=Expiry_date
        Promotion.list_promotions.append(self)
     def add_promotions(self,promotion_):
         Promotion.list_promotions.append(promotion_)
     def is_valid(self,user):
         if len(user.Reservation_History)>=10:
            return True
         else:    
            return False
     def apply_discount(self,reservation):
           reservation.amount-=((self.Discount/100)*reservation.amount)
     def print_object(self):
        print(f"\nCODE:{self.Code}\t|\tDESCRIPTION: {self.Description}\t|\tDISCOUNT: {self.Discount}\t|\tEXPIRY_DATE:{self.Expiry_date}\n ")

         
class Reservation():
      counter=0
      def __init__(self,user,function,seats,amount):
        Reservation.counter+=1
        self.id_reservation=Reservation.counter
        self.user=user
        self.function=function
        self.seats=seats
        self.amount=amount
        self.status="WHITHOUT PAY"
      def Confirm_Payment(self):
          print(f"\nYour reservation is \n")
          print(f"\nUSER-{self.user.name}\n")
          print(f"\nFUNCTION - {self.function.id_function} SEATS: {len(self.seats)}\n")
          print(f"\nTOTAL AMOUNT ${self.amount}\n")
          print(f"\nYour payment was succesfull\n")
          self.status="PAID"
      def Do_A_ticket(self):
          print(f"\nYour ticket has the folowwing information\n")
          print(f"\nUSER-{self.user.name}\n")
          print(f"\nFUNCTION - {self.function.id_function} SEATS: {len(self.seats)}\n")
          print(f"\nTOTAL AMOUNT ${self.amount}\n")
          print(f"\nSTATUS -{self.status}\n")
      def apply_promos(self,promo):
          if promo.is_valid(self.user)==False:
              print(f"\nYou cannot apply this promotion\n")
          else:
              promo.apply_discount(self)
              print(f"\nYour promotion was applied,now your amount of the reservations is {self.amount}\n")
      def print_object(self):
        print(f"\nID OF RESERVATION:{self.id_reservation}\n")
        print("\nDATA OF THE USER:\n")
        print(f"\nID:{self.user.id_person}\t|\t{self.user.name}\t|\t{self.user.email}\t|\tTEL:{self.user.telephone}\t|\tPOINTS:{self.user.Fidelity_points}\n")
        print("\nDATA OF THE FUNCTION:\n")
        self.function.print_object()
        print("\nSEATS SELECTED:\n")
        for a in self.seats:
            print(f"{a},")
        print(f"\nAMOUNT:{self.amount}\t|\tSTATUS:{self.status}\n")
