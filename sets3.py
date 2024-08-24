import matplotlib.pyplot as plt
from matplotlib_venn import venn2
 
v = venn2(subsets = (1, 1,1), set_labels = ('Всі сторони є рівними', 'Сторін більше 3'))

v.get_label_by_id('10').set_text('1. Правильний\n Трикутник')
v.get_label_by_id('01').set_text('1. Довільний\n Пентагон \n 2. Прямокутник')
v.get_label_by_id('11').set_text('1. Квадарт')
plt.show()


# Правильний Трикутник
# Квадарт
# Довільний Пентагон

# Всі сторони є рівними
# Сторін більше 3
