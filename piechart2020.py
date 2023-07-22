import matplotlib.pyplot as plt
party=['bjp','cng','sp','bsp','other']
votes=[1000,300,450,600,180]
plt.axis("equal")

plt.pie(votes,labels=party,radius=1.5,shadow=True,explode=[0,0.2,0,0,0],autopct='%0.2f%%',startangle=180)
plt.show()