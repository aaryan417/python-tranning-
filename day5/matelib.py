import matplotlib.pyplot as plt

player = ["prashant", "patti", "messi", "haaland"]
goals = [9, 8, 0, 0]

plt.bar(player, goals)

plt.xlabel("Player")
plt.ylabel("Goals")

plt.show()
plt.plot(player, goals)
plt.show()



