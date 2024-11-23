import matplotlib.pyplot as plt
a = [1,3,7,1,9,2,2.2,3.9,4,5,3,2,9,3.4,6,7,8.5,9,12]
plt.hist(a, bins = 10)
plt.savefig('histogram.png')
plt.clf()
