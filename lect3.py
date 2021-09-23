## lambda versus functions 

#def someCalc(a):
#   return a*(a-1)
#print( someCalc(3) )
#print( someCalc(5) )


#someCalc = lambda a: a*(a-1)
#print( someCalc(3) )
#print( someCalc(5) )



## Comments on input technical 
#import sys
#def getFibAt(i:int)->int: #return Fibonacci series value at i
#   a, b=0, 1
#   while i>0:
#      a, b = b, a+b
#      i-=1
#   return a
#sys.stdout.write("Enter a position in the Fibonacci sequence: ")
#i = int( sys.stdin.readline() )
#answer = getFibAt(i)
#sys.stdout.write( str(answer)+" is at "+str(i))

#print( getFibAt.__annotations__ )






## queues

# Python program to
# demonstrate queue implementation
# using list
from collections import deque
 
# Initializing a queue
queue = deque()
 
# Adding elements to the queue
queue.append('Joe Block')      ## 1st arrival
queue.append('Magician Wayne') ## 2nd arrival
queue.append('Elephant Ted')   ## 3rd arrival
 
print("Initial queue")
print(queue)

queue.popleft()                # See u later Mr Joe Block
print("Current queue")
print(queue)

queue.append("I am an urgent patient!")
print("Current queue")
print(queue)

queue.pop()
print("Current queue")
print(queue)








