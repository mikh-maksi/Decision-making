import matplotlib.pyplot as plt
from matplotlib_venn import venn2
 
v = venn2(subsets = (1, 1,1), set_labels = ('Управління', 'Технології'))

v.get_label_by_id('10').set_text('1.Менеджмент\n 2.Маркетинг')
v.get_label_by_id('01').set_text('1.Програмування \n 2.Аналіз даних  ')
v.get_label_by_id('11').set_text('1.Економічна \n кібернетика')
plt.show()
