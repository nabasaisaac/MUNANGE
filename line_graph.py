import sqlite3

import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime
import matplotlib.dates as mdates
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt  # Import matplotlib's pyplot module
from matplotlib.font_manager import FontProperties

connection = sqlite3.connect("munange.db")
cursor = connection.cursor()
cursor.execute("SELECT loan_date, CAST(amount AS INT) FROM loans WHERE status='on going'")
data = cursor.fetchall()
cursor.close()
connection.close()
# print(data)
dictionary_data = {}
for key, value in data:
    if key in dictionary_data.keys():
        dictionary_data[key] += value
        pass
    else:
        dictionary_data[key] = value

new_dict_data = [{'loan_date':date, 'amount':amount} for
                 date, amount in dictionary_data.items()]
new_dict_data.sort(key=lambda x: datetime.datetime.strptime(x['loan_date'], '%d-%b-%Y'))

print(new_dict_data)

# Extract x and y values
x = [datetime.datetime.strptime(entry['loan_date'], '%d-%b-%Y') for entry in new_dict_data]
y = [entry['amount'] for entry in new_dict_data]

print(y)
# Spline interpolation for smoother line
x_numeric = mdates.date2num(x)
spl = make_interp_spline(x_numeric, y, k=3)  # k=3 for cubic spline
x_smooth = np.linspace(x_numeric.min(), x_numeric.max(), 300)
y_smooth = spl(x_smooth)
x_smooth_dates = mdates.num2date(x_smooth)


class LineGraph:
    def __init__(self, display_frame):
        self.display_frame = display_frame

        # Create a figure for the line graph
        figure = Figure(figsize=(9, 4), dpi=90)
        plot = figure.add_subplot(1, 1, 1)

        # Advanced line plot
        plot.plot(x_smooth_dates, y_smooth, color='#4CC053', linewidth=2)
        plot.fill_between(x_smooth_dates, y_smooth, color='#4CC053', alpha=0.2)
        figure.subplots_adjust(left=0.05, right=1, top=0.8, bottom=0.1)

        # Adding markers
        points = plot.scatter(x, y, color='#4CC053', edgecolors='w', linewidth=1, zorder=5)

        # Format the date on the x-axis
        plot.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
        plot.xaxis.set_major_locator(mdates.MonthLocator())

        # Customize grid and background
        plot.grid(color='white', linestyle='--', linewidth=0.5, alpha=0.7)
        figure.patch.set_facecolor('white')
        plot.set_facecolor('white')

        # Customize plot appearance
        plot.set_title('Loan Distribution Over Time', fontsize=18, color='#0C2844', pad=10)
        plot.set_xlabel('Loan Date', fontsize=14, color='#0C2844', labelpad=-10)
        plot.set_ylabel('Loan Amount', fontsize=14, color='#0C2844', labelpad=-10)
        plot.tick_params(axis='x', colors='white')
        plot.tick_params(axis='y', colors='white')

        # Remove y-axis numerical values (keep label)
        plot.yaxis.set_major_locator(plt.NullLocator())
        plot.yaxis.set_minor_locator(plt.NullLocator())

        font = FontProperties()
        font.set_family('serif')  # Example: 'serif', 'sans-serif', 'monospace', etc.
        font.set_size(10)

        # Tooltip
        annot = plot.annotate("", xy=(0, 0), xytext=(15, 15), textcoords="offset points",
                              bbox=dict(boxstyle="round,pad=0.5", fc="#44aaee", ec="#44aaee", alpha=0.7),
                              arrowprops=dict(arrowstyle="->", color='#44aaee'),
                              fontproperties=font)

        annot.set_visible(False)
        ax = plot.axes
        ax.spines[['top', 'right', 'left', 'bottom']].set_visible(False)

        def update_annot(event):
            vis = annot.get_visible()
            if event.inaxes == plot:
                cont, ind = points.contains(event)
                if cont:
                    index = ind["ind"][0]
                    x = points.get_offsets()[index, 0]
                    y = points.get_offsets()[index, 1]
                    annot.xy = (x, y)
                    text = f'{mdates.num2date(x).strftime("%b %d")}\nLoan: UGX {y:,.1f}'
                    annot.set_text(text)
                    annot.set_visible(True)
                    figure.canvas.draw_idle()
                else:
                    if vis:
                        annot.set_visible(False)
                        figure.canvas.draw_idle()

        figure.canvas.mpl_connect("motion_notify_event", update_annot)

        # Create a FigureCanvasTkAgg widget
        canvas = FigureCanvasTkAgg(figure, master=self.display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=5)

