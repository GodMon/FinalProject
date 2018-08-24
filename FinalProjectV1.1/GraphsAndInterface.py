"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

The_data = np.loadtxt(open('SimulatedData.csv', 'rb'), delimiter=',', skiprows=0)
Outcome = The_data[:, 0]
Outcome = Outcome.astype(int)
Time = The_data[:, 1]
Cost = The_data[:, 2]
Outcome_Frequency = np.bincount(Outcome)
Total_Cost_List = np.zeros([11, 1])
Average_Cost_List = np.zeros([11, 1])
for i in range(500):
    for j in range(1, 12):
        if Outcome[i] == j:
            one_cost = Cost[i]

            Total_Cost_List[j - 1] = Total_Cost_List[j - 1] + one_cost

for i in range(len(Outcome_Frequency) - 1):
    Average_Cost_List[i] = Total_Cost_List[i] / Outcome_Frequency[i + 1]


class Graph(object):

    def TheBarChart1(self):
        self.input_list = Outcome_Frequency[1:]
        # print (self.input_list)
        self.name_list = ['Admitted', 'Call Closed', 'Discharged', 'Emergency dentist', 'MIU',
                          'Not picked up in an ambulance', 'OOH', 'Out-patient clinic', 'Seen by A&E doctor',
                          'Spoke to a primary care service', 'WIC']
        self.colors = ['b', 'orange', 'g', 'r', 'purple', 'brown', 'pink', 'gray', 'yellow', 'aqua', 'lightskyblue']
        self.BC1 = plt.figure()
        self.BC1_chart = self.BC1.add_subplot(1, 2, 1)
        self.BC1_legend = self.BC1.add_subplot(1, 2, 2)

        self.BC1_chart.set_title('Outcome Distribution')
        self.BC1_chart.set_xlabel('Outcome')
        self.BC1_chart.set_ylabel('Number')
        self.BC1_chart.set_xticks(range(len(self.name_list)))
        self.BC1_chart.bar(range(len(self.input_list)),
                           self.input_list,
                           color=self.colors,
                           width=1)
        self.BC1_ysuitrange_list = []
        for a, b in zip(range(len(Outcome_Frequency) - 1), self.input_list):
            self.BC1_chart.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)
            self.BC1_barnumber = [a]
            self.BC1_xsuitrange = [a - 0.5, a + 0.5]
            self.BC1_ysuitrange = [0, b]
            self.BC1_ysuitrange_list.append(b)
        self.The_maxbar = np.argmax(self.BC1_ysuitrange_list)
        self.The_minbar = np.argmin(self.BC1_ysuitrange_list)

        self.img = Image.open('BarChartLegends.png')
        self.BC1_legend.axis('off')
        self.BC1_legend.imshow(self.img)

        self.BC1.canvas.mpl_connect('button_press_event', Graph.onclick_BC1)
        plt.show()

        return (self.The_maxbar, self.The_minbar)

    def ThePieChart1(self):
        self.input_list = Outcome_Frequency[1:]
        self.The_maxbar = np.argmax(self.input_list) + 1
        self.The_minbar = np.argmin(self.input_list) + 1
        self.name_list = ['1 Admitted', '2 Call Closed', '3 Discharged', '4 Emergency dentist', '5 MIU',
                          '6 Not picked up in an ambulance', '7 OOH', '8 Out-patient clinic', '9 Seen by A&E doctor',
                          '10 Spoke to a primary care service', '11 WIC']
        self.colors = ['b', 'orange', 'g', 'r', 'purple', 'brown', 'pink', 'gray', 'yellow', 'aqua', 'lightskyblue']
        self.PC1 = plt.figure()
        self.PC1_chart = self.PC1.add_subplot(1, 1, 1)
        self.PC1_chart = plt.pie(self.input_list,
                                 labels=self.name_list,
                                 labeldistance=1.1,
                                 pctdistance=0.6,
                                 startangle=90,
                                 autopct='%.1f%%',
                                 shadow=True,
                                 colors=self.colors
                                 )
        plt.title('Outcome Distribution')
        plt.axis('equal')
        plt.legend(bbox_to_anchor=(1, 1),
                   bbox_transform=plt.gcf().transFigure)

        self.PC1.canvas.mpl_connect('button_press_event', Graph.onclick_PC1)

        plt.show()
        return (self.The_maxbar, self.The_minbar)

    def TheBarChart2(self):
        self.input_list = Average_Cost_List
        self.name_list = ['Admitted', 'Call Closed', 'Discharged', 'Emergency dentist', 'MIU',
                          'Not picked up in an ambulance', 'OOH', 'Out-patient clinic', 'Seen by A&E doctor',
                          'Spoke to a primary care service', 'WIC']
        self.colors = ['b', 'orange', 'g', 'r', 'purple', 'brown', 'pink', 'gray', 'yellow', 'aqua', 'lightskyblue']
        self.BC2 = plt.figure()
        self.BC2_chart = self.BC2.add_subplot(1, 2, 1)
        self.BC2_legend = self.BC2.add_subplot(1, 2, 2)

        self.BC2_chart.set_title('Average Cost in Different Outcomes')
        self.BC2_chart.set_xlabel('Outcome')
        self.BC2_chart.set_ylabel('Average Cost(GBP)')
        self.BC2_chart.set_xticks(range(len(self.name_list)))

        for i in range(len(Average_Cost_List)):
            self.BC2_chart.bar(i, self.input_list[i], color=self.colors[i], width=1)

        self.BC2_ysuitrange_list = []
        for a, b in zip(range(len(Average_Cost_List)), self.input_list):
            self.BC2_chart.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)
            self.BC2_barnumber = [a]
            self.BC2_xsuitrange = [a - 0.5, a + 0.5]
            self.BC2_ysuitrange = [0, b]
            self.BC2_ysuitrange_list.append(b)
        self.The_maxbar = np.argmax(self.BC2_ysuitrange_list)
        self.The_minbar = np.argmin(self.BC2_ysuitrange_list)

        self.img = Image.open('BarChartLegends.png')
        self.BC2_legend.axis('off')
        self.BC2_legend.imshow(self.img)

        self.BC2.canvas.mpl_connect('button_press_event', Graph.onclick_BC2)

        plt.show()
        return (self.The_maxbar, self.The_minbar)

    def TheBoxPlot2(self):
        self.boxplot_array = np.zeros([5, 11])
        self.calculation_list = []
        self.calculated_list = []
        self.BP2 = plt.figure()
        self.BP2_chart = self.BP2.add_subplot(1, 2, 1)
        self.BP2_legend = self.BP2.add_subplot(1, 2, 2)
        for i in range(1, 12):
            for j in range(500):
                if Outcome[j] == i:
                    self.calculation_list.append(Cost[j])
            self.calculated_list = np.percentile(self.calculation_list, [0, 25, 50, 75, 100])
            self.calculation_list = []
            for k in range(5):
                self.boxplot_array[k, i - 1] = self.calculated_list[k]
        self.BP2_chart.set_xlabel('Outcome')
        self.BP2_chart.set_ylabel('One Record Cost(GBP)')
        self.BP2_chart.set_title('One Time Cost Distribution')
        self.BP2_ysuitrange_listmax = []
        self.BP2_ysuitrange_listmin = []
        self.BP2_chart.boxplot(self.boxplot_array, widths=1)
        for a, b in zip(range(len(Outcome_Frequency) - 1), self.boxplot_array[4, :]):
            self.BP2_chart.text(a + 1, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)
            self.BP2_ysuitrange_listmax.append(b)
        self.The_maxbar = np.argmax(self.BP2_ysuitrange_listmax) + 1
        for a, b in zip(range(len(Outcome_Frequency) - 1), self.boxplot_array[0, :]):
            self.BP2_ysuitrange_listmin.append(b)
        self.The_minbar = np.argmin(self.BP2_ysuitrange_listmin) + 1

        self.img = Image.open('BoxPlotLegends.png')
        self.BP2_legend.axis('off')
        self.BP2_legend.imshow(self.img)
        self.BP2.canvas.mpl_connect('button_press_event', Graph.onclick_BP2)
        plt.show()
        return (self.The_maxbar, self.The_minbar)

    def onclick_BC1(event):
        a, b = Graph.TheBarChart1(Graph)
        plt.close()
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata))
        if (event.xdata > a - 0.5) and (event.xdata <= a + 0.5):
            print('BC1: Maximum: Right')
        elif (event.xdata > b - 0.5) and (event.xdata <= b + 0.5):
            print('BC1: Minimum: Right')
        else:
            print('BC1: No Maximum or Minimum')

    def onclick_BC2(event):
        a, b = Graph.TheBarChart2(Graph)
        plt.close()
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata))
        if (event.xdata > a - 0.5) and (event.xdata <= a + 0.5):
            print('BC2: Maximum: Right')
        elif (event.xdata > b - 0.5) and (event.xdata <= b + 0.5):
            print('BC2: Minimum: Right')
        else:
            print('BC2: No Maximum or Minimum')

    def onclick_PC1(event):
        a, b = Graph.ThePieChart1(Graph)
        plt.close()
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata))
        PC1_answer1 = input('What is the No. of Maximum Outcome?')
        i = int(PC1_answer1)
        if a == i:
            print('PC1: Maximum: Right')
        else:
            print('PC1: Maximum: Wrong')
        PC1_answer2 = input('What is the No. of Minimum Outcome?')
        i = int(PC1_answer2)
        if b == i:
            print('PC1: Minimum: Right')
        else:
            print('PC1: Minimum: Wrong')

    def onclick_BP2(event):
        a, b = Graph.TheBoxPlot2(Graph)
        plt.close()
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata))
        if (event.xdata > a - 0.5) and (event.xdata <= a + 0.5):
            print('BP2: Maximum: Right')
        elif (event.xdata > b - 0.5) and (event.xdata <= b + 0.5):
            print('BP2: Minimum: Right')
        else:
            print('BP2: No Maximum or Minimum')

