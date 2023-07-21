import pickle

data = []
with open("prompt.txt") as f:
    data = f.readlines()

diction = []

for i in data:
    a = str(i)
    diction.append(a[0:len(i)-1])
    h, l = img.size
    print(h,l)

try:
    with open("data.pickle", "wb") as f:
        pickle.dump(diction, f, protocol=pickle.HIGHEST_PROTOCOL)
except Exception as ex:
    print("Error during pickling object (Possibly unsupported):", ex)
