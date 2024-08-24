import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import datestr2num, DateFormatter, DayLocator
from matplotlib.ticker import AutoMinorLocator
from matplotlib.patches import Patch

# Create dummy date
tasks = ['Вимоги', 'Теорія', 'Практика', 'Підготовка', 'Екзамен', 'Перевірка', 'Перескладання']
start_dates = ['2024-09-01', '2024-09-15', '2024-11-01', '2024-12-15','2025-01-15', '2025-01-16', '2025-01-24']
end_dates = ['2024-09-14', '2024-10-31', '2024-12-14', '2025-01-14','2025-01-15', '2025-01-23', '2025-01-31']

# Setup the dates and calculate durations
start_dates = [datestr2num(d) for d in start_dates]
end_dates = [datestr2num(d) for d in end_dates]

durations = [(end - start) for start, end in zip(start_dates, end_dates)]

fig, ax = plt.subplots(figsize=(15, 8), facecolor='#25253c')

ax.set_facecolor('#25253c')

# Create colours for each task based on categories
colors = ['#7a5195', '#ef5675', '#ffa600'] 
task_colors = [colors[0]] * 3 + [colors[1]] * 3 + [colors[2]] * 1

# Display the bars
ax.barh(y=tasks, width=durations, left=start_dates, 
height=0.8, color=task_colors)

ax.invert_yaxis()

# Setup the x axis labels
ax.set_xlim(start_dates[0], end_dates[-1])

date_form = DateFormatter("%d-%m")
ax.xaxis.set_major_formatter(date_form)

ax.xaxis.set_major_locator(DayLocator(interval=10))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.tick_params(axis='x', which='minor', length=2, color='white', labelsize=6)

ax.get_yaxis().set_visible(False)

# Control the colour of the grid for major and minor lines
ax.grid(True, axis='x', linestyle='-', color='#FFFFFF', alpha=0.2, which='major')
ax.grid(True, axis='x', linestyle='-', color='#FFFFFF', alpha=0.05, which='minor')
ax.set_axisbelow(True)

# Add labels for each task. For padding, we can use an f-string and add some extra space
for i, task in enumerate(tasks):
    ax.text(start_dates[i], i, f'  {task}', ha='left', va='center', color='white', fontsize=12, fontweight='bold')

# Add the current date line
today = datetime.datetime.now().strftime("%Y-%m-%d")
today_num = datestr2num(today)
ax.axvline(today_num, color='red', alpha=0.8)

# Style ticks, labels and colours
ax.tick_params(axis='both', colors='white')

ax.set_xlabel('Дати', color='white', fontsize=12)
ax.set_title('Проходження навчального курсу', color='white', fontsize=14)

# Hide spines so only bottom is visible
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Create a list of custom patches for the legend
legend_elements = [
    Patch(facecolor=colors[0], label='Навчання'),
    Patch(facecolor=colors[1], label='Екзамен'),
    Patch(facecolor=colors[2], label='Перескладання'),
]

# Add the legend in the top right corner of the plot
ax.legend(handles=legend_elements, loc='upper right', 
          facecolor='white', 
          edgecolor='white', 
          fontsize=10, title='Етапи', title_fontsize=12, frameon=True)

plt.show()