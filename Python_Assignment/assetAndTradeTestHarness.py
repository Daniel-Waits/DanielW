#** Test harness for graphMenu.py

import graphMenu
import GraphLinkedList
def main():
  f = GraphLinkedList.DSAGraph()
  p = graphMenu.cryptoMenu()
  NUMTESTS = 6
  test = [False] * NUMTESTS
  p._readFile(f)

  try:
    f.assetOverview()
    f.visualiseGraph()
    print('\033[92m'"Asset successfully found and corresponding graph shown!"'\033[0m')
    test[0] = True
  except:
    print("Failed")

  try:
    f.getTradeDetails("ETHBTC")
    print('\033[92m'"Trade details successfully shown!"'\033[0m')
    test[1] = True
  except:
    print("Failed")

  try:
    print("Showing all paths from 'ETH' to 'BTC':")
    f.printAllPaths("ETH", "BTC")
    print('\033[92m'"Paths from 'ETH' to 'BTC' successfully shown!"'\033[0m')
    test[2] = True
  except ValueError as E:
    print(E)

  try:
    f.addAssetFilter("DOGE")
    print("Asset 'DOGE' ignored!")
    print("Testing by searching in graph for 'DOGE'!")
    f.getAssetDetails("DOGE")
    print('\033[92m'"Asset 'DOGE' successfully ignored!"'\033[0m')
    test[3] = True
  except:
    print("Failed")

  try:
    f.getAssetDetails("BTC")
    print('\033[92m'"Asset details for 'BTC' successfully displayed!"'\033[0m')
    test[4] = True
  except:
    print("Failed")

  try:
    f.getTopTenPrice()
    f.getTopTenVolume()
    f.getTopTenGain()
    print('\033[92m'"Broad trade overview successfully displayed!"'\033[0m')
    test[5] = True
  except:
    print("Failed")

  count = 0
  for i in range(NUMTESTS):
    if test[i] == True:
      print("Test", i, "passed!")
      count += 1
  print('\033[93m'"Result for assetAndTradeTestHarness.py =", (count/NUMTESTS)*100, "%"'\033[0m')