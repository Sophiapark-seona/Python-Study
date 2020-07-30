#in python, a regular expression is written like this
# re.match( '[0-9]*' , '1234' ) 
#as you can see, we are using the 0-9 rule we said earlier
#'1234' is the string we want to check
# * <----- this means that we match from 0 or more matches with our rule
# so the string 'asdc' would match too, since we accept 0 matches too hahaha
#If we don't add * 'asdc' is not match right?
#right!
#But if we don't add anything at all, it will only match the first numeric character
#To tell him that we want to match one or more character, we can use +, like this yes <3
# re.match( '[0-9]+' , '1234' ) 
#with +, it means that the rule will match one or more (infinite) numeric characters
#better, right? Right!!
#let's see what happens if we match our input string with this last rule
#put the result of that re.match in a variable and print it!
#ok, let's try it!<3
#Which one?
#the one you wrote, just launch the code <3
#should we import something?
#oh, right!
#wait, I don't rememebr the name hahaha
#Take your time!
#it was easy hahahaha
#Yes it's only 're' hahaha
#let's try now!
#It says : <re.Match object; span=(0, 4), match='1234'>
#Oh, sorry, it didn't open the terminal for me so I didn't see hahaha
#It's ok <3
#always so sweet <3<3
#ok, so it matchs our whole string!
#let's change 1234 to something with letters!
#<re.Match object; span=(0, 2), match='12'>
#yes, so it's working as expected, right? 
#Right, but what is span?
#it's from what index to what index our match is in the string!
#no, sorry, index and lenght

#The first index and lenth?
#yes! from index 0, 2 characters
#Got it <3
#you always understand everything immediately <3<3<3
#Because I have a nice teacher <3<3<3
#Be careful, or I'll want a big reward hahahahaaha
#Hahahahahaha okay <3 <3
#Ok! now!
#Other than numbers, we can also add other characters
#it's pretty easy to do, you just have to add them to the list! hahaha
#like this! Let's say that I also want to match the character '.'
#I can write
#[0-9.]+
#Easy! Yes it's easy!
#Now, what would we write if we want to match a valid string for our calculator?
#it has to include numbers, operations and space!
#You were smart so you already written it in the code hahaha
#I remember hahaha
#Then should I add it in the if that we check the
#for now, onlu add it to the re here
#perfect <3
#let's try to see what happens like this
#<re.Match object; span=(0, 6), match='1 + 2 '>
#Exactly! seems like it works, right? Yes right
#So, let's try to print only the match
#Can you imagine how to do it?
#Maybe using match? hmm
#you have everything inside the variable 'regular'
#regular is made of span, and match
#You still don't know this, but maybe you can guess it
#there is a way to only access match by writing regular..... (something instead of the dots)
#Try to guess for fun hahaha
#regular.match something like that?
#Actually, it's exactly like that <3
#hahahaha <3
#I knew that you are smart <3
#hahaha, ok, he's annoying hahaha
#Yes !!
#this is about the 3rd topic, so I wanted you to guess this thing ayway, even if it doesn't work now
#Then maybe it's an array?
#let's try regular[1]
#hahah this was my fault because i don't remember python syntax hahaha
#HAhahaha I understand it <3
#Give me a sec to search <3
#<3<3
#<3<3
#Ok, try regular.groups(0)
#annoying hahaha
#It's interesting though hahaha
#try like this
#hahaha damn it hahahaha
#I'm little glad because it's our study now hahahaha
#hahahaha it's actually not important and we can skip it, but it's annoying hahaha
#I'll search it later, for now let's skip it because it's late!
#Okay <3<3
#thank you <3<3
#Ok! so, what happens if we want to see fi there is any invalid character?
#We want to accept our valid characters, and match only the wrong ones!
#luckily, there is a way to do that easily!
#you just have to add ^ before the rule!
# ^ = not! easy!
# ^ means not?
#Correct <3
#like this ^[0-9]
#let's try it!
#in the re.match?
#yes <3
#<re.Match object; span=(0, 6), match='1 + 2 '>
#What is difference with the previous code?
#nothing, which is weird hahahaha
#try like this
#It says 'None' hahaha
#this time, it's correct! because it fails immediately at the start of the string!
#try now
#Now it works, right?
#Ah! I understood, but 1+2 can't be in the first?
#yeah, if we use the match function like this!
#there are many other functions too, for example, let's try the search
#regular = re.search('[^0-9+-/* ]+', 'sdasdadass 1 + 2') <---- like this!
#What if we write 1 + 2 first?
#OH it works!
#yeah <3
#the match function is for complete matches, I think.
#the search fucntion is for partial matches
#This is my guess, I never actually used them in python hahaha
#I see, it's very new for me too hahaha
#anyway, what happens if we write only a good string? like 1 + 2
#it works well right?
#it's perfect I'd say <3
#So I think that we have a new way to check if our string is correct, right?
#Right! Then we shouldn't use ^ right?
#You could check if the string is all valid without ^
#Or check if there is something invalid including ^
#The first match all the numbers and operations, and the second match invalid characters
#Since we're lazy,  I thin it's better not to write a way to understand if the match is completely right or not
#So it's smarter to use ^ and check if regular is different from None
#Makes sense? It's a little difficult maybe
#It's little confusing but understood <3
#Are you sure?<3 I can explain better <3
#I think I can understand more better trying the code <3
#Then let's do that! <3
#At the real code?
#Yes, let's comment the for and use a regex (regular expression) instead

import re
#regular = re.search('[^0-9+-/* ]+', '1 + 2')
#print(regular)



sum = lambda a, b : int(a) + int(b)

