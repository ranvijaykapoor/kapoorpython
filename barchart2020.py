import matplotlib.pyplot as plt
import numpy as np
company=('techsrijan','google','microsoft','crompton')
revenue=(500,10000,1500,2000)
profit=(200,8000,1200,500)
xpos=np.arange(len(company))
print(xpos)
#plt.bar(company, revenue, label="revenue",color="green")
#plt.bar(company, profit, label="profit",color="red")

plt.bar(xpos-0.2, revenue, label="revenue",color="green",width=0.4)
plt.bar(xpos+0.2, profit, label="profit",color="red",width=0.4)
plt.xticks(xpos,company)
plt.ylabel("revenue  in million")
plt.title("compny profit loss")
#plt.grid()
plt.legend()
plt.show()