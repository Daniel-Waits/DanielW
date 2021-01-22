#** Test harness for graphMenu.py

import graphMenu
import GraphLinkedList
def main():
  assetFile = r'F:\OneDrive - Curtin University of Technology Australia\Uni\Y2S2\COMP1002-Data Structures and Algorithms\Python\Assignment\assetFile.json'
  dayTrades = r'F:\OneDrive - Curtin University of Technology Australia\Uni\Y2S2\COMP1002-Data Structures and Algorithms\Python\Assignment\24hrTrades.json'
  assetInfo = r'F:\OneDrive - Curtin University of Technology Australia\Uni\Y2S2\COMP1002-Data Structures and Algorithms\Python\Assignment\assetInfo.json'
  f = GraphLinkedList.DSAGraph()
  p = graphMenu.cryptoMenu()
  NUMTESTS = 3
  test = [False] * NUMTESTS

  try:
    p.chooseMode(f)
    print('\033[92m'"Usage successfully shown!"'\033[0m')
    test[0] = True
  except:
    print("Failed")

  try:
    p.reportMode(f, assetFile, dayTrades, assetInfo)
    print('\033[92m'"Report mode successfully shown!"'\033[0m')
    test[1] = True
  except:
    print("Failed")

  try:
    print('\033[91m'"--Press '9' to continue with test!"'\033[0m')
    p.interactiveMode(f)
    print('\033[92m'"Interactive mode successfully shown!"'\033[0m')
    test[2] = True
  except:
    print("Failed")

  count = 0
  for i in range(NUMTESTS):
    if test[i] == True:
      print("Test", i, "passed!")
      count += 1
  print('\033[93m'"Result for graphMenuTestHarness.py =", (count/NUMTESTS)*100, "%"'\033[0m')