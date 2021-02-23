text = open("Maze.txt") #opens the text file
a = text.read().replace("/n", " ") #splits the Trues and Falses into rows
b = list(a) #makes a list of Trues and Falses from a
print(b)
