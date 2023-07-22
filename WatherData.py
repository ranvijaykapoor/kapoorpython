import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[40,36,50,28,17,29,46]
plt.plot(x,y,color='red',linewidth=5,linestyle='dotted')
plt.xlabel('Day')
plt.ylabel('Temprature')
plt.title('wether info')
plt.show()