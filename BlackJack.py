'''
BLACKJACK Game Implemented using Python 2.7

Created on Jul 13, 2014

@author: aravind krishnakumar
'''
#!/usr/bin/python

import random

#Global Variables to be accessed in both the classes

global creditchip
global chips
chips = 0
creditchip =100

#User class to Hit,Stand down and Double down functions

class User:
    
    #Global Variables
    global usersumnew
    usersum = 0   
    usersumnew = 0
    global sumcard
    sumcard = 0
    global sumtemp
    sumtemp = 0
    global sumvar
    sumvar = 0
   
    #Initial Deal Function
    def deal(self):
        
        global listofcards
        global usersum
        global card1
        global card2
        
        #List of Cards
        cards =  [2,3,4,6,7,8,9,10,'Jack','Queen','King','Aces']
        #Random Selection of Cards
        card1 = (random.choice(cards))
        card2 = (random.choice(cards))

        print("User Cards :")
        print "Card 1 -> ",card1 
        print "Card 2 -> ",card2
        
        #Allocating value for each card
        if card1 in('Jack','Queen','King'):
            sum11 = 10
        elif card1 == 'Aces':
            sum11 = 11
        else:
            sum11 = card1
        
        #Allocating value for each card
        if card2 in('Jack','Queen','King'):
            sum22 = 10
        elif card2 == 'Aces':
            sum22 = 11
        else:
            sum22 = card2
        
        #Adding the randomly generated Cards to a LIST,to keep track of Cards fo the User
        listofcards = [card1,card2]
        usersum = sum11+sum22

        print("User Total :")
        print(usersum)
        
        '''
        If the cards include either Aces with 10,Jack,Queen and King any of these cards they are called as 
        BLACKJACK CARDS and the if user gets these cards they are declared as Winner,without giving the chance for dealer
        '''
        
        if(usersum == 21):
            print("**************************")
            print("BLACK JACK CARDS!")
            print(listofcards)
            print("User Won!!!!")
            print("**************************")
            global creditchip
            global chips
            creditchip = creditchip+chips 
            print("User Credits : ")
            print(creditchip)
            print("Do you want to continue to Play?")
            option = raw_input("Enter yes or no : ")
            if(option == 'no'):
                print("Bye Bye !!!")
                print("Your Final Credit Value : ")
                print(creditchip)
            else:
                try:
                    chips = int(input("Enter the number of chips to Bet:"))
                    if(chips>100):
                        print("Value cannot be greater than be 100!!! Enter again : ")
                        chips = int(input("Enter the number of chips to Bet:"))
                except:
                    print("you must enter an integer")
                    chips = int(input("Enter the number of chips to Bet:"))
    
                while(chips<1):

                    print("Enter Again!!There must be some mistake in your input!!")
                    try:
                        chips = int(input("Enter the number of chips to Bet:"))
                    except:
                        print("you must enter an integer")
                        chips = int(input("Enter the number of chips to Bet:"))
                User2 = User()
                User2.deal()
            
        return(usersum)

    #Returns the User sum for comparing with Dealer's value
    def itreturns(self):
        usersum1 = usersum
        return(usersum1)
    
    #If the user chooses HIT this function will be called
    def Hit(self,chips,double):
        
        #Global Declaration of Values
        global usersumnew
        global count
        count = 0
        count = count + 1
        usersumnew = 0
        
        #Randomly selecting the 3rd Card
        cards = [2,3,4,6,7,8,9,10,'Jack','Queen','King','Aces']
        card3 = (random.choice(cards))
                
        print("User's New Card :")
        print(card3)
        
        #Appending the 3rd Card to already existing list of Cards
        listofcards.append(card3)
        
        print("User new set of Cards :")  
        print(listofcards)
        
        #Calculating the new sum of totals
        for sumcalc in listofcards:
            #Allocating value for each card
            if sumcalc in('Jack','Queen','King'):
                sum41 = 10
            elif sumcalc == 'Aces':
                #If the total sum of the cards is less than 11,then the Ace card is considered as 10
                #else it is taken as 1
                if(usersumnew < 11 ):
                    sum41 = 11
                else:
                    sum41 = 1
            else:
                sum41 = sumcalc
            usersumnew = usersumnew+sum41

        print("User Total :")
        print(usersumnew)
       
       
        #If the Values is above 21 the user is busted
        if(usersumnew>21):
            print("**************************")
            print("User BUSTED!!!!")
            print("**************************")
            #Used to check whether it is a normal Hit or Double Down
            if(double == False):
                global creditchip
                creditchip = creditchip-chips
            else:
                
                creditchip = creditchip-(1.5*chips)
            print("Credits Remaining : ")
            print(creditchip)
        else:
            #Used to check whether it is a normal Hit or Double Down
            if(double == False ):
                #If the User wants to HIT again or If he surrenders ,chooses the appropriate option
                print("Do you want to HIT again?")
                print("Please select one of the option :")
                print("1.HIT")
                print("2.STAND")

                choice =raw_input("Enter the option: ")
                if(choice == '1'):
                    double = False
                    count = count+1
                    User.Hit(self,chips,double)
                elif(choice == '2'):
                    dealer2 = Dealer()
                    dealer2.Stand1(chips,double)
                else:
                    print("Bad Option!!")
            else:
                dealer2 = Dealer()
                dealer2.Stand1(chips,double)
        return(usersumnew)
       
    
    def itreturnsNew(self):
        global usersumnew
        usersumnew1 = usersumnew
        return(usersumnew1)
    
    #If the user chooses double down option,this function will be called
    def doubledown(self,chips): 
        double = True   
        chips1 = chips
        User2 = User()
        User2.Hit(chips1,double)
        
    #If the user decides to SPLIT the cards,this function will be called
    def split(self,chips1):
        global card1
        global card2
        global list1
        global list2
        global sumcard
        global sumtemp
    
        option ='yes'
            
        list1 = [card1]
        list2 = [card2]
        
        User1 = User()
        
        list11 = User1.splitcardgenereator(list1)
        
        print("Please select one of the option :")
        print("1.HIT")
        print("2.STAND")      
        choice =raw_input("Enter the option: ")
        
        #If User Selects 1st Option Dealer Hits the User with Cards
        if(choice == '1'):
            while(option == 'yes'):
                list11 = User1.splitcardgenereator(list11)
                if(sumcard>21):
                    print("***********User Busted***********")
                    global creditchip
                    global chips
                    creditchip = creditchip-chips 
                    print("Credits Left : ")
                    print(creditchip)
                    '''
                    If the user set1 cards crosses the limit 21,then the first set of cards will be 'busted'
                    Then the second sets of cards will be generated
                    '''
                    print("##########Set 2 Cards : ############")
                    User1.split1(chips1)
                else:
                    print("Do you want to hit again? ")  
                    option = raw_input("Enter yes or no : ") 
                    if(option == 'yes'):
                        list11 = User1.splitcardgenereator(list11)
                    else:
                        print("***************************")
                        print("Set 1: Final List of Cards : ")
                        print(list11)
                        print("Sum of the Cards : ")
                        sumtemp = sumcard
                        print(sumtemp)
                        print("***************************")
                    
                        print("##########Set 2 Cards : ############")
                        User1.split1(chips1)
                    
                return list11 
                         
            #If User Selects 2nd Option Stand Function is called
        elif(choice == '2'):
                global sumcar
                print("***************************")
                print("Set 1 Final List of Cards:")
                print(list11)
                print("Sum of the Cards : ")
                sumtemp = sumcard
                print(sumtemp)
                print("***************************")
                print("##########Set 2 Cards : ############")
                User1.split1(chips1)
        else:
            print("Bad Option!!")
            
    def splitreturns1(self):
        global sumtemp
        sum1 = sumtemp
        print(sum1)
        return(sum1)
        
    #Card Generator function - for randomly generating the cards    
    def splitcardgenereator(self,listS):
    
        cards = [2,3,4,6,7,8,9,10,'Jack','Queen','King','Aces']
        card3 = (random.choice(cards))
        print("User's New Card : ")
        print(card3)
        listS.append(card3)

        global sumcard
        sumcard = 0
        
        for sum11 in listS:
            #Allocating value for each card
            if sum11 in('Jack','Queen','King'):
                sumcard1 = 10
            elif sum11 == 'Aces':
                #If the total sum of the cards is less than 11,then the Ace card is considered as 11
                #else it is taken as 1
                if(sumcard < 11 ):
                    sumcard1 = 11
                else:
                    sumcard1 = 1
            else:
                sumcard1 = sum11
            sumcard = sumcard+sumcard1
            
        print("Sum of Cards ")
        print(sumcard) 
        print("List of Cards")      
        print(listS)     
        return(listS)
    
    def split1(self,chips1):
        
        global sumvar
        global sumcard
        
        list22 = User1.splitcardgenereator(list2)
        
        print("Please select one of the option :")
        print("1.HIT")
        print("2.STAND")       
        choice =raw_input("Enter the option: ")
        
        option = 'yes'
        #If User Selects 1st Option Dealer Hits the User with Cards
        if(choice == '1'):
            while(option == 'yes'):
                list22 = User1.splitcardgenereator(list22)    
                if(sumcard > 21):
                    print("**********User Busted************")
                    global creditchip
                    global chips
                    creditchip = creditchip-chips 
                    print("Credits Left : ")
                    print(creditchip)
                    Dealer2 = Dealer()
                    Dealer2.StandSplit(chips1)
                    break
                else:
                    print("Do you want to hit again? ")  
                    option = raw_input("Enter yes or No : ") 
                    if(option == 'yes'):
                        list22 = User1.splitcardgenereator(list22)
                    else:
                    
                        print("***************************")
                        print("Set 2 Final List of Cards:")
                        print(list22)
                        sumvar = sumcard
                        print("Sum of Cards : ")
                        print(sumvar)
                        print("***************************")
                    
                    Dealer2 = Dealer()
                    Dealer2.StandSplit(chips1)
                    Dealer2.StandSplit1(chips1)
                    
            return list22 
                         
            #If User Selects 2nd Option Stand Function is called
        elif(choice == '2'):
            global sumcard22
            print("***************************")
            print("Set 2 Final List of Cards:")
            print(list22)
            sumvar = sumcard
            print("Sum of Cards : ")
            print(sumvar)
            print("***************************")        
            Dealer2 = Dealer()
            Dealer2.StandSplit(chips1)
            Dealer2.StandSplit1(chips1)
        else:
            print("Bad Option!!")
        
        print("Please select one of the option :")
        print("1.HIT")
        print("2.STAND")
              
        choice =raw_input("Enter the option: ")
        
    def splitreturns2(self):
        global sumvar
        sum2 = sumvar
        return(sum2)
    
    
#Dealer Class ,handles the operations of the dealer
class Dealer(User):
        global Dealercards
        global DealercardsVisual
        global dealersum
        global dealersumNew
        
        #Generation of Random Cards
        def cardgenerator(self,sum1):
            global Dealercards
            
            cards = [2,3,4,6,7,8,9,10,'Jack','Queen','King','Aces']
            card = (random.choice(cards))
            #Allocating the values for the Cards
            if card in('Jack','Queen','King'):
                card1 = 10
                print("Dealer's Newly Generated Card : ")
                print(card)
            elif card == 'Aces':
                if(sum1 < 11):
                    card1 = 11
                    print("Dealer's Newly Generated Card : ")
                    print(card)
                else:
                    card1 = 1 
                    print("Dealer's Newly Generated Card : ")
                    print(card)           
            else:
                card1 = card
                print("Dealer's Newly Generated Card : ")
                print(card1)
            
            Dealercards.append(card1)
            DealercardsVisual.append(card)
            print("Dealer's Cards : ")
            print(DealercardsVisual)
            return card1

        #Calculating the Sum of Cards
        def sumcalc(self,sum1):
                               
                sum2 = Dealer.cardgenerator(self,sum1)
                sum1 = sum1+sum2
                return(sum1)

        #Validating the Sum

        '''

        If the Dealer Car Sumation values is less than 17 ,he can draw cards from Discard Holder
        Random Card is genereated using the cardgenerator function
        The New card value is added to the existing sum in sumcalc function
        The checksum function checks for the new value if it is less than 17,
        then a new card is generated
        If the generated new card is more than 21,the dealer gets busted
              
        '''
        
        def checksum(self,dealersum):
                
                sum1 = dealersum
                sum2 = Dealer.sumcalc(self,sum1)                   
                if(sum2 < 17):
                    sum2 = Dealer.checksum(self, sum2)
                return(sum2)
                
        #Initial card generation of Dealer's cards
        def Ddeal(self):
                global dealersum
                global Dealercards
                global DealercardsVisual

                cards = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Aces']
    
                dealercard1 = (random.choice(cards))
                dealercard2 = (random.choice(cards))

                print("Dealer Cards :")
                print "Card 1 -> ",dealercard1
                print "Card 2 -> Folded"
                
                
                if dealercard1 in('Jack','Queen','King'):
                    sum1 = 10
                elif dealercard1 == 'Aces':
                    sum1 = 11
                else:
                    sum1 = dealercard1
    
                if dealercard2 in('Jack','Queen','King','Aces'):
                    sum2 = 10
                elif dealercard2 == 'Aces':
                    sum1 = 11
                else:
                    sum2 = dealercard2
                
                Dealercards = [dealercard1,dealercard2]
                DealercardsVisual = [dealercard1,dealercard2]
    
                dealersum = sum1+sum2
                
                if(dealersum == 21):
                    print("**************************")
                    print("BLACK JACK CARDS!")
                    print(DealercardsVisual)
                    print("Dealer Won!!!!")
                    print("**************************")
                    global creditchip
                    global chips
                    creditchip = creditchip-chips 
                    print("User Credits : ")
                    print(creditchip)
                    print("Do you want to continue to Play?")
                    option = raw_input("Enter yes or no : ")
                    if(option == 'no'):
                        print("Bye Bye !!!")
                        print("Your Final Credit Value : ")
                        print(creditchip)
                    else:
                        try:
                            chips = int(input("Enter the number of chips to Bet:"))
                            if(chips>100):
                                print("Value cannot be greater than be 100!!! Enter again : ")
                                chips = int(input("Enter the number of chips to Bet:"))
                        except:
                            print("you must enter an integer")
                            chips = int(input("Enter the number of chips to Bet:"))
                        while(chips<1):

                            print("Enter Again!!There must be some mistake in your input!!")
                            try:
                                chips = int(input("Enter the number of chips to Bet:"))
                            except:
                                print("you must enter an integer")
                                chips = int(input("Enter the number of chips to Bet:"))
                        User2 = User()
                        User2.deal()
                        Dealer2 = Dealer()
                        Dealer2.Ddeal()    

                
        def Stand(self,chips,double):
            '''
            If the dealer sum of cards is greater than 17,then it is checked with the user sum of cards
            the winner is declared based on who has greater sum
            
            If the dealer sum is less than 17,then a new card is generated using the cardgenerator function
            and the newsum is calculated with the updated total.
            '''
            if(dealersum>17):
                if(dealersum>User().itreturns()):
                    print("User Value :")
                    print(User().itreturns())
                    print("Dealer Sum : ")
                    print(dealersum)
                    print("**************************")
                    print("Dealer's Cards : ")
                    print(DealercardsVisual)
                    print("Dealer Won")
                    print("**************************")           
                    global creditchip
                    creditchip = creditchip-chips
                    print("Credits Remaining : ")
                    print(creditchip)
                
                elif(dealersum == User().itreturns()):
                    print("******Dealer and User Sum's are Equal******")
                    print("User Value :")
                    print(User().itreturns())
                    print("Dealer's Cards : ")
                    print(DealercardsVisual)
                    print("Credits Remaining : ")
                    print(creditchip)
                
                else:
                    print("User Value :")
                    print(User().itreturns())
                    print("Dealer's Cards : ")
                    print(DealercardsVisual)
                    print("Dealer Sum :")
                    print(dealersum)
                    print("**************************")
                    print("User Won")
                    print("**************************")                    
                    creditchip = creditchip+chips
                    print("Credits Remaining : ")
                    print(creditchip)
                    
            else:
                dealersumNew = Dealer.checksum(self,dealersum)
                
                if(dealersumNew>User().itreturns()):
                    print("Dealer Sum : ")
                    print(dealersumNew)
                    if(dealersumNew>21):
                        print("**************************")
                        print("Dealer Busted!!!")
                        print("User Won!")
                        print("**************************")
                        if(double == False):
                            creditchip = creditchip+chips
                        else:
                            creditchip = creditchip+(1.5*chips)
                        print("Credits Remaining : ")
                        print(creditchip)
                        
                    else:
                        print("User Value :")
                        print(User().itreturns())
                        print("**************************")
                        print("Dealer's Cards : ")
                        print(DealercardsVisual)
                        print("Dealer Won")
                        print("**************************")
                        if(double == False):
                            creditchip = creditchip-chips
                        else:
                            creditchip = creditchip-(1.5*chips)
                        print("Credits Remaining : ")
                        print(creditchip)
                
                elif(dealersum == User().itreturns()):
                        print("******Dealer and User Sum's are Equal******")
                        print("User Value :")
                        print(User().itreturns())
                        print("Dealer's Cards : ")
                        print(DealercardsVisual)
                        print("Credits Remaining : ")
                        print(creditchip)
                else:
                    print("User Value :")
                    print(User().itreturns())
                    print("Dealer's Cards : ")
                    print(DealercardsVisual)
                    print("Dealer Sum :")
                    print(dealersumNew)
                    print("**************************")
                    print("User Won")
                    print("**************************")
                    if(double == False):
                            creditchip = creditchip+chips
                    else:
                            creditchip = creditchip+(1.5*chips)
                    print("Credits Remaining : ")
                    print(creditchip)
        
        def Stand1(self,chips,double):
            
            global dealersumNew
            dealersumNew = 0
        
            if(dealersum>17):
                if(dealersum>User().itreturnsNew()):
                    print("User Value :")
                    print(User().itreturnsNew())
                    print("Dealer Sum : ")
                    print(dealersum)
                    print("**************************")
                    print("Dealer's Cards : ")
                    print(DealercardsVisual)
                    print("Dealer Won")
                    print("**************************")
                    global creditchip
                    if(double == False):
                            creditchip = creditchip-chips
                    else:
                            creditchip = creditchip-(1.5*chips)
                    print("Credits Remaining : ")
                    print(creditchip)
                    
                elif(dealersum == User().itreturnsNew()):
                    print("******Dealer and User Sum's are Equal******")
                    print("User Value :")
                    print(User().itreturnsNew())
                    print("Dealer's Cards : ")
                    print(DealercardsVisual)
                    print("Credits Remaining : ")
                    print(creditchip)
                    
                else:
                    print("User Value :")
                    print(User().itreturnsNew())
                    print("Dealer Sum :")
                    print(dealersum)
                    print("Dealer's Cards : ")
                    print(DealercardsVisual)
                    print("**************************")
                    print("User Won")
                    print("**************************")
                    if(double == False):
                            creditchip = creditchip+chips
                    else:
                            creditchip = creditchip+(1.5*chips)
                    print("Credits Remaining : ")
                    print(creditchip)
                    
            else:
                dealersumNew = Dealer.checksum(self,dealersum)
                
                if(dealersumNew>User().itreturnsNew()):
                    print("Dealer Sum : ")
                    print(dealersumNew)
                    if(dealersumNew>21):
                        print("**************************")
                        print("Dealer Busted!!!")
                        print("User Won!")
                        print("**************************")
                        if(double == False):
                            creditchip = creditchip+chips
                        else:
                            creditchip = creditchip+(1.5*chips)
                        print("Credits Remaining : ")
                        print(creditchip)
                        
                    else:
                        print("User Value :")
                        print(User().itreturnsNew())
                        print("**************************")
                        print("Dealer's Cards : ")
                        print(DealercardsVisual)
                        print("Dealer Won")
                        print("**************************")
                        if(double == False):
                            creditchip = creditchip-chips
                        else:
                            creditchip = creditchip-(1.5*chips)
                        print("Credits Remaining : ")
                        print(creditchip)
                        
                elif(dealersum == User().itreturnsNew()):
                    print("******Dealer and User Sum's are Equal******")
                    print("User Value :")
                    print(User().itreturnsNew())
                    print("Dealer's Cards : ")
                    print(DealercardsVisual)
                    print("Credits Remaining : ")
                    print(creditchip)
                
                else:
                    print("User Value :")
                    print(User().itreturnsNew())
                    print("Dealer Sum :")
                    print(dealersumNew)
                    print("Dealer's Cards : ")
                    print(DealercardsVisual)
                    print("**************************")
                    print("User Won")
                    print("**************************")
                    if(double == False):
                            creditchip = creditchip+chips
                    else:
                            creditchip = creditchip+(1.5*chips)
                    print("Credits Remaining : ")
                    print(creditchip)
                    
        def StandSplit(self,chips):         
                    
                    global dealersum
                    global dealersumNew
                    calc = User1.splitreturns1()
                    
                    if(dealersum>17):
                        if(dealersum>calc):
                            print("User Value :")
                            print(calc)
                            print("Dealer Sum : ")
                            print(dealersum)
                            print("**************************")
                            print("Dealer's Cards : ")
                            print(DealercardsVisual)
                            print("Dealer Won")
                            print("**************************")
                            global creditchip
                            creditchip = creditchip-chips
                            print("Credits Remaining : ")
                            print(creditchip)
                    
                        elif(dealersum == calc):
                            print("******Dealer and User Sum's are Equal******")
                            print("User Value :")
                            print(calc)
                            print("Dealer's Cards : ")
                            print(DealercardsVisual)
                            print("Credits Remaining : ")
                            print(creditchip)
                    
                        else:
                            print("User Value :")
                            print(calc)
                            print("Dealer Sum :")
                            print(dealersum)
                            print("Dealer's Cards : ")
                            print(DealercardsVisual)
                            print("**************************")
                            print("User Won")
                            print("**************************")
                            creditchip = creditchip+(chips)
                            print("Credits Remaining : ")
                            print(creditchip)
                    
                    else:
                        dealersumNew = Dealer.checksum(self,dealersum)
                
                        if(dealersumNew > calc):
                            print("Dealer Sum : ")
                            print(dealersumNew)
                            if(dealersumNew>21):
                                print("**************************")
                                print("Dealer Busted!!!")
                                print("User Won!")
                                print("**************************")
                                creditchip = creditchip+(chips)
                                print("Credits Remaining : ")
                                print(creditchip)
                        
                            else:
                                print("User Value :")
                                print(calc)
                                print("**************************")
                                print("Dealer's Cards : ")
                                print(DealercardsVisual)
                                print("Dealer Won")
                                print("**************************")
                                creditchip = creditchip-(chips)
                                print("Credits Remaining : ")
                                print(creditchip)
                        
                        elif(dealersum == calc):
                            print("******Dealer and User Sum's are Equal******")
                            print("User Value :")
                            print(User().itreturnsNew())
                            print("Dealer's Cards : ")
                            print(DealercardsVisual)
                            print("Credits Remaining : ")
                            print(creditchip)
                
                        else:
                            print("User Value :")
                            print(calc)
                            print("Dealer Sum :")
                            print(dealersumNew)
                            print("Dealer's Cards : ")
                            print(DealercardsVisual)
                            print("**************************")
                            print("User Won")
                            print("**************************")
                            creditchip = creditchip+chips
                            print("Credits Remaining : ")
                            print(creditchip)
        
        def StandSplit1(self,chips):
            
            global dealersum
            global dealersumNew
            global DealercardsVisual
            deal = 0
            sum = 0
            sum1 = 0
            
            calc = User1.splitreturns2()
            
            for sum in DealercardsVisual:
                #Allocating value for each card
                if sum in('Jack','Queen','King'):
                    sum1 = 10
                elif sum == 'Aces':
                    #If the total sum of the cards is less than 11,then the Ace card is considered as 11
                    #else it is taken as 1
                    if(deal < 11 ):
                        sum1 = 11
                    else:
                        sum1 = 1
                else:
                    sum1 = sum
            
                deal = deal+sum1
                
            if(deal>calc):
                    print("User Value :")
                    print(calc)
                    print("Dealer Sum : ")
                    print(deal)
                    if(deal>21):
                        print("**************************")
                        print("Dealer Busted!!!")
                        print("User Won!")
                        print("**************************")
                        global creditchip
                        creditchip = creditchip+(chips)
                        print("Credits Remaining : ")
                        print(creditchip)
                    else:
                        print("**************************")
                        print("Dealer's Cards : ")
                        print(DealercardsVisual)
                        print("Dealer Won")
                        print("**************************")                 
                        creditchip = creditchip-chips
                        print("Credits Remaining : ")
                        print(creditchip)
                    
            elif(deal == calc):
                    print("******Dealer and User Sum's are Equal******")
                    print("User Value :")
                    print(calc)
                    print("Dealer's Cards : ")
                    print(DealercardsVisual)
                    print("Credits Remaining : ")
                    print(creditchip)
                    
            else:
                print("User Value :")
                print(calc)
                print("Dealer Sum :")
                print(deal)
                print("Dealer's Cards : ")
                print(DealercardsVisual)
                print("**************************")
                print("User Won")
                print("**************************")                
                creditchip = creditchip+(chips)
                print("Credits Remaining : ")
                print(creditchip)
    
