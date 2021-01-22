import graphMenu
import GraphLinkedList

def menu():
  f = GraphLinkedList.DSAGraph()
  p = graphMenu.cryptoMenu()
  p.chooseMode(f)

menu()