height = 3

#I want to print this
#*
#**
#***

#So, I can do it the stupid way

#i = 1
#i = 1

#for j in range(i):
#    print('*', end='')
#print()

#i = i + 1
# i = 1 + 1 ---> = 2
#for j in range(i):
#    print('*', end='')
#print()

#i = i + 1
#i = 2 + 2 ----> = 4
#for k in range(i):
#    print('*', end='')

#--------------------------------------------

#for i in range(3):
#    for j in range(i + 1):
#        print('*', end='')
#    print()

#How can we fix it?
#We wanted
#*
#**
#***

#But in our first i step, the j loop is skipped because i = 0 :(
#is that right?

#It works!!! <3 #I want to save this comments for later hahaha #saved!
#Good <3
#You can of course save everything when we are done!
#Let's move down the file so you can keep the old comments too!

#for i in range(3):
#    for j in range(i):
#        print('*', end='')
#    print()
#This is the code
#Let's try to follow the loop step by step

#for i in range(3) ----> i will be 0,1,2
#first step, i = 0

#for j in range(0) <---- i = 0, so 0
#so j will be.... nothing hahahaha
#the for is skipped
#print() <---- we only print an empty line

#second step, i = 1!

#for j in range(1) <---- i = 1, so 1
#so j will be 0
#only 1 step will be made
#print('*', end='') ----> we print *
#print() <---- we print an empty line

#So now we have
#
#*

#third step, i = 2!

#for j in range(2) <---- i = 2, so 2
#so j will be 0,1
#2 steps will be made

##First step, j = 0
##print('*', end='') ----> we print *

##Second step, j = 1
##print('*', end='') ----> we print *

##we printed ** (in this two j steps)

#print() <---- we print an empty line

#So now we have
#
#*
#**

#So, let's go back to the code!

#Final code:

#for i in range(3):
#    for j in range(i + 1):
#        print('*', end='')
#    print()

#---------------------------------------------------------------------

#Now, I'm a very annoying guy
#I decided that I want it in the opposite way!
#Like this
#***
#**
#*

#Nothing, I wrote it badly hahahaha
#Like that hahaha #I'll try hahaha

#for i in range(3):
#    for j in reversed(i+1):
#        print('*', end='')
#    print()

#You're thinking about the right thing, but you're working on the wrong place ;)
#We have the old code
#Remember the steps we saw before?
#Let's take the first step again, i = 0

#first step, i = 0

#for j in range(0 + 1) <---- i = 0, so 1
#so j will be 0
#we will make only 1 step inside the for
##print('*', end='') <------ we print *
#print() <---- we only print an empty line

#Now, we want to print *** in the first line, instead of *
#To do this, we need j to be 0,1,2
#so we have 2 ways to do it
# -> i + 1 = 3
# -> we put something else instead of i + 1

#Both ways are perfectly ok
#Any ideas? #We can't input 3 right?
#If we input 3, the next step in the loop won't work
#Would it be useful if i was 2,1,0 instead of 0,1,2? #Right!
#Can you make it do that? #using reversed thing? #yep! ;)
#We wanted to change i, not j, right? #right!
#Ok, try working on i then!
#Where do you give i a value?
#Are you there? #I'm thinking but I don't know hahaha
#It's ok, we can do it <3
#Let me ty explaining you in another way
#Do you know of while loops? #Yes!

#Let's try to write this as a while loop (instead of for)
#I'll start writing it to give you an hint

#i = 3
#while (i >= 1):
#    for j in range(i):
#        print('*', end='')
#    print()
#    i = i - 1

#Good, can you make it work like we want now?
#like this
#***
#**
#*

#It's almost perfect now
#i starts from 3, then we remove 1 each time
#until when it has to continue?
# i = 3, i = 2, i = 1, i = 0, i = -1....
#When does it have to stop?
#It works! But it lacks one row!
#Would > 0 work too? #Yes!
#Perfect! Amazing <3!
#Do you think it can work if I write it like this:


for i in reversed(range(3)):
    for j in range(i+1):
        print('*', end='')
    print()


#Ok, no problem!What is confusing for you now?
#deciding i and j hahaha I need more time to think maybe
#It's ok, when you are confused, divide the loops in steps as we did before
#Do you want to stop at this for now to give you the time to review it with calm?
#I think it's better :) And I think you should go out soon! <3
#Best gf ever <3
#Then copy everything! ;) #Ok, Thank you nice teacher ever <3
#Copied? #finished! <3
#Ok, I'll clean some comments and let's go back to kakao, ok?
#ok :)