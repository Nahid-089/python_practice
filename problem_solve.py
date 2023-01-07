myDict = {
    "pankha": "fan",
    "dabba": "box",
    "vastu": "item"
}
print("Options are", myDict.keys())
a = input("Enter The Hindi Word")
#print("The Meanig Of Your Word is:", myDict[a])
print("The Meanig Of Your Word is:", myDict.get(a))