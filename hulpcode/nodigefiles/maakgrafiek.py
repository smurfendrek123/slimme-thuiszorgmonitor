import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
f= open('datafile.txt','r')
lines=f.readlines()
f.close()

plt.plot(lines)
plt.show()
