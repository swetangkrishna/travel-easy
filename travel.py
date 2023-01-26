class nodes:
    def __init__(self, node_name, node_dist=0, node_adjacent=1):
        self.name = node_name
        #distance from initial point
        self.dist = node_dist
        self.addjacent = node_adjacent

#the places will be marked with A,B,C,D... and so on
n = int(input("Enter the number of places to visit."))
print(n)

#initial location is taken as 'A'
print("let's suppose your input is divided into " + str(n) + " characters starting from A to " + chr(64 + n))
print(chr(65) + " being the initial point")

#specifying the distance between the points
print("Enter the distances from initial point to all the points and if there is no direct path from initial point then input x")

for i in range(1,n+1):
    globals()[f"{chr(64+i)}"] = nodes(str(chr(64+i)),"","")
    #if there is no direct path to initial point then input x
    globals()[f"{chr(64+i)}"].dist = input("Enter the distance from intial point to "+ str(chr(64+i)))
    globals()[f"{chr(64+i)}"].adjacent = input("Enter the number of adjacent points from "+ str(chr(64+i)))


for i in range(1,n+1):
    print(globals()[f"{chr(64+i)}"].name)
    print(globals()[f"{chr(64+i)}"].dist)
    print(globals()[f"{chr(64+i)}"].adjacent)