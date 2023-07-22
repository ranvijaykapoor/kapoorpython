import matplotlib.pyplot as plt
day=[1,2,3,4,5,6,7]
temp_max=[40,36,50,28,17,29,46]
temp_min=[50,10,8,10,6,1,8]
#plt.plot(day,temp,color="red",marker="D",markersize='20')
plt.plot(day,temp_max,color="red",label="max")
plt.plot(day,temp_min,color="green",label="min")
plt.xlabel('Day')
plt.ylabel('Temprature')
plt.title('wether info')
plt.legend(loc="best",shadow="true",fontsize="large")
plt.grid()
plt.savefig("weather.png")
plt.show()