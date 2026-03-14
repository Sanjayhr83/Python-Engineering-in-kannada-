# #while loop(A loop is a programming structure that repeats a set of instructions as long as a specified condition is True. In Python, the while loop allows you to repeatedly execute a block of code as long as the condition is True.)
i=0 #initialization
while i<100: #condition
    print(f"Hello {i}")
    i+=1 #increment (or decrement)
print("Loop ended")

i=0
while i<10:
    print(i,end=" ")    #end=" " prints the output in the same line with a space separator
    i+=1

#while using break
i = 1
while i <= 10:
    if i == 5:
        break   #break stops the loop immediately.
    print(i)
    i += 1

#while using continue
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue   #continue skips the current iteration and moves to the next iteration.
    print(i)
    i += 1

#Using while Loops for User Input
correct_pin="1234"
trials=0
while trials <3:
    trials+=1
    pin=input(f"your {trials} attempt - enter your pin: ")
    if pin!=correct_pin:
        print("Incorrect PIN. Try again.")
    else:
        print("PIN accepted. You can proceed.")
        break

print("Odd numbers from 1 to 20:")
i=0
while i<=20:
    if i%2!=0:
        print(i)
    i+=1

#Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over.
print("Countdown Timer:")
import time
i=0
while i<10:
    time.sleep(1)
    print(10-i)
    i+=1
print("Happy new year!")