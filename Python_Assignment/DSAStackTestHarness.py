#** Test harness for DSAStack.py

import graphMenu
import DSAStack
def main():
  NUMTESTS = 3
  test = [False] * NUMTESTS
  p = None

  try:
    p = DSAStack.DSAStack()
    print('\033[92m'"Stack successfully created!"'\033[0m')
    test[0] = True
  except:
    print("Failed")

  try:
    p.push(5)
    p.push(8)
    p.push(28)
    p.push(51)
    p.push(32)
    print('\033[92m'"Data successfully inserted!"'\033[0m')
    test[1] = True
  except:
    print("Failed")


  try:
    val = p.pop()
    if val == "32":
      print("Error")
    val1 = p.pop()
    if val == "51":
      print("Error")
    print('\033[92m'"Top successfully found and removed!"'\033[0m')
    test[2] = True
  except:
    print("Failed")

  count = 0
  for i in range(NUMTESTS):
    if test[i] == True:
      print("Test", i, "passed!")
      count += 1
  print('\033[93m'"Result for DSAStack.py =", (count/NUMTESTS)*100, "%"'\033[0m')
        
