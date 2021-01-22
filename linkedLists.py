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
        newNd.setNext(self.tail)
        self.head = newNd
      else: #>1 item in list
        newNd.setNext(self.head)
        self.head = newNd
    except (ValueError) as err:
      print(err)

  def insertLast(self,newValue):
    newNd = DSALinkedList._DSAListNode(newValue)
    if self.isEmpty(): #empty list
      self.tail = newNd
      self.head = newNd
    elif self.tail.getValue() == self.head.getValue(): #1 item in list
        newNd.setPrevious(self.tail)
        self.tail = newNd
    else:
      newNd.setPrevious(self.tail)
      self.tail = newNd
    
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
