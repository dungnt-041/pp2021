import pickle
temp = []
for i in range(ord('A'), ord('Z') + 1):
    try:
        f = open("C:/Users/G40/Desktop/Human Resource/Database/Staff{}.pickle".format(chr(i)), "rb")
        f.close()
        temp.append(chr(i))
    except:
        continue 
print(temp)