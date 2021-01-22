class DSABinarySearchTree():
    def __init__(self):
        self._root = None  #start with an empty tree

    def find(self, key):
        return self._findRec(key, self._root)

    def _findRec(self, key, cur):
        value = None
        if cur == None:
            print("Key ", key, " not found")

        elif key == cur._key:
            value = cur._value

        elif key < cur._key:
            value = self._findRec(key, cur._left)

        else:
            value = self._findRec(key, cur._right)
        return value

    def insert(self, key, value):
        self._insertRec(key, value, self._root)

    def _insertRec(self, key, value, cur):
        updateNode = cur
        if(cur == None):
            if(self._root == None):
                self._root = DSABinarySearchTree.DSATreeNode(key, value)
            else:
                newNode = DSABinarySearchTree.DSATreeNode(key, value)
                updateNode = newNode

        elif(key == cur._key):
            print("Key already exists")
            print(key)
        elif(key < cur._key):
            cur.setLeft(self._insertRec(key, value, cur._left))
            cur = cur._left
        else:
            cur.setRight(self._insertRec(key, value, cur._right))
            cur = cur._right
        return updateNode

    def delete(self, key):
        self._deleteRec(key,self._root)

    def _deleteRec(self, key, curNode):
        updateNode = curNode
        if(curNode == None):
            print("Not possible")
        elif(key == curNode._key):
            updateNode = self._deleteNode(key,curNode)
        elif(key < curNode._key):
            curNode.setLeft(self._deleteRec(key,curNode._left))
        else:
            curNode.setRight(self._deleteRec(key,curNode._right))
        return updateNode  

    def _deleteNode(self, key, delNode):
        updateNode = None
        if(delNode._left == None and delNode._right == None):
            updateNode = None
        elif(delNode._left != None and delNode._right == None):
            updateNode = delNode._left
        elif(delNode._left == None and delNode._right != None):
            updateNode = delNode._right
        else:
            updateNode = self._promoteSuccessor(delNode._right)
            if(updateNode != delNode._right):
                updateNode.setRight(delNode._right)
            updateNode.setLeft(delNode._left)
        return updateNode
        
    def _promoteSuccessor(self, curNode):
        successor = curNode
        if(curNode._left != None):
            successor = self._promoteSuccessor(curNode._left)
            if(successor == curNode._left):
                curNode.setLeft(successor._right)
        return successor

    def traverseInOrder(self):
        return self._traverseInOrderRec(self._root)

    def _traverseInOrderRec(self, curNode):
        result = []
        if(curNode != None):
            result = self._traverseInOrderRec(curNode._left)
            result.append(curNode._key)
            result = result + self._traverseInOrderRec(curNode._right)
        return result

    def balance(self):
            result = self._traverseInOrderRec(self._root)
            numLeft = result.index(self._root._key)
            numRight = len(result) - numLeft
            balancePercent = (abs(numLeft-numRight)/((numLeft+numRight)/2)) #using equation for percentage difference
            asPercentage = "{:.0%}".format(balancePercent)
            if(numLeft < numRight):
                concatResult = "Balance = right biased: " + asPercentage
            else:
                concatResult = "Balance = left biased: " + asPercentage
            return concatResult

    def traversePreOrder(self):
        return self._traversePreOrderRec(self._root)

    def _traversePreOrderRec(self, curNode):
        result = []
        if(curNode != None):
            result.append(curNode._key)
            result = result + self._traversePreOrderRec(curNode._left)
            result = result + self._traversePreOrderRec(curNode._right)
        return result
    
    def traversePostOrder(self):
        return self._traversePostOrderRec(self._root)

    def _traversePostOrderRec(self, curNode):
        result = []
        if(curNode != None):
            result = self._traversePostOrderRec(curNode._left)
            result = result + self._traversePostOrderRec(curNode._right)
            result.append(curNode._key)
        return result

    def height(self):
        return self._heightRec(self._root)
    
    def _heightRec(self, curNode):
        if(curNode == None):
            htSoFar = -1
        else:
            leftHt = self._heightRec(curNode._left)
            rightHt = self._heightRec(curNode._right)
            if(leftHt > rightHt):
                htSoFar = leftHt + 1
            else:
                htSoFar = rightHt + 1
        return htSoFar

    def min(self):
        return self._minRec(self._root)

    def _minRec(self, curNode):
        if(curNode._left != None):
            minKey = self._minRec(curNode._left)
        else:
            minKey = curNode._key
        return minKey
    
    def max(self):
        return self._maxRec(self._root)

    def _maxRec(self, curNode):
        if(curNode._right != None):
            maxKey = self._maxRec(curNode._right)
        else:
            maxKey = curNode._key
        return maxKey
    
    class DSATreeNode():
        def __init__(self, inKey, inValue):
            self._key = inKey
            self._value = inValue
            self._left = None
            self._right = None

        def __str__(self):
            return ("Key: " + str(self._key) + " Value: " + str(self._value))
        
        def getKey(self):
            return self._key
        
        def getValue(self):
            return self._value

        def getLeft(self):
            return self._left
        
        def setLeft(self, newLeft):
            self._left = newLeft
        
        def getRight(self):
            return self._right
        
        def setRight(self, newRight):
            self._right = newRight

