# Pie Chart

from matplotlib import pyplot as plt

continents = ["North America", "South America", "Europe", "Asia", "Africa"]
population = [579000000, 422000000, 741000000, 4463000000, 1216000000]
explode = (0, 0, 0.1, 0, 0)
plt.pie(population,autopct="%1.1f%%",explode=explode)
plt.legend(continents)
plt.title("World Populations By Continents")
plt.axis("equal")
plt.show()