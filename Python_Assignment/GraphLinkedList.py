import linkedLists
import DSAStack
import graphVisualiser
import BinarySearchTree

class DSAGraph():
  def __init__(self):
    self.vertices = linkedLists.DSALinkedList()
    self.edges = linkedLists.DSALinkedList()
  
  def addVertex(self, label, symbol, marketCap, price, curculatingSupply, volume, oneHour, oneDay, sevenDay):
    flag = False
    for i in range(self.vertices.getLength()):
      if label == self.vertices.getNthNode(i).label:
        flag = True
    if flag is False:
      self.vertices.insertSorted(DSAGraph.DSAGraphVertex(label, symbol, marketCap, price, curculatingSupply, volume, oneHour, oneDay, sevenDay))
    else:
      return 0

  def addEdge(self, label1, label2, symbol, priceChange, priceChangePercent, weightedAvgPrice, prevClosePrice, lastPrice, highPrice, lowPrice):
    self.edges.insertSortedEdge(DSAGraph.DSAGraphEdge(label1, label2, symbol, priceChange, priceChangePercent, weightedAvgPrice, prevClosePrice, lastPrice, highPrice, lowPrice))

  def hasVertex(self, label):
    flag = False
    for i in range(self.vertices.getLength()):
      if self.vertices.getNthNode(i).label == label:
        flag = True
    return flag

  def getVertexCount(self):
    return (self.vertices.getLength())

  def getEdgeCount(self):
    count = 0
    for i in range(self.vertices.getLength()):
      self.edges.getNthNode(i)
      count += 1
    return count
  
  def getVertex(self, label):
    vertex = None
    for i in range(self.vertices.getLength()):
      if self.vertices.getNthNode(i).label == label:
        vertex = self.vertices.getNthNode(i)
    return vertex

  def getEdge(self, label):
    edgeList = linkedLists.DSALinkedList()
    for i in range(self.edges.getLength()):
      if self.edges.getNthNode(i).origin == label:
        edgeList.insertFirst(DSAGraph.DSAGraphEdge(self.edges.getNthNode(i).origin, self.edges.getNthNode(i).to, self.edges.getNthNode(i).symbol, self.edges.getNthNode(i).priceChange, self.edges.getNthNode(i).priceChangePercent, self.edges.getNthNode(i).weightedAvgPrice, self.edges.getNthNode(i).prevClosePrice, self.edges.getNthNode(i).lastPrice, self.edges.getNthNode(i).highPrice, self.edges.getNthNode(i).lowPrice))
    return edgeList

  def getEdgeReverse(self, label):
    edgeList = linkedLists.DSALinkedList()
    for i in range(self.edges.getLength()):
      if self.edges.getNthNode(i).origin == label:
        edgeList.insertLast(DSAGraph.DSAGraphEdge(self.edges.getNthNode(i).origin, self.edges.getNthNode(i).to, self.edges.getNthNode(i).symbol, self.edges.getNthNode(i).priceChange, self.edges.getNthNode(i).priceChangePercent, self.edges.getNthNode(i).weightedAvgPrice, self.edges.getNthNode(i).prevClosePrice, self.edges.getNthNode(i).lastPrice, self.edges.getNthNode(i).highPrice, self.edges.getNthNode(i).lowPrice))
    return edgeList

  def getAdjacencyList(self):
    for vert in range((self.vertices.getLength())):
      print(self.vertices.getNthNode(vert).symbol, "->", end=' ')
      (self.getEdgeReverse(self.vertices.getNthNode(vert).symbol)).printEdges(),

  def getTradeDetails(self, label):
    if not self.checkEdge(label):
      print('\033[91m'"Trade", label, "does note exist!"'\033[0m')
    else:
      for i in range(self.edges.getLength()):
        if self.edges.getNthNode(i).symbol == label:
          print(label, "Trade Details")
          print("priceChange ($) for", self.edges.getNthNode(i).symbol, "=", self.edges.getNthNode(i).priceChange)
          print("priceChangePercent (%) for", self.edges.getNthNode(i).symbol, "=", self.edges.getNthNode(i).priceChangePercent)
          print("weightedAvgPrice ($) for", self.edges.getNthNode(i).symbol, "=", self.edges.getNthNode(i).weightedAvgPrice)
          print("prevClosePrice ($) for", self.edges.getNthNode(i).symbol, "=", self.edges.getNthNode(i).prevClosePrice)
          print("lastPrice ($) for", self.edges.getNthNode(i).symbol, "=", self.edges.getNthNode(i).lastPrice)
          print("highPrice ($) for", self.edges.getNthNode(i).symbol, "=", self.edges.getNthNode(i).highPrice)
          print("lowPrice ($) for", self.edges.getNthNode(i).symbol, "=", self.edges.getNthNode(i).lowPrice)

  def getAssetDetails(self, label):
    if not self.checkVertex(label):
        print('\033[91m'"Asset", label, "does not exist!"'\033[0m')
    else:
      for i in range(self.vertices.getLength()):
        if self.vertices.getNthNode(i).symbol == label:
          print("Asset Details for: ", label)
          print("Name: ", self.vertices.getNthNode(i).label)
          print("Market Cap for", self.vertices.getNthNode(i).symbol, "=", self.vertices.getNthNode(i).marketCap)
          print("Price ($) for", self.vertices.getNthNode(i).symbol, "=", self.vertices.getNthNode(i).price)
          print("Circulating Supply ($) for", self.vertices.getNthNode(i).symbol, "=", self.vertices.getNthNode(i).circulatingSupply)
          print("Volume (24hr) for", self.vertices.getNthNode(i).symbol, "=", self.vertices.getNthNode(i).volume)
          print("Percent change (1 hour)(%) for", self.vertices.getNthNode(i).symbol, "=", self.vertices.getNthNode(i).oneHour)
          print("Percent change (24 hour)(%) for", self.vertices.getNthNode(i).symbol, "=", self.vertices.getNthNode(i).oneDay)
          print("Percent change (7 day)(%) for", self.vertices.getNthNode(i).symbol, "=", self.vertices.getNthNode(i).sevenDay)

  def printStats(self):
    length = self.vertices.getLength()
    total1hr = 0.0
    total24hr = 0.0
    total7day = 0.0
    totalSupply = 0.0
    for i in range(self.vertices.getLength()):
      total1hr += self.vertices.getNthNode(i).oneHour
    for i in range(self.vertices.getLength()):
      total24hr += self.vertices.getNthNode(i).oneDay
    for i in range(self.vertices.getLength()):
      total7day += self.vertices.getNthNode(i).sevenDay
    for i in range(self.vertices.getLength()):
      totalSupply += self.vertices.getNthNode(i).circulatingSupply
    average1hr = total1hr/length
    average24hr = total24hr/length
    average7day = total7day/length
    print("Total assets =", length)
    print("1 Hour trend(%) =", average1hr)
    print("24 Hour trend(%) =", average24hr)
    print("7 Day trend(%) =", average7day)
    print("Total supply =", totalSupply)
    
  def addAssetFilter(self, assetName):
    if not self.checkVertex(assetName):
        print('\033[91m'"Asset", assetName, "does not exist!"'\033[0m')
    else:
      count = 1
      self.vertices.removeVertex(assetName)
      for i in range(self.edges.getLength()):
        self.edges.removeEdge(assetName)
        count = i
      return count

  def checkVertex(self, vertex):
    flag = False
    for i in range(self.vertices.getLength()):
      if self.vertices.getNthNode(i).symbol == vertex:
        flag = True
    return flag

  def checkEdge(self, label):
    flag = False
    for i in range(self.edges.getLength()):
        if self.edges.getNthNode(i).symbol == label:      
          flag = True
    return flag

  def visualiseGraph(self):
    c = graphVisualiser.GraphVisualisation()
    for i in range(self.edges.getLength()):
      c.addEdge(self.edges.getNthNode(i).origin, self.edges.getNthNode(i).to)
    print("Graph opened in new tab!")
    c.visualise()
  
  def visualiseAsset(self, asset):
    if not self.checkVertex(asset):
      print('\033[91m'"Asset", asset, "does not exist!"'\033[0m')
    else:
      c = graphVisualiser.GraphVisualisation()
      for i in range(self.edges.getLength()):
        if self.edges.getNthNode(i).origin == asset:
          c.addEdge(self.edges.getNthNode(i).origin, self.edges.getNthNode(i).to)
      print("Graph opened in new tab!")
      c.visualise()
    
  def assetOverview(self):
    count = self.getEdgeCount()
    print("Total number of asset pairs:", count)
  
  def getTopTenPrice(self):
    print("--------------------------------------------------")
    print("-----------Top ten assets for price($):-----------")
    a = BinarySearchTree.DSABinarySearchTree()
    for i in range(self.vertices.getLength()):
      a.insert(self.vertices.getNthNode(i).price, self.vertices.getNthNode(i).label)
    for i in range(10):
      a.max()
    print("-----------Top ten assets for price($):-----------")

  def getTopTenVolume(self):
    print("--------------------------------------------------")
    print("----Top ten assets for volume in last 24hr($):----")
    b = BinarySearchTree.DSABinarySearchTree()
    for i in range(self.vertices.getLength()):
      b.insert(self.vertices.getNthNode(i).volume, self.vertices.getNthNode(i).label)
    for i in range(10):
      b.max()
    print("----Top ten assets for volume in last 24hr($):----")
    print("--------------------------------------------------")

  def getTopTenGain(self):
    print("------Top ten gainers in the last 7 days(%):------")
    c = BinarySearchTree.DSABinarySearchTree()
    for i in range(self.vertices.getLength()):
      c.insert(self.vertices.getNthNode(i).sevenDay, self.vertices.getNthNode(i).label)
    for i in range(10):
      c.max()
    print("------Top ten gainers in the last 7 days(%):------")
    print("--------------------------------------------------")

  def printAllPathsUtil(self, origin, dest, path):
    for i in range(self.vertices.getLength()):
      if self.vertices.getNthNode(i).symbol == origin:
        self.vertices.getNthNode(i).visited = True
    path.push(origin)
    if origin == dest:
      path.print()
    else:
      for vert in range((self.vertices.getLength())):
        if self.vertices.getNthNode(vert).symbol == origin:
          val1 = vert
      adjList = (self.getEdgeReverse(self.vertices.getNthNode(val1).symbol))
      for j in range(adjList.getLength()):
        val = adjList.getNthNode(j).to
        for i in range(self.vertices.getLength()):
          if self.vertices.getNthNode(i).symbol == val:
            if self.vertices.getNthNode(i).visited == False:
              self.printAllPathsUtil(val, dest, path)
    path.pop()
    for i in range(self.vertices.getLength()):
      if self.vertices.getNthNode(i).symbol == origin:
        self.vertices.getNthNode(i).visited = False
  
  def printAllPaths(self, origin, dest):
    if not self.checkVertex(origin):
        print('\033[91m'"Asset", origin, "does not exist!"'\033[0m')
    elif not self.checkVertex(dest):
        print('\033[91m'"Asset", dest, "does not exist!"'\033[0m')
    else:
      for i in range(self.vertices.getLength()):
        self.vertices.getNthNode(i).visited = False
      path = DSAStack.DSAStack()
      self.printAllPathsUtil(origin, dest, path)
    

  def getAdjacent(self, vertex):
    for vert in range((self.vertices.getLength())):
      if self.vertices.getNthNode(vert).symbol == vertex:
        (self.getEdgeReverse(self.vertices.getNthNode(vert).symbol)).printEdges(),
    


  class DSAGraphEdge():
    def __init__(self, baseAsset, quoteAsset, inSymbol, inPriceChange, inPriceChangePercent, inWeightedAvgPrice, inPrevClosePrice, inLastPrice, inHighPrice, inLowPrice):
      self.origin = baseAsset
      self.to = quoteAsset
      self.symbol = inSymbol
      self.priceChange = inPriceChange
      self.priceChangePercent = inPriceChangePercent
      self.weightedAvgPrice = inWeightedAvgPrice
      self.prevClosePrice =  inPrevClosePrice
      self.lastPrice = inLastPrice
      self.highPrice = inHighPrice
      self.lowPrice =  inLowPrice

    def getOrigin(self):
      return self.origin
    
    def getTo(self):
      return self.to

    def getSymbol(self):
      return self.symbol
    
    def setOrigin(self, inOrigin):
      self.origin = inOrigin

    def setTo(self, inTo):
      self.to = inTo
    
    def setSymbol(self, inSymbol):
      self.symbol = inSymbol

  class DSAGraphVertex():
      def __init__(self, inLabel, inSymbol, inMarketCap, inPrice, inCurculatingSupply, inVolume, inOneHour, inOneDay, inSevenDay):
        self.label = inLabel
        self.symbol = inSymbol
        self.marketCap = inMarketCap
        self.price = inPrice
        self.circulatingSupply = inCurculatingSupply
        self.volume = inVolume
        self.oneHour = inOneHour
        self.oneDay = inOneDay
        self.sevenDay = inSevenDay
        self.visited = None
      
      def getLabel(self):
        return self.label
      
      def getSymbol(self):
        return self.symbol
      
      def setLabel(self, inLabel):
        self.label = inLabel
      
      def setSymbol(self, inSymbol):
        self.symbol = inSymbol