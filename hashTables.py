import math
#state 0 = never used, 1 = used, -1 = formerly used
class DSAHashTable():
  def __init__(self, tableSize):
    actualSize = self._findNextPrime(tableSize)
    self.hashArray = [None] * actualSize
    for i in range(actualSize):
      self.hashArray[i] = DSAHashTable.DSAHashEntry(None, None)

  def put(self, inKey, inValue):
    hashVal = self._hash(inKey)
    orig = hashVal
    while self.hashArray[hashVal].state == 1:
      hashVal += 1
      if hashVal >= (len(self.hashArray)):
        hashVal = hashVal - (len(self.hashArray))
    self.hashArray[hashVal] = DSAHashTable.DSAHashEntry(inKey, inValue) 
    print("hash value for ", inKey, " = ", hashVal, "-Original = ", orig, "-Value = ", inValue)

  def get(self, inKey):
    hashIdx = self._hash(inKey)
    origIdx = hashIdx
    found = False
    giveUp = False

    while (not found) and (not giveUp):
      if (self.hashArray[hashIdx].state == 0):
        giveUp = True
      elif (self.hashArray[hashIdx].key == inKey):
        found = True
      else:
        hashIdx = (hashIdx + 1) % (len(self.hashArray))
        if (hashIdx == origIdx):
          giveUp = True
    if (not found):
      print("Key not found!")
    retValue = self.hashArray[hashIdx].value
    return retValue

  def remove(self, inKey):
    hashVal = self._hash(inKey)
    while self.hashArray[hashVal].state == 1 or self.hashArray[hashVal].state == -1:
      if hashVal == (len(self.hashArray)):
        hashVal = 0
      if self.hashArray[hashVal].key == inKey:
        self.hashArray[hashVal] = DSAHashTable.DSAHashEntry(None, None)
        self.hashArray[hashVal].state = -1
        print("Removing: ", inKey, "-", hashVal)
      hashVal += 1

  def getLoadFactor(self):
    numItems = 0
    for i in range (len(self.hashArray)):
      if self.hashArray[i].state is 1:
        numItems += 1
    loadFactor = numItems/(len(self.hashArray))
    return loadFactor
  

  def _resize(self, size):
    extra = None
    if (len(self.hashArray)) % 2 == 0: #even
      extra = 0
    else:
      extra = 1
    newLength = int(self._findNextPrime(((len(self.hashArray)) + extra) * size))
    print(newLength)
    newArray = self.hashArray.copy()
    print(newArray[0].key)
    self.hashArray = [None] * newLength
    for i in range(newLength):
      self.hashArray[i] = DSAHashTable.DSAHashEntry(None, None)
      print("new hash array value = ", self.hashArray[i].key)
      print(self.hashArray[0].state)
      if newArray[i].state == 1:
        #print("yes")
        #self.put("daniel", 19779797)
        self.put(newArray[i].key, newArray[i].value)
      self.hashArray = newArray
        


  def _hash(self, inKey):
    a = 63689
    b = 378551
    hashIdx = 0

    for ii in range (len(inKey)):
      hashIdx = (hashIdx * a) + ord(inKey[ii])
      a *= b
    return hashIdx % (len(self.hashArray))
  
  def _stepHash(self, inKey):
    MAX_STEP = 5
    hashStep = MAX_STEP - (inKey % MAX_STEP)
    return hashStep

  def _findNextPrime(self, startVal):
    if (startVal % 2 == 0):
      primeVal = startVal - 1
    else:
      primeVal = startVal
    
    isPrime = False
    while (not isPrime):
      primeVal = primeVal + 2
      ii = 3
      isPrime = True
      rootVal = math.sqrt(primeVal)
      while (ii <= rootVal) and (isPrime):
        if (primeVal % ii == 0):
          isPrime = False
        else:
          ii = ii + 2
    return primeVal

  class DSAHashEntry():
    def __init__(self, inKey, inValue):
      if (inKey is not None):
        self.key = inKey
        self.value = inValue
        self.state = 1
      else:
        self.key = ""
        self.value = None
        self.state = 0
      
    def _getKey(self):
      return self.key
    
    def _getValue(self):
      return self.value
    
    def _getState(self):
      return self.state

    def _setKey(self, inKey):
      self.key = inKey
    
    def _setValue(self, inValue):
      self.value = inValue
    
    def _setState(self, inState):
      self.state = inState
    


