#** Test harness for binarySearchTree.py

import graphMenu
import BinarySearchTree
import sys
import io
def main():
  NUMTESTS = 3
  test = [False] * NUMTESTS
  p = None

  try:
    p = BinarySearchTree.DSABinarySearchTree()
    print('\033[92m'"BST successfully created!"'\033[0m')
    test[0] = True
  except:
    print("Failed")

  try:
    p.insert("Alex", 5)
    p.insert("Daniel", 8)
    p.insert("Geoff", 4)
    p.insert("Fred", 6)
    p.insert("George", 9)
    print('\033[92m'"Data successfully inserted!"'\033[0m')
    test[1] = True
  except:
    print("Failed")


  try:
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    p.max()
    val = new_stdout.getvalue()
    sys.stdout = old_stdout
    if val == "9 = George":
      print("Error")
    print('\033[92m'"Max successfully found!"'\033[0m')
    test[2] = True
  except:
    print("Failed")

  count = 0
  for i in range(NUMTESTS):
    if test[i] == True:
      print("Test", i, "passed!")
      count += 1
  print('\033[93m'"Result for binarySearchTree.py =", (count/NUMTESTS)*100, "%"'\033[0m')
        
