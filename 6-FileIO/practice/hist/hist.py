import matplotlib.pyplot as plt

dict = {}
with open("anthem_cp.txt", "r") as anthem:
    data = anthem.readlines()
with open(
    "anthem_cp.txt",
    "w",
) as anthem:
    for line in data:
        anthem.write(line.replace(",", "").replace(";", "").replace(".", ""))
with open("anthem_cp.txt", "r") as anthem:
    for line in anthem.readlines():
        for word in line.split():
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
plt.plot(x=[x for x in dict.keys()], height=[x for x in dict.values()])
plt.show()
