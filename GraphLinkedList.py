import linkedLists
import DSAStack
import BinarySearchTree

class DSAGraph():
  def __init__(self):
    self.vertices = linkedLists.DSALinkedList()
    self.edges = linkedLists.DSALinkedList()
    #myiter = iter(self.vertices)
    #value = next(myiter)
  
  def addVertex(self, label, value):
    flag = False
    for i in range(self.vertices.getLength()):
      if label == self.vertices.getNthNode(i).label:
        flag = True
    if flag is False:
      self.vertices.insertSorted(DSAGraph.DSAGraphVertex(label, value))
    else:
      flag = False

  def addEdge(self, label1, label2, value):
    self.edges.insertSortedEdge(DSAGraph.DSAGraphEdge(label1, label2, value))
    
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
        edgeList.insertFirst(self.edges.getNthNode(i).to) 
    return edgeList.printListInOrder()

  def getEdgeReverse(self, label):
    edgeList = linkedLists.DSALinkedList()
    for i in range(self.edges.getLength()):
      if self.edges.getNthNode(i).origin == label:
        edgeList.insertLast(self.edges.getNthNode(i).to) 
    return edgeList
  
  def getAdjacencyList(self):
    for vert in range((self.vertices.getLength())):
      print(self.vertices.getNthNode(vert).label, "->", self.getEdge(self.vertices.getNthNode(vert).label))
    print("")

  def depthFirstSearch(self, startVertex):
    for i in range(self.vertices.getLength()):
      self.vertices.getNthNode(i).visited = False
    for i in range(self.vertices.getLength()):
      if self.vertices.getNthNode(i).label == startVertex:
        self.vertices.getNthNode(i).visited = True
        flag = i
    S = DSAStack.DSAStack()
    S.push(self.vertices.getNthNode(i).label)
    T = linkedLists.DSALinkedList()
    while S.isEmpty() == False:
      print(self.vertices.getNthNode(flag).label)
      vertList = self.getEdge(self.vertices.getNthNode(flag).label)
      print(vertList.printListInOrder())
      print(vertList.getLength())
      for i in range(vertList.getLength()):
        print("hiiiiii")
        print(vertList.getNthNode(i))
        #while vertList.getNthNode(i) is not None:
          #print(vertList.getNthNode(i))
          #w = vertList.getNthNode(i)
          #T.insertFirst(w)
          #self.edges.getNthNode(i).visited = True
          #S.push(w)





  #def _dFS(self, startVertex, linkedList):
    #for i in range(linkedList.getLength()):
      #if linkedList.getNthNode(i).label == startVertex:
        #linkedList.getNthNode(i).visited = True
        #print(startVertex, end=' ')
    #edgeList = self.getEdgeReverse(startVertex)
    #for j in range(edgeList.getLength()):
      #if linkedList.getNthNode(j).visited == False:
        #self._dFS(linkedList.getNthNode(j).label, linkedList)
    
  #def depthFirstSearch(self, startVertex):
    #for i in range(self.vertices.getLength()):
      #self.vertices.getNthNode(i).visited = False
    #self._dFS(startVertex, self.vertices)

  def getAdjacent(self, label):
    vertexList = []
    for vert in self.vertices:
      if vert.label == label:
        vertexList.append(self.getEdge(vert.label))
    return vertexList

  def sort(self):
    self.vertices.sort(key=lambda x: x.label, reverse=False)

  class DSAGraphEdge():
    def __init__(self, originVertex, toVertex, inValue):
      self.origin = originVertex
      self.to = toVertex
      self.value = inValue
    
    def getValue(self):
      return self.value
    
    def getOrigin(self):
      return self.origin
    
    def getTo(self):
      return self.to

  class DSAGraphVertex():
      def __init__(self, inLabel, inValue):
        self.label = inLabel
        self.value = inValue
        self.visited = None
      
      def getLabel(self):
        return self.label
      
      def getValue(self):
        return self.value
        #exports value
      
      def getAdjacent(self):
        return self.value
        #exports vertexList
      
      def getAdjacentE(self):
        return self.value
        #exports edgeList
      
      def addEdge(self, vertex):
        return self.value

      def setVisited(self):
        self.visited = True
      
      def clearVisited(self):
        return self.value

      def getVisited(self):
        return self.value
        #exports boolean
      
      def toString(self):
        string = None
        string = ("Label = ", self.label, "| Value = ", self.value)
        return string

