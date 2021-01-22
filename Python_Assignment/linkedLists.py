#doubly linked double ended
#has a head and a tail
#has a previous and a next
class DSALinkedList():
  def __init__(self):
    self.head = None
    self.tail = None

  def isEmpty(self):
    if self.head == None:
      empty = True
    else:
      empty = False
    return empty

  def peekFirst(self):
    try:  
        if self.isEmpty():
            raise ValueError("The list is empty!")
        else:
            nodeValue = self.head.getValue()
            return nodeValue
    except (ValueError) as err:
        print(err)
      
  def removeFirst(self):
    try:  
      nodeValue = None
      if self.isEmpty(): #empty list
          raise ValueError("The list is empty!")
      elif self.tail.getValue() == self.head.getValue(): #1 item in list
        nodeValue = self.head.getValue()
        self.tail = None
        self.head = None
      elif self.head.getNext() == None: #2 items in list
        nodeValue = self.head.getValue()
        self.head = self.tail
      else: #>1 items in list
          nodeValue = self.head.getValue()
          self.head = self.head.getNext()
      return nodeValue
    except (ValueError) as err:
        print(err)

  def removeVertex(self, item):
    if self.head == None:
      print("List not initialized")
    if self.head.value.label == item:
      self.head = self.head.getNext()
      self.head.setPrevious(None)
    cur = self.head
    while cur.next != None:
      if cur.value.symbol == item:
        node = cur
        nodeToRemove = node
        previousNode = nodeToRemove.previous
        nextNode = nodeToRemove.next
        previousNode.setNext(nextNode)
        nextNode.setPrevious(previousNode)
      cur = cur.next
    if self.tail.value.label == item: #if edge is tail
      self.tail = self.tail.getPrevious()
      self.tail.setNext(None)
      return 0
  
  def removeEdge(self, item):
    count = 0
    if self.head == None:
      print("List not initialized")
    if self.head.value.to == item: #if edge is head
      self.head = self.head.getNext()
      self.head.setPrevious(None)
      return 0
    cur = self.head
    cur1 = self.head
    cur2 = self.head
    while cur.next != None: #if edge elsewhere
      cur2 = cur2.next
      if cur.value.to == item:
        cur1.setNext(cur2)
        cur2.setPrevious(cur1)
        return 0
      count += 1
      cur = cur.next
      if count > 1:
        cur1 = cur1.next
    if self.tail.value.to == item: #if edge is tail
      self.tail = self.tail.getPrevious()
      self.tail.setNext(None)
      return 0

  def getNthNode(self, nodeVal):
    temp = self.head
    count = 0
    while temp :
      if count == nodeVal:
        return temp.value
      count += 1
      temp = temp.next
    
  def getNode(self, nodeVal):
    temp = self.head
    count = 0
    while temp :
      if count == nodeVal:
        return temp
      count += 1
      temp = temp.next

  def removeLast(self):
    try:
      nodeValue = None
      if self.isEmpty(): #empty list
          raise ValueError("The list is empty!")
      elif self.tail.getValue() == self.head.getValue(): #1 item in list
        nodeValue = self.head.getValue()
        self.tail = None
        self.head = None
      elif self.head.getNext() == None: #2 items in list
        nodeValue = self.tail.getValue()
        self.tail = self.head
      else: #>1 items in list
          nodeValue = self.tail.getValue()
          self.tail = self.tail.getPrevious()
      return nodeValue
    
    except (ValueError) as err:
      print(err)

  def peekLast(self):
    try:  
        if self.isEmpty():
            raise ValueError("The list is empty!")
        else:
          nodeValue = self.tail.getValue()
          return nodeValue
    except (ValueError) as err:
        print(err)

  def insertFirst(self,newValue):
    try:
      newNd = DSALinkedList._DSAListNode(newValue)
      if self.isEmpty(): #empty list
        self.head = newNd
        self.tail = newNd
      elif self.tail.getValue() == self.head.getValue(): #1 item in list
        oldNode = self.tail
        newNd.setNext(oldNode)
        oldNode.setPrevious(newNd)
        self.tail = oldNode
        self.head = newNd
      else: #>1 item in list
        newNd.setNext(self.head)
        self.head = newNd
    except (ValueError) as err:
      print(err)

    
  def printListInOrder(self):
    newArr = DSALinkedList()
    for i in range(self.getLength()):
      newArr.insertFirst(self.getNthNode(i))
      print(newArr.getNthNode(i).to)
    return newArr
  
  def printEdges(self):
    node = self.head
    #print("Trades for asset: "),
    #print(self.head.value.origin)
    while node is not None:
      print(node.value.to, end=' ')
      node = node.next
    print("")

  def printEdgesValue(self):
    node = self.head
    #print("Trades for asset: "),
    #print(self.head.value.origin)
    while node is not None:
      print(node.value.value),
      node = node.next
    print("")

  def insertSorted(self, newValue):
    try:
      newNd = DSALinkedList._DSAListNode(newValue)
      if self.isEmpty(): #empty list
        self.head = newNd
        self.tail = newNd
      elif self.tail.getValue() == self.head.getValue(): #1 item in list
        oldNode = self.tail
        if ((newNd.value.symbol)) < ((oldNode.value.symbol)):
          newNd.setNext(oldNode)
          oldNode.setPrevious(newNd)
          self.tail = oldNode
          self.head = newNd
        else: #belongs at end
          newNd.setPrevious(oldNode)
          oldNode.setNext(newNd)
          self.tail = newNd
          self.head = oldNode
      else: #>1 item in list
        temp = self.head
        temp1 = self.head #x-1 pointer
        count = 0
        while temp:
          if ((newValue.symbol)) < ((temp.value.symbol)):
            if count == 0: #goes at beginning of list
              temp.setPrevious(newNd)
              newNd.setNext(temp)
              self.head = newNd
              return 0
            else:
              temp.setPrevious(newNd)
              temp1.setNext(newNd)
              newNd.setNext(temp)
              newNd.setPrevious(temp1)
              return 0
          
          elif (temp.getNext() == None):
            temp2 = self.tail
            self.tail.setNext(newNd)
            newNd.setPrevious(temp2)
            self.tail = newNd
            return 0
          temp = temp.next
          count += 1
          if count > 1:
            temp1 = temp1.next
    except (ValueError) as err:
      print(err)

  def insertSortedEdge(self, newValue):
    try:
      newNd = DSALinkedList._DSAListNode(newValue)
      if self.isEmpty(): #empty list
        self.head = newNd
        self.tail = newNd
      elif self.tail.getValue() == self.head.getValue(): #1 item in list
        oldNode = self.tail
        first = min(newNd.value.to, oldNode.value.to)
        #print("min of:", newNd.value.to, oldNode.value.to, " = ", first)
        if first == newNd.value.to:
          newNd.setNext(oldNode)
          oldNode.setPrevious(newNd)
          self.tail = oldNode
          self.head = newNd
        else: #belongs at end
          newNd.setPrevious(oldNode)
          oldNode.setNext(newNd)
          self.tail = newNd
          self.head = oldNode
      else: #>1 item in list
        temp = self.head
        temp1 = self.head #x-1 pointer
        count = 0
        while temp:
          first = min(newNd.value.to, temp.value.to)
          #print("min of:", newNd.value.to, temp.value.to, " = ", first)
          if first == newNd.value.to:
            if count == 0: #goes at beginning of list
              temp.setPrevious(newNd)
              newNd.setNext(temp)
              self.head = newNd
              return 0
            else:
              temp.setPrevious(newNd)
              temp1.setNext(newNd)
              newNd.setNext(temp)
              newNd.setPrevious(temp1)
              return 0
          
          elif (temp.getNext() == None):
            temp2 = self.tail
            self.tail.setNext(newNd)
            newNd.setPrevious(temp2)
            self.tail = newNd
            return 0
          temp = temp.next
          count += 1
          if count > 1:
            temp1 = temp1.next
    except (ValueError) as err:
      print(err)

  def insertLast(self,newValue):
    newNd = DSALinkedList._DSAListNode(newValue)
    if self.isEmpty(): #empty list
      self.tail = newNd
      self.head = newNd
    elif self.tail.getValue() == self.head.getValue(): #1 item in list
        oldNode = self.head
        newNd.setPrevious(oldNode)
        oldNode.setNext(newNd)
        self.head = oldNode
        self.tail = newNd
    else:
      temp = self.tail
      self.tail.setNext(newNd)
      newNd.setPrevious(temp)
      self.tail = newNd
    
  def getLength(self):
    temp = self.head
    count = 0
    while temp :
      count += 1
      temp = temp.next
    return count

  def findInList(self, item):
    if self.head == None:
      print("List not initialized")
    if self.head.value == item:
      return True
    if self.tail.value == item:
      return True
    cur = self.head
    while cur.next != None:
      if cur.value == item:
        return True
      cur = cur.next
    return False
  
  def findNode(self, item):
    if self.head == None:
      print("List not initialized")
    if self.head.value == item:
      return self.head
    if self.tail.value == item:
      return self.tail
    cur = self.head
    while cur.next != None:
      if cur.value == item:
        return cur
      cur = cur.next
    return False


  class LinkedList():
    def __init__(self):
      self._root = None

    def insertFirst(self, value):
      if self._root == None:
        self._root = DSALinkedList.ListNode(value)
      else:
        newNode = DSALinkedList.ListNode(value)
        newNode._next = self._root
        self._root = newNode  
      
    def __iter__(self):
      self._cur = self._root
      return self

    def __next__(self):
      curval = None
      if self._cur == None:
        raise StopIteration
      else:
        curval = self._cur._data
        self._cur = self._cur._next
      return curval

  class ListNode():
    def __init__(self,data):
      self._next = None
      self._data = data

  class _DSAListNode():
    def __init__(self,inValue):
      self.value = inValue
      self.next = None
      self.previous = None

    def getValue(self):
      return self.value

    def setValue(self,inValue):
      self.value = inValue

    def getNext(self):
      return self.next

    def setNext(self,newNext):
      self.next = newNext

    def setPrevious(self, newPrevious):
      self.previous = newPrevious

    def getPrevious(self):
      return self.previous
