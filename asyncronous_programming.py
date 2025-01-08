# asyncio
# threading
# asychronous_programming
# to do things parallely using asyncio and threading
# run this in a background

import asyncio

# await and async

async def printSomething():
  print("Hello")
  await asyncio.sleep(1)  # sleep the exccution for 1 sec
  print("World")

async def fn():
    await asyncio.sleep(1)
    print('This is ')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')

asyncio.run(printSomething())
asyncio.run(fn())

async def myFn1():
  for i in range(1,5):
    await asyncio.sleep(1)
    print(i)

async def myFn2():
  for i in range(10,17):
    await asyncio.sleep(1)
    print(i)

async def myFn3():
  for i in range(20,31):
    await asyncio.sleep(1)
    print(i)

async def runMultipleFunction():
  await asyncio.gather(myFn1(), myFn2(), myFn3())  # run function parallely

asyncio.run(runMultipleFunction())

print("Finished")

#################################################################

import threading
import time

def printSomething():
  print("Hello")
  time.sleep(1)
  print("World")

def printSomething2():
  print("Hi")
  time.sleep(1)
  print("Student")

thread = threading.Thread(target=printSomething)  # sub process
thread1 = threading.Thread(target=printSomething2)  # sub process

thread.start()
thread.join()   # wait for the backgound task to complete
thread1.start()
thread1.join()