#you removed one thing!
#the lambda is correct, but you removed it from the function <3
#no, the return is automatic <3
#look at the subtract function,something is different
#Good<3
#let's test it first
# it works <3
#beacuase you are amazing <3
#My teacher is more <3
#You'll teacher will ask for a good payment <3
#Hahahahaha okay, I will!
#Now let's do the others!
#Amazing as always <3 LEt's test everything!
#Yayyy!
#Best programmer ever <3
#Hahahahaha Thank you <3
#Now, let's go back to the bottom for the next topic!
subtract = lambda a, b: int(a)-int(b)

multiply = lambda a, b:int(a)*int(b)

divide = lambda a, b: int(a)/int(b)

#shall we write here? or on kakao?
#Anywhere you are free!
#let's try here first, this way you have the explenation saved in the file!
#Okay, good idea!
#<3
#get_string = input()
get_string= input() #get_string is "5 - 5"

operations = '+-*/ '

#put it here
#I wanted to leave you the for too for future reference <3
#You are really wonderful <3<3
#Not as much as you <3<3
#Let's try it <3
#Oh, right! we can't declare it inside the if hahaha
#let's comemnt the one at the top

#Ok, the problem is that None is not a string, it's a special word!
#to compare it, you have to write like this
#regular is None
#yeah! hahaha this is better
#It's right? hahaha
#It works perfectly, right?<3
#Yeyyy <3<3
#Good job <3<3<3 We finished our basic version of the calculator!
#Wow! Finally we did <3 Then there's left 1 topic?
#Yes, a very very important one, much more than this last ones!
#Yeyyyy! I'm so curious but we should study it next time hahaha
#Yes <3 It was already planned like this, don't worry <3
#Thanks a lot today too, my teacher <3<3<3
#Please reward me well <3<3<3 hahahaha
#What do you want teacher hahahaha
#I think it's better if you decide, trust me hahahahaha
#You made me laugh hahahahaha <3 Let's meet at the kakao!
#Then my day was worth it! <3<3<3
#To kakao!<3


regular = re.search('[^0-9+-/* ]+', get_string)
if not regular is None: 
    print("invalid input")
    exit()

#for i in get_string:
#    if not (i.isnumeric() or operations.find(i) > -1):#this is a solution
#    if not i.isnumeric() and operations.find(i) == -1: #this is the other   
#        print("invalid input")
#        exit()

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


#Ok, first topic! Ready?ㅋㅋㅋㅋㅋ
#ready!
#Ok, the first topic are called lambda expressions! Have you ever heard of them? 
#Yes!
#Wow! this makes things easier hahahahaAre they already clear to you?
#Not that clear but I understood the idea of lambda!
#Ok, then let's do them after I explain a little bit!
#to be short, lambda expressions are a way to write a function very fast and not wasting space
#instead of writing
#function f (a,b) {
#return a+b;
#}
#we can write something like (a,b) => a+b
#This lets us not waste space and time writing a lot.
#It also has other uses, but for now let's stop at this one
#No, wait, is it clear until here?
#Yes I am teacher <3
#So cute <3<3<3 You get A+ <3
# hahahahaha <3
#Now, in javascript they are written similarly to how I writter earlier
#in python the idea is the same, but the synatx is a little different
#it should be like this
#lambda a : a+1
#I'll check now, give me a sec, but I'm almost sure hahaha
#Ok, take your time!
#you have to write lambda apparently hahaha
#How can I do that?
#you have to declare it as if it was a variable, by writing it like that (lambda input : function)
#For example, lambda a : a + 5
#Try to write me here in a comment a lambda to divide the number by 10
#lambda a : a / 10
#Perfect as always <3
#You first <3
#I wanted to type <3 <3 hahaha
#And I want to see them <3 <3
#Now, what if we need many parameters?
#it's easy! it's enough to write
#lambda a,b : a + b 
#this is the same as what I wrote before in c-like language ---> (a,b) => a+b
#Clear?
#Clear!
#Ok, now we only need to know how to use it, right?
#Right :)
#To use it, we just need to assign it to a variable
#like this
# f = lambda a,b : a + b
#Easy, right?
#Yes, it's easy!
#and to use it, we jsut do it like this f(1,3)
#Done! :D
#Yeyy!
#Now, can we replace our operation functions with lambdas since they are very simple?
#Yes I'll try!
#Good <3
#Where I need to start? hahaha
#hahaha <3
#Ok, we have some functions
#like define sum(.....) etc etc
#instead of writing all of that, I want only one row of a lambda like sum = lambda .... etc etc
#Then I don't need functions or I should fix them?
#you don't need functions! we will replace them with lambdas
#May I start from the top now?
#응 <3
#<3<3
#Ok! Great job, you were already perfect before starting <3
#Always ready <3
#The next topic is regular expressions! ever heard of them?
#I heard similar expression! Maybe other thing haha
#Then to be sure I'll explai <3 Stop me if something isn't clear, ok?<3
#OK <3
#Ok! Regular expressions are a way to easily see if strings contains some characters or if they are in the right formats
#it's like declaring rules for the string, and seeing if some part of the string match our rules
#for example, I want to say
#My string needs to contain at least one number
#there is a way to say that, and check if the strings match our rule correctly!
#With pratical examples it will be more clear, don't worry hahaha
#Let's start with numbers
#As you know, numbers are all between 0 and 9, right? right!
#Ok, in regular expression, a range like that is written like this 
#0-9
#0-9 means that every number will match with this rule
#so, if our string is 'abc5rhjahshsfoe'
#we will have one match, the 5!
#clear? Clear!
#ok! if I write '12345', every single number wil be a match for our expression 0-9
#since checking if something is number is pretty common, we also have a shorter way to write it
# it's written like this: \d  <----- d means 'digit'
#For now everything is very theoric and confusing, right?hahaha
# A little bit hahaha
#it's normal, they are easier to understand by practice! hahaha
# so, let's go back to the top