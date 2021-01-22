#** Test harness for graphMenu.py

import graphMenu
import GraphLinkedList
def main():
  saveFile = r'F:\OneDrive - Curtin University of Technology Australia\Uni\Y2S2\COMP1002-Data Structures and Algorithms\Python\Assignment\saveFile.pkl'
  f = GraphLinkedList.DSAGraph()
  p = graphMenu.cryptoMenu()
  NUMTESTS = 4
  test = [False] * NUMTESTS

  try:
    p._printFileNames()
    print('\033[92m'"FileNames successfully shown!"'\033[0m')
    test[0] = True
  except:
    print("Failed")

  try:
    p._readFile(f)
    print('\033[92m'"Files read successfully and corresponding graph created!"'\033[0m')
    test[1] = True
  except:
    print("Failed")

  try:
    p.save(saveFile, f)
    print('\033[92m'"Object successfully saved!"'\033[0m')
    test[2] = True
  except:
    print("Failed")

  try:
    print(p.load(saveFile))
    print('\033[92m'"Object successfully loaded!"'\033[0m')
    test[3] = True
  except:
    print("Failed")

  count = 0
  for i in range(NUMTESTS):
    if test[i] == True:
      print("Test", i, "passed!")
      count += 1
  print('\033[93m'"Result for fileIOTestHarness.py =", (count/NUMTESTS)*100, "%"'\033[0m')