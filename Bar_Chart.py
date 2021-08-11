import numpy as np

import matplotlib.pyplot as plt

# data to plot

n_groups = 5

means_kachi= (50, 51,48, 44,54)

means_class1 = (45,50,52,29,30)

means_class2=(40,40,44,45,46)

means_class3=(38,37,32,41,42)

means_class4=(41,46,36,30,33)

means_class5=(40,38,50,30,32)

# create plot

fig, ax= plt.subplots()

index = np.arange(n_groups)

bar_width = 0.1

opacity = 0.75

rects1 = plt.bar(index, means_kachi, bar_width,

alpha=opacity,

color='b',

label='Kachi')

rects2 = plt.bar(index + bar_width, means_class1, bar_width,

alpha=opacity,

color='g',

label='class 1')

rects3= plt.bar(index + 2*bar_width, means_class2, bar_width,

alpha=opacity,

color='r',

label='class 2')

rects4 = plt.bar(index + 3*bar_width, means_class3, bar_width,

alpha=opacity,

color='c',

label='class 3')

rects5= plt.bar(index + 4*bar_width, means_class4, bar_width,

alpha=opacity,

color='m',

label='class 4')

rects6 = plt.bar(index +5* bar_width, means_class5, bar_width,

alpha=opacity,

color='y',

label='class 5')

plt.xlabel('Years')

plt.ylabel('Enrolments')

plt.title('Class Wise Enrolments')

plt.xticks(index + bar_width, ('31-10-17', '31-10-18', '31-10-19', '31-10-20','current year'))

plt.legend()

plt.tight_layout()

plt.show()
