def sum(a,b):
    return int(a)+int(b)

def subtract(a,b):
    return int(a)-int(b)

def multiply(a,b):
    return int(a)*int(b)

def divide(a,b):
    return int(a)/int(b)


#get_string = input()
get_string= input() #get_string is "5 - 5"

operations = '+-*/ '

for i in get_string:
    if not (i.isnumeric() or operations.find(i) > -1):#this is a solution
#    if not i.isnumeric() and operations.find(i) == -1: #this is the other   
        print("invalid input")
        exit()

try:
    #does this
    index_plus = get_string.find("+")
    index_minus = get_string.find("-")
    index_multiply = get_string.find("*")
    index_divide = get_string.find("/")  


    if index_plus > -1: #get_string.find("+") = find an index of + or it gives -1
        #Ok, so in this case? 
        #it gives -1 !
        #So what will the code do in this case?  if get_string.find("+") --> if -1: 
        #if -1: <<<--- is true!
        # so it does this
        first = get_string[:index_plus] #then this --> get_string[:-1]... But -1 is not a valid index :O
        #So it gives an error
        second = get_string[index_plus+1:]
        print(sum(first, second))

    if index_minus > -1:
        first = get_string[:index_minus]
        second = get_string[index_minus+1:]
        print(subtract(first, second))

    if index_multiply > -1:
        first = get_string[:index_multiply]
        second = get_string[index_multiply+1:]
        print(multiply(first, second))

    if index_divide > -1:
        first = get_string[:index_divide]
        second = get_string[index_divide+1:]
        print(divide(first, second))
except:
    print(" :( ")#goes here


#Hi beautiful :D
#Hi Handsome :D
#Hahahaha so cuteeeeeeeeeeeeee <3
#we're goind to start to make a calculator today, ready? <3
#Ready! :D
#Ok! So first we'll make a text one, without graphical interface, we'll add it later. Ok?
#OK!
#Good! Then so 내 사랑, make me a simple code that get a string as input and put it in a varaible!
#What I should set the variavle name?
#Whatever you want <3 you're the boss here <3
#Hahahahaha ok!
#Is it right you said?
#print get_string and run it <3
#There's an error 
#yeah, weird
#try now
#hmm, this is weird
#I think it happened before too!
#run this
#Can you see this?
#Yes <3
#It works <3
#yayyyyyy <3 And you changed your color <3
#I didn't change it and your's is also changed hahaha
#Now I see you pink, which is cute hahahaha
#Hahahahaha you are orange <3
#And you are beautiful <3
#Should we type at the same time ? Can we
#Oh we can hahaha, yes!

#I'm not sure about what happens hahahaha
#seems like it works hahaha
#In the liveshare tab do you see the 'session chat' voice?
#voice?
#option hahaha
#under chat channels
#I only can see Session Chat!
#that's the one! what happens if you click it?
#I sent you to the kakao haha
#saw that <3
#try to type there!
#can you see my message in chat?
#Yes I can see!