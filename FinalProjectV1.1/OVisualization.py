import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from PIL import Image


class OVisualization():
    def __init__(self):
        self.Odata = np.loadtxt(open('NRandomGeneratorData.csv', 'rb'), delimiter=',', skiprows=0, dtype=str)
        # print (self.Odata)
        self.Odata_Gender = self.Odata[:, 0]
        # print (self.Odata_Gender)
        self.Odata_Age = self.Odata[:, 1]
        self.Odata_Condition = self.Odata[:, 2]
        self.Odata_Outcome = self.Odata[:, 3]
        self.Odata_Cost = self.Odata[:, 4]

    def Obasicinformation(self):
        self.bi = plt.figure()

        self.bi_genderpie = self.bi.add_subplot(1, 3, 1)  # pie chart gender

        self.genderclass = Counter(self.Odata_Gender)
        self.male = self.genderclass['Male']
        self.female = self.genderclass['Female']
        self.numlist_gender = []
        self.numlist_gender.append(self.male)
        self.numlist_gender.append(self.female)
        self.namelist_gender = ['Male', 'Female']
        self.colorlist_gender = ['burlywood', 'pink']
        self.bi_genderpie = plt.pie(
            self.numlist_gender,
            labels=self.namelist_gender,
            labeldistance=1.1,
            pctdistance=0.8,
            startangle=90,
            autopct='%.1f%%',
            shadow=True,
            colors=self.colorlist_gender)
        plt.title('Gender')
        plt.axis('equal')

        self.bi_agepie = self.bi.add_subplot(1, 3, 2)  # pie chart age

        self.ageclass = Counter(self.Odata_Age)
        self.numlist_age = [self.ageclass['0~4'], self.ageclass['5~19'], self.ageclass['20~64'], self.ageclass['65+']]
        self.namelist_age = ['0~4', '5~19', '20~64', '65+']
        # for i in self.ageclass:
        #     self.numlist_age.append(self.ageclass[str(i)])
        #     self.namelist_age.append(i)
        # print (self.numlist_age)
        # print (self.namelist_age)
        self.colorlist_age = ['yellow', 'limegreen', 'olive', 'deeppink']
        self.bi_agepie = plt.pie(
            self.numlist_age,
            labels=self.namelist_age,
            labeldistance=1.1,
            pctdistance=0.8,
            startangle=90,
            autopct='%.1f%%',
            shadow=True,
            colors=self.colorlist_age)
        plt.title('Age Group')
        plt.axis('equal')

        self.bi_conditionpie = self.bi.add_subplot(1, 3, 3)  # pie chart condition
        self.conditionclass = Counter(self.Odata_Condition)
        self.numlist_condition = [self.conditionclass['Unknown'], self.conditionclass['Cardiac conditions'],
                                  self.conditionclass['Respiratory conditions'],
                                  self.conditionclass['Central Nervous System conditions'],
                                  self.conditionclass['Gastrointestinal conditions'],
                                  self.conditionclass['Collapse'], self.conditionclass['Falls'],
                                  self.conditionclass['Dislocation/fracture/joint injury/amputation']]
        self.namelist_condition = ['Unknown',
                                   'Cardiac conditions',
                                   'Respiratory conditions',
                                   'Central Nervous System conditions',
                                   'Gastrointestinal conditions', 'Collapse',
                                   'Falls',
                                   'Dislocation/fracture/joint injury/amputation']

        print(self.namelist_condition)
        self.colorlist_condition = ['skyblue', 'salmon', 'khaki', 'mediumpurple', 'darkorange', 'mediumseagreen',
                                    'darkgrey', 'purple']
        self.bi_conditionpie = plt.pie(
            self.numlist_condition,
            labels=self.namelist_condition,
            labeldistance=1.1,
            pctdistance=0.8,
            startangle=90,
            autopct='%.1f%%',
            shadow=True,
            colors=self.colorlist_condition)
        plt.title('Condition')
        plt.axis('equal')

        plt.suptitle('OVisualization Basic Information of Patients (2500 Records from Random Generators)')
        plt.show()

    def Ooutcomedistribution(self):
        self.od = plt.figure()

        self.outcomeclass = Counter(self.Odata_Outcome)
        self.numlist_outcome = [self.outcomeclass['Admitted'], self.outcomeclass['Not picked up in an ambulance'],
                                self.outcomeclass['Emergency dentist'], self.outcomeclass['Discharged'],
                                self.outcomeclass['WIC'], self.outcomeclass['MIU'],
                                self.outcomeclass['Call Closed'], self.outcomeclass['Spoke to a primary care service'],
                                self.outcomeclass['OOH'], self.outcomeclass['Seen by A&E doctor'],
                                self.outcomeclass['Out-patient clinic']]
        # print (self.numlist_outcome)
        self.namelist_outcome = ['Admitted', 'Not picked up in an ambulance', 'Emergency dentist', 'Discharged', 'WIC',
                                 'MIU', 'Call Closed', 'Spoke to a primary care service', 'OOH', 'Seen by A&E doctor',
                                 'Out-patient clinic']
        # print (self.outcomeclass)

        self.od_bar = self.od.add_subplot(1, 3, 1)  # bar chart outcome distribution

        self.colorlist_outcome = ['lightblue', 'orange', 'g', 'r', 'purple', 'brown', 'pink', 'gray', 'yellow', 'aqua',
                                  'lightskyblue']
        self.od_bar.bar(range(len(self.numlist_outcome)),
                        self.numlist_outcome,
                        color=self.colorlist_outcome,
                        width=1)
        for a, b in zip(range(len(self.namelist_outcome)), self.numlist_outcome):
            self.od_bar.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=9)
        self.od_bar.set_xlabel('Outcome')
        self.od_bar.set_ylabel('Number')
        plt.title('Bar Chart')

        self.od_pie = self.od.add_subplot(1, 3, 2)  # pir chart outcome distribution
        self.explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1)
        self.od_pie = plt.pie(self.numlist_outcome,
                              # labels=self.namelist_outcome,
                              # labeldistance=1.3,
                              explode=self.explode,
                              pctdistance=1.3,
                              startangle=90,
                              autopct='%.1f%%',
                              # shadow=True,
                              colors=self.colorlist_outcome
                              )
        plt.title('Pie Chart')
        plt.axis('equal')

        self.od_legend = self.od.add_subplot(1, 3, 3)
        self.img = Image.open('OutcomeDistributionLegend.png')
        self.od_legend.axis('off')
        self.od_legend.imshow(self.img)

        plt.suptitle('OVisualization Outcome Distribution (2500 Records from Random Generators)')
        plt.show()

    def Ocostrelation(self):
        self.cr = plt.figure()

        self.outcomeclass = Counter(self.Odata_Outcome)
        self.numlist_outcome = [self.outcomeclass['Admitted'], self.outcomeclass['Not picked up in an ambulance'],
                                self.outcomeclass['Emergency dentist'], self.outcomeclass['Discharged'],
                                self.outcomeclass['WIC'], self.outcomeclass['MIU'],
                                self.outcomeclass['Call Closed'], self.outcomeclass['Spoke to a primary care service'],
                                self.outcomeclass['OOH'], self.outcomeclass['Seen by A&E doctor'],
                                self.outcomeclass['Out-patient clinic']]
        self.namelist_outcome = ['Admitted', 'Not picked up in an ambulance', 'Emergency dentist', 'Discharged', 'WIC',
                                 'MIU', 'Call Closed', 'Spoke to a primary care service', 'OOH', 'Seen by A&E doctor',
                                 'Out-patient clinic']
        self.numlist_cost = np.zeros([11, 1])
        self.avgcost = np.zeros([11, 1])

        for i in range(2500):
            for j in self.namelist_outcome:
                if self.Odata_Outcome[i] == j:
                    self.one_cost = float(self.Odata_Cost[i])
                    # print (self.one_cost)
                    self.namelist_outcomeinnum = self.namelist_outcome.index(j)
                    self.numlist_cost[self.namelist_outcomeinnum] = self.numlist_cost[
                                                                        self.namelist_outcomeinnum] + self.one_cost
        # print (self.numlist_cost)
        for i in range(len(self.namelist_outcome)):
            self.avgcost[i] = self.numlist_cost[i] / self.numlist_outcome[i]
        # print (self.avgcost)
        self.cr_bar = self.cr.add_subplot(1, 4, 1)

        self.colorlist_outcome = ['lightblue', 'orange', 'g', 'r', 'purple', 'brown', 'pink', 'gray', 'yellow', 'aqua',
                                  'lightskyblue']
        for i in range(len(self.namelist_outcome)):
            self.cr_bar.bar(i,
                            self.avgcost[i],
                            color=self.colorlist_outcome[i],
                            width=1)
        for a, b in zip(range(len(self.namelist_outcome)), self.avgcost):
            self.cr_bar.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=9)
        plt.title('Bar Chart')

        self.cr_barlegend = self.cr.add_subplot(1, 4, 2)
        self.img = Image.open('OutcomeDistributionLegend.png')
        self.cr_barlegend.axis('off')
        self.cr_barlegend.imshow(self.img)

        self.cr_box = self.cr.add_subplot(1, 4, 3)

        self.cr_box_array = np.zeros([5, 11])
        self.calculation_list = []
        self.calculated_list = []
        for i in self.namelist_outcome:
            for j in range(2500):
                if self.Odata_Outcome[j] == i:
                    self.calculation_list.append(float(self.Odata_Cost[j]))
            self.calculated_list = np.percentile(self.calculation_list, [0, 25, 50, 75, 100])
            self.calculation_list = []
            for k in range(5):
                self.cr_box_array[k, self.namelist_outcome.index(i)] = self.calculated_list[k]
        # print (self.cr_box_array)
        self.cr_box.boxplot(self.cr_box_array, widths=1)
        for a, b in zip(range(len(self.namelist_outcome)), self.cr_box_array[4, :]):
            self.cr_box.text(a + 1, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=9)

        plt.title('Box-plot')

        self.cr_boxlegend = self.cr.add_subplot(1, 4, 4)
        self.img = Image.open('BoxPlotLegends.png')
        self.cr_boxlegend.axis('off')
        self.cr_boxlegend.imshow(self.img)

        plt.suptitle('OVisualization Average Cost in Different Outcomes (2500 Records from Random Generators)')

        plt.show()

# ov = OVisualization()
# ov.Ocostrelation()
