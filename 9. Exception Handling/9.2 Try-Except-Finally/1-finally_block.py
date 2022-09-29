'''
The finally block, if specified, will be executed regardless
if the try block raises an error or not.
'''

x = "Let's try this message"

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")