import matplotlib.pyplot as plt
 
# defining labels
activities = ['read', 'sleep', 'study', 'play']
 
# portion covered by each label
slices = [3, 7, 5, 7]
 
# color for each label
colors = ['r', 'c', 'g', 'b']
 
# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors, 
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')
 
# plotting legend
plt.legend()
 
# showing the plot
plt.show()






































