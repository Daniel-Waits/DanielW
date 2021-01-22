import pickle
import json
import GraphLinkedList
import csv
import sys
import graphVisualiser
import BinarySearchTree
sys.setrecursionlimit(100000000) # Increase recursion limit for serialising

c = GraphLinkedList.DSAGraph()
assetFile = r'F:\OneDrive - Curtin University of Technology Australia\Uni\Y2S2\COMP1002-Data Structures and Algorithms\Python\Assignment\assetFile.json'
dayTrades = r'F:\OneDrive - Curtin University of Technology Australia\Uni\Y2S2\COMP1002-Data Structures and Algorithms\Python\Assignment\24hrTrades.json'
saveFile = r'F:\OneDrive - Curtin University of Technology Australia\Uni\Y2S2\COMP1002-Data Structures and Algorithms\Python\Assignment\saveFile.pkl'
assetInfo = r'F:\OneDrive - Curtin University of Technology Australia\Uni\Y2S2\COMP1002-Data Structures and Algorithms\Python\Assignment\assetInfo.json'
class cryptoMenu():
    def chooseMode(self, object):
        if len(sys.argv) < 2:
            self.usageInformation()
        else:
            mode = sys.argv[1]
            if mode == "-i":
                self.interactiveMode(object)
            elif mode == "-r":
                if len(sys.argv) < 4:
                    print("Please run again and enter 3 files, assetFile, 24hr trades, and assetInfo!")
                self.reportMode(object, None, None, None)

    def interactiveMode(self, object):
        dataLoaded = False
        while True:
            self._printOptions()
            choice = self._inputNum("Please choose a menu item: ")
            if choice == 1:
                #load data
                self._printOpt1SubOptions()
                choice1 = self._inputNum("Please choose a menu item: ")
                if choice1 == 1:
                    self._readFile(object)
                    dataLoaded = True
                    print("------Data successfully imported!------")
                elif choice1 == 2:
                    object = self.load(saveFile)
                    dataLoaded = True
                    print("------Data successfully imported!------")
                else:
                    print('\033[91m'"Incorrect choice, press 1 and try again!"'\033[0m')
            elif choice == 2 and dataLoaded:
                #find and display asset
                value = self._inputString("Please input an asset symbol, to get a visual overview of it (e.g. BTC)(input none for broad asset overview): ")
                print("--------Asset overview!--------")
                if value == "":
                    object.assetOverview()
                    object.visualiseGraph()
                else:
                    object.visualiseAsset(value)
                print("--------Asset overview!--------")
            elif choice == 3 and dataLoaded:
                #find and display trade details
                value = self._inputString("Please input a trade symbol to find its' details (e.g. ETHBTC): ")
                print("------Trade details found!------")
                object.getTradeDetails(value)
                print("------Trade details found!------")
            elif choice == 4 and dataLoaded:
                #find and display potential trade paths
                print("Please input a base asset and quote asset to display direct and indirect paths between the two: ")
                value = self._inputString("Base asset (e.g. BTC): ")
                value1 = self._inputString("Quote asset (e.g. ETH): ")
                object.printAllPaths(value, value1)
            elif choice == 5 and dataLoaded:
                #set asset filter
                value = self._inputString("Please input an asset symbol, to ignore all its' trade pairs (e.g. BTC): ")
                object.addAssetFilter(value)
                print("------Asset", value, "successfully ignored!------")
            elif choice == 6 and dataLoaded:
                #asset overview
                value = self._inputString("Please input an assets' symbol to find its' details (e.g. BTC): ")
                print("------Asset details found!------")
                object.getAssetDetails(value)
                print("------Asset details found!------")
            elif choice == 7 and dataLoaded:
                #trade overview
                object.getTopTenPrice()
                object.getTopTenVolume()
                object.getTopTenGain()
            elif choice == 8:
                #save data
                self.save(saveFile, object)
                print("------Object saved successfully!------")
                #print(load(saveFile))
            elif choice == 9:
                #exit
                break

    def usageInformation(self):
        print("------------------")
        print("Usage Information:")
        print("In order to run this program, you have 2 options. You can run with -i or -r at the end. (e.g. python cryptoGrapy.py -i).")
        print("-i is an interactive mode where you can choose from a menu of options pre decided options.")
        print("-r is report mode, where you pass a file to the program, and it will return some useful statistics on the dataset.")
        print("------------------")

    def reportMode(self, object, file1, file2, file3):
        if file1 is None:
            file1 = sys.argv[2]
        if file2 is None:
            file2 = sys.argv[3]
        if file3 is None:
            file3 = sys.argv[4]    
        self._readFileUnknown(file1, file2, file3, object)
        object.printStats()
        object.visualiseGraph()

        
    def _inputNum(self, prompt):
        while True:
            try:
                num = int(input(prompt))
                break
            except ValueError:
                pass
        return num
    
    def _inputString(self, prompt):
        while True:
            try:
                string = str(input(prompt))
                break
            except TypeError:
                pass
        return string

    def _printOptions(self):
        print("1 -> Load/reload data")
        print("2 -> Find and display asset")
        print("3 -> Find and display trade details")
        print("4 -> Find and display potential trade paths")
        print("5 -> Set asset filter")
        print("6 -> Asset overview")
        print("7 -> Trade overview")
        print("8 -> Save data")
        print("9 -> Quit")
    
    def _printOpt1SubOptions(self):
        print("1 -> Load Asset and Trade data")
        print("2 -> Load Serialised data from file")

    def _readFile(self, object):
        with open(assetFile) as f:
            data = json.load(f)
        with open(dayTrades) as f1:
            data1 = json.load(f1)
        with open(assetInfo) as f2:
            data2 = json.load(f2)
        for i, j, k in zip(data['symbols'], data1, data2):
            object.addVertex(k['Retrieved: 21/10/20'], k['__0'], k['__1'], float(k['__3'].replace(',','')), k['__5'], float(k['__6'].replace(',','')), k['__7'], k['__8'], float(k['__9']))
            object.addEdge(i['baseAsset'], i['quoteAsset'], i['symbol'], j['priceChange'], j['priceChangePercent'], j['weightedAvgPrice'], j['prevClosePrice'], j['lastPrice'], j['highPrice'], j['lowPrice'])
    
    def _readFileUnknown(self, file, file1, file2, object):
        with open(file) as f:
            data = json.load(f)
        with open(file1) as f1:
            data1 = json.load(f1)
        with open(file2) as f2:
            data2 = json.load(f2)
        for i, j, k in zip(data['symbols'], data1, data2):
            object.addVertex(k['Retrieved: 21/10/20'], k['__0'], k['__1'], float(k['__3'].replace(',','')), float(k['__5']), k['__6'], float(k['__7']), float(k['__8']), float(k['__9']))
            object.addEdge(i['baseAsset'], i['quoteAsset'], i['symbol'], j['priceChange'], j['priceChangePercent'], j['weightedAvgPrice'], j['prevClosePrice'], j['lastPrice'], j['highPrice'], j['lowPrice'])

    def _printFileNames(self):
        print("assetFile =", assetFile)
        print("dayTrades =", dayTrades)
        print("saveFile =", saveFile)
        print("assetInfo =", assetInfo)

    def load(self, fileName):
        try:
            with open(fileName, "rb") as dataFile:
                return pickle.load(dataFile)
        except:
            print("Error Saving")

    def save(self, fileName, object):
        try:
            with open(fileName, "wb") as dataFile:
                pickle.dump(object, dataFile)
        except:
            print("Error Saving")