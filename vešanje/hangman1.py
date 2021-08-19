import mysql.connector as mysql
from connection import *

class Base:
    def choose_word(self):
        con=Connection.getInstance()
        cursor=con.cursor()
        cursor.execute("SELECT word FROM wordsList")
        words = cursor.fetchall()
        print(words)
        for word in words:
            print(word)
        print("***************************************************")
        search_word=''
        index_word =''
        indicator=True
        while indicator  :
            index_word = int(input("Choose word index : "))
            gaps = ''
            if index_word in range(len(words)):
                print("Exists index")
                for i  in range(len(words)) :
                    if index_word== i:
                        search_word=str(words[i])
                        gaps = '-'*(len(search_word)-5)
                        indicator=False
            else:
                print("Index does not exists,try again!")
            search_word=search_word.strip("(").strip(")").strip("'").strip(",").strip("'")
            if indicator==False:
                break 
        print("The search word has :", len(gaps) ,"letters")
        print(gaps) 
        pictures = ( '''
 +---+
 |   |
     |
     |
     | ''','''
 +---+
 |   |
 O   |
     |
     | ''', '''
 +---+
 |   |
 O   |
/    |
     | ''' , '''
 +---+
 |   |
 O   |
/ \  |
     | ''' , '''
 +---+
 |   |
 O   |
/|\  |
     | ''' , '''
 +---+
 |   |
 O   |
/|\  |
/    | ''' , '''
 +---+
 |   |
 O   |
/|\  |
/ \  | ''' )
        passLetter=[]
        mistake=0 
        while mistake<6 :
            letter = input("Enter letter : ") 
            if letter==int:
                print("False man!")
            if letter in search_word :
                print("Letter Exists")
                print("Move on..")
                passLetter.append(letter)
                print(passLetter)
            else :
                print("Letter does not exists!")
                mistake+=1
                print("This is mistake number : " ,mistake)
                print(gaps)
            if letter in passLetter:
                print("This letter was already choosen,choose another one!")
            print(pictures[mistake])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            if mistake==6 :
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Game Over,You Are a Hanged Man !!!")
                print("Search Word is : ",search_word)
                break
            for i in range(len(search_word)):
                gaps=list(gaps)
                if letter==search_word[i]:
                    gaps[i]=gaps[i].replace('-',letter)
                    print(gaps)
            word = input("Try to guess the word : ")
            if word==search_word:
                print("The Search Word is : ",search_word)  
                print("BRAVO,Mission acomplished!!!")
                break
            else :
                print("You did not guess,try again... ")
            if '-'  in gaps:
                print("Move on...")
            else :
                print("BRAVO,You guessed the word!") 
                print("***************************************************")
                print(gaps)
                if len(gaps)==6:
                    gaps=str(gaps[0]+gaps[1]+gaps[2]+gaps[3]+gaps[4]+gaps[5])
                elif len(gaps)==7:
                    gaps=str(gaps[0]+gaps[1]+gaps[2]+gaps[3]+gaps[4]+gaps[5]+gaps[6])
                elif len(gaps)==8 :
                    gaps=str(gaps[0]+gaps[1]+gaps[2]+gaps[3]+gaps[4]+gaps[5]+gaps[6]+gaps[7])
                elif len(gaps)==9 :
                    gaps=str(gaps[0]+gaps[1]+gaps[2]+gaps[3]+gaps[4]+gaps[5]+gaps[6]+gaps[7]+gaps[8])
                elif len(gaps)==10:
                    gaps=str(gaps[0]+gaps[1]+gaps[2]+gaps[3]+gaps[4]+gaps[5]+gaps[6]+gaps[7]+gaps[8]+gaps[9])
                elif len(gaps)==11:
                    gaps=str(gaps[0]+gaps[1]+gaps[2]+gaps[3]+gaps[4]+gaps[5]+gaps[6]+gaps[7]+gaps[8]+gaps[9]+gaps[10])
                elif len(gaps)==12 :
                    gaps=str(gaps[0]+gaps[1]+gaps[2]+gaps[3]+gaps[4]+gaps[5]+gaps[6]+gaps[7]+gaps[8]+gaps[9]+gaps[10]+gaps[11])
                elif len(gaps)==13 :
                    gaps=str(gaps[0]+gaps[1]+gaps[2]+gaps[3]+gaps[4]+gaps[5]+gaps[6]+gaps[7]+gaps[8]+gaps[9]+gaps[10]+gaps[11]+gaps[12])
                print("The Search Word is : ", gaps)
                break
                
            print("***************************************************")
    def playAgain(self):
        while 1:
            again=input("Do You want to play again?  ")
            if again=="yes":
                base=Base()
                base.choose_word()
            else:
                print("Good Bye")
                break
base = Base()
base.choose_word()
base.playAgain()

    
