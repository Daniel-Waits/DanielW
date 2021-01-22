class DSAStack():
  DEFAULT_CAPACITY = 100
  def __init__(self):
    self.stack = [None] * DSAStack.DEFAULT_CAPACITY
    self.count = 0

  def getCount(self):
    return self.count

  def isEmpty(self):
    if self.count == 0:
      empty = True
    else:
      empty = False
    return empty

  def isFull(self):
    if self.count == (len(self.stack)):
      full = True
    else:
      full = False
    return full

  def push(self,value):
    try:  
        if self.isFull():
          raise ValueError("The stack is full!")
        else:
          self.stack[self.count] = value
          self.count = self.count + 1
    except (ValueError) as err:
        print(err)

  def pop(self):
    topVal = self.top()
    self.count = self.count - 1
    return topVal

  def top(self):
    try:  
        if self.isEmpty():
            raise ValueError("The stack is empty!")
        else:
            topVal = self.stack[self.count-1]
        return topVal
    except (ValueError) as err:
        print(err)
      
  def print(self):
    for i in range(self.count):
      if i == self.count-1:
        print(self.stack[i])
      else:
        print(self.stack[i], "->", end=' ')





  