option = 'yes'           
while(option == 'yes'): 
   
    try:
        chips = int(input("Enter the number of chips to Bet:"))
        if(chips>100):
            print("Value cannot be greater than be 100!!! Enter again : ")
            chips = int(input("Enter the number of chips to Bet:"))
    except:
            print("you must enter an integer")
            chips = int(input("Enter the number of chips to Bet:"))
            while(isinstance(chips,int)):
                chips = int(input("Enter the number of chips to Bet:"))
    
    while(chips<1):

            print("Enter Again!!There must be some mistake in your input!!")
            try:
                chips = int(input("Enter the number of chips to Bet:"))
            except:
                print("you must enter an integer")
                chips = int(input("Enter the number of chips to Bet:"))
    
               
    if(creditchip !=0 ):
        #User1 Created            
        User1 = User()
        User1.deal()

        #Dealer Created
        Dealer1 = Dealer()
        Dealer1.Ddeal()
    
        print("Please select one of the option :")
        print("1.HIT")
        print("2.STAND")
        print("3.DOUBLE DOWN")
        global card1
        global card2
        if(card1 == card2):
            print("4.SPLIT")

        choice =raw_input("Enter the option: ")
        
        #If User Selects 1st Option Dealer Hits the User with Cards
        if(choice == '1'):
            double = False      
            User1.Hit(chips,double)
        
        #If User Selects 2nd Option Stand Function is called
        elif(choice == '2'):
            double = False   
            Dealer1.Stand(chips,double) 
        
        elif(choice == '3'):
            double = True       
            User1.doubledown(chips)
        
        elif(choice == '4'):
        #If both the cards are same then this option will be enabled
            if(card1 == card2):
                double = True       
                User1.split(chips)
            else:
                print("Bad Option!!")
        
        else:
            print("Bad Option!!")
    
        print("Do you want to continue to Play?")
        option = raw_input("Enter yes or no : ")
        if(option == 'no'):
            print("Bye Bye !!!")
            print("Your Final Credit Value : ")
            print(creditchip)
        elif(option!='yes'):
            print("Wrong Input!! Enter Again please ")
            print("Do you want to continue to Play?")
            option = raw_input("Enter yes or no : ")        
        else:
            option ='yes'
    
    else:
        print("You have lost all Credits!!No Plays anymore!!")
        option = 'no'
   

