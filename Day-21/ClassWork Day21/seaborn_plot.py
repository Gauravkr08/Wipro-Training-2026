import seaborn as sns
import matplotlib.pyplot as plt

marks = [50, 60, 70, 80, 90, 65]

sns.set_style("whitegrid")
sns.histplot(data=marks, bins=5)

plt.title("Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()
