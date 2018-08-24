from faker import Faker
import numpy as np
import random


from faker.providers import BaseProvider
class MyProvider(BaseProvider):
    def FakeOutcome(self):
        self.the_number = random.randint(1,100)
        if self.the_number <= 52:
            self.outcome_output = 1 #Admitted
        elif self.the_number >= 53 and self.the_number<= 57:
            self.outcome_output = 2 #Call Closed
        elif self.the_number > 57 and self.the_number<= 64:
            self.outcome_output = 3 #Discharged
        elif self.the_number > 64 and self.the_number<= 68:
            self.outcome_output = 4 #Emergency dentist
        elif self.the_number >68 and self.the_number<= 76:
            self.outcome_output = 5 #MIU
        elif self.the_number >76 and self.the_number<= 81:
            self.outcome_output = 6 #Not picked up in an ambulance
        elif self.the_number >81 and self.the_number<= 82:
            self.outcome_output = 7 #OOH
        elif self.the_number > 82 and self.the_number<= 83:
            self.outcome_output = 8 #Out-patient clinic
        elif self.the_number >83 and self.the_number<= 85:
            self.outcome_output = 9 #Seen by A&E doctor
        elif self.the_number > 85 and self.the_number<= 88:
            self.outcome_output = 10 #Spoke to a primary care service
        else:
            self.outcome_output = 11 #WIC
        #print (self.the_number)
        return self.outcome_output
    def FakeTimeAndCost(self):
        self.outcome_output = MyProvider.FakeOutcome(MyProvider)
        if self.outcome_output == 1:
            self.pathway_time = random.uniform(4.64, 6.64) # average time is 5.64 mins
            self.pathway_cost = random.uniform(539.2, 1139.2) # average cost is 839.2(GBP)
        elif self.outcome_output == 2:
            self.pathway_time = 0
            self.pathway_cost = random.uniform(7.1, 11.1)
        elif self.outcome_output == 3:
            self.pathway_time = random.uniform(3.00, 5.00)
            self.pathway_cost = random.uniform(202.9, 342.9)
        elif self.outcome_output == 4:
            self.pathway_time = 0
            self.pathway_cost = random.uniform(24.1, 84.1)
        elif self.outcome_output == 5:
            self.pathway_time = random.uniform(1.46, 3.46)
            self.pathway_cost = random.uniform(73.0, 193.0)
        elif self.outcome_output == 6:
            self.pathway_time = 0
            self.pathway_cost = random.uniform(24.0, 84.0)
        elif self.outcome_output == 7:
            self.pathway_time = random.uniform(1.29, 3.29)
            self.pathway_cost = random.uniform(121.4, 261.4)
        elif self.outcome_output == 8:
            self.pathway_time = random.uniform(11.80, 13.80)
            self.pathway_cost = random.uniform(346.6, 746.6)
        elif self.outcome_output == 9:
            self.pathway_time = random.uniform(70.20, 72.20)
            self.pathway_cost = random.uniform(301.2, 701.2)
        elif self.outcome_output == 10:
            self.pathway_time = 0
            self.pathway_cost = random.uniform(24.1, 84.1)
        else:
            self.pathway_time = 0.28
            self.pathway_cost = random.uniform(11.8, 15.8)
        return self.outcome_output, round(self.pathway_time, 2), round(self.pathway_cost, 1)

    def Creation(self):

        the_row = 500
        the_column = 3
        FakerData = np.zeros([the_row, the_column])
        for i in range(the_row):
            Outcome, Time, Cost = MyProvider.FakeTimeAndCost(MyProvider)
            one_record = [Outcome, Time, Cost]
            # print (one_record)
            for j in range(the_column):
                FakerData[i][j] = one_record[j]

        np.savetxt('SimulatedData.csv', FakerData, delimiter=',')

fake = Faker()

fake.add_provider(MyProvider) # add this class to Faker

fake.Creation()