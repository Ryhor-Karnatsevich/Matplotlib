import matplotlib.pyplot as plt
list1 = [1970,1980,1990,2000,2010,2020,2030,2040]
list2 = [2,4,8,16,32,100,80,150]
list3 = ["70th","80th","90th","00th","10th","20th","30th","40th"]
list4 = ["2b","4b","8b","16b","32b","100b","80b","150b"]
plt.yscale('log')
plt.plot(list1,list2)
plt.xlabel('year')
plt.ylabel('average')
plt.title('My First Plot')
plt.yticks(list2,list4)



plt.savefig('plot.png')  # Сохранение графика как изображение


plt.close()