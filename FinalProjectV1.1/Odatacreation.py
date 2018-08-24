import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random


class Odatacreation():

    def NRandomGenerator(self):
        self.num_cost = 0
        self.num_gender = random.uniform(0, 100)
        if self.num_gender < 46.57:
            self.class_gender = 'Female'  # female
        else:
            self.class_gender = 'Male'  # male
        # print (self.class_gender,self.num_gender)

        self.num_age = random.uniform(0, 100)
        if self.num_age < 9.32:
            self.class_age = '0~4'
        elif 9.32 <= self.num_age < 21.78:
            self.class_age = '5~19'
        elif 21.78 <= self.num_age < 75.49:
            self.class_age = '20~64'
        else:
            self.class_age = '65+'
        # print(self.class_age, self.num_age)

        self.num_condition = random.uniform(0, 100)
        if self.num_condition < 53.57:
            self.class_condition = 'Unknown'
        elif 53.57 <= self.num_condition < 60.20:
            self.class_condition = 'Central Nervous System conditions'
        elif 60.20 <= self.num_condition < 69.94:
            self.class_condition = 'Dislocation/fracture/joint injury/amputation'
        elif 69.94 <= self.num_condition < 79.51:
            self.class_condition = 'Respiratory conditions'
        elif 79.51 <= self.num_condition < 84.25:
            self.class_condition = 'Falls'
        elif 84.25 <= self.num_condition < 90.80:
            self.class_condition = 'Cardiac conditions'
        elif 90.80 <= self.num_condition < 95.64:
            self.class_condition = 'Collapse'
        else:
            self.class_condition = 'Gastrointestinal conditions'
        # print(self.class_condition, self.num_condition)

        self.provider = random.uniform(0, 100)
        if self.provider < 50:  # Call a provider
            self.callnum = random.uniform(0, 100)
            if self.callnum < 50:  # Call 999
                self.num_cost += 7
                self.situationassessed = random.uniform(0, 100)  # Situation assessed
                if self.class_condition == 'Unknown':  # Unknown
                    if self.situationassessed < 17.34:  # Not LT
                        self.class_outcome = 'Not picked up in an ambulance'
                        self.num_cost += 47
                    else:  # LT
                        self.num_cost += 230  # Picked up in an ambulance
                        self.num_cost += 317  # A&E
                        self.num_cost += 86  # Assessed - to see if it is an A&E situation
                        self.aesituation = random.uniform(0, 100)
                        if self.aesituation < 83.92:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 96.05:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 87.84:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 87.84 <= self.disoporpc < 92.96:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 21.3:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 21.3 <= self.wicmiuorooh < 78.6:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'

                elif self.class_condition == 'Central Nervous System conditions':  # Other conditions
                    if self.situationassessed < 22.22:  # Not LT
                        self.class_outcome = 'Not picked up in an ambulance'
                        self.num_cost += 47
                    else:  # LT
                        self.num_cost += 230  # Picked up in an ambulance
                        self.num_cost += 317  # A&E
                        self.num_cost += 86  # Assessed - to see if it is an A&E situation
                        self.aesituation = random.uniform(0, 100)
                        if self.aesituation < 93.43:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 99.9:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 91.44:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 91.44 <= self.disoporpc < 98.77:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 46.75:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 46.75 <= self.wicmiuorooh < 53.25:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                elif self.class_condition == 'Dislocation/fracture/joint injury/amputation':
                    if self.situationassessed < 50:  # Not LT
                        self.class_outcome = 'Not picked up in an ambulance'
                        self.num_cost += 47
                    else:  # LT
                        self.num_cost += 230  # Picked up in an ambulance
                        self.num_cost += 317  # A&E
                        self.num_cost += 86  # Assessed - to see if it is an A&E situation
                        self.aesituation = random.uniform(0, 100)
                        if self.aesituation < 46.4:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 93.16:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 39.34:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 39.34 <= self.disoporpc < 49.24:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 1.37:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 1.37 <= self.wicmiuorooh < 98.63:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                elif self.class_condition == 'Respiratory conditions':
                    if self.situationassessed < 18.06:  # Not LT
                        self.class_outcome = 'Not picked up in an ambulance'
                        self.num_cost += 47
                    else:  # LT
                        self.num_cost += 230  # Picked up in an ambulance
                        self.num_cost += 317  # A&E
                        self.num_cost += 86  # Assessed - to see if it is an A&E situation
                        self.aesituation = random.uniform(0, 100)
                        if self.aesituation < 98.34:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 99.78:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 97.67:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 97.67 <= self.disoporpc < 99.46:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 45.45:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 45.45 <= self.wicmiuorooh < 54.54:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                elif self.class_condition == 'Falls':
                    if self.situationassessed < 29.9:  # Not LT
                        self.class_outcome = 'Not picked up in an ambulance'
                        self.num_cost += 47
                    else:  # LT
                        self.num_cost += 230  # Picked up in an ambulance
                        self.num_cost += 317  # A&E
                        self.num_cost += 86  # Assessed - to see if it is an A&E situation
                        self.aesituation = random.uniform(0, 100)
                        if self.aesituation < 50:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 50:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 33.33:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 33.33 <= self.disoporpc < 66.66:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 33.33:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 33.33 <= self.wicmiuorooh < 66.66:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                elif self.class_condition == 'Cardiac conditions':
                    if self.situationassessed < 22.79:  # Not LT
                        self.class_outcome = 'Not picked up in an ambulance'
                        self.num_cost += 47
                    else:  # LT
                        self.num_cost += 230  # Picked up in an ambulance
                        self.num_cost += 317  # A&E
                        self.num_cost += 86  # Assessed - to see if it is an A&E situation
                        self.aesituation = random.uniform(0, 100)
                        if self.aesituation < 96.33:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 99.74:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 94.96:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 94.96 <= self.disoporpc < 98.91:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 48.17:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 48.17 <= self.wicmiuorooh < 51.84:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                elif self.class_condition == 'Collapse':
                    if self.situationassessed < 28.84:  # Not LT
                        self.class_outcome = 'Not picked up in an ambulance'
                        self.num_cost += 47
                    else:  # LT
                        self.num_cost += 230  # Picked up in an ambulance
                        self.num_cost += 317  # A&E
                        self.num_cost += 86  # Assessed - to see if it is an A&E situation
                        self.aesituation = random.uniform(0, 100)
                        if self.aesituation < 50:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 50:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 33.33:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 33.33 <= self.disoporpc < 66.66:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 33.33:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 33.33 <= self.wicmiuorooh < 66.66:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                else:  # Gastrointestinal conditions
                    if self.situationassessed < 58.7:  # Not LT
                        self.class_outcome = 'Not picked up in an ambulance'
                        self.num_cost += 47
                    else:  # LT
                        self.num_cost += 230  # Picked up in an ambulance
                        self.num_cost += 317  # A&E
                        self.num_cost += 86  # Assessed - to see if it is an A&E situation
                        self.aesituation = random.uniform(0, 100)
                        if self.aesituation < 96.93:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 99.89:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 97.06:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 97.06 <= self.disoporpc < 99.15:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 47.62:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 47.62 <= self.wicmiuorooh < 52.38:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'



            else:  # Call 111
                self.num_cost += 9.13
                self.directedtoservice = random.uniform(0, 100)
                if self.directedtoservice < 20:  # Ambulance requested by 111
                    self.num_cost += 20
                    self.num_cost += 317
                    self.num_cost += 86
                    self.aesituation = random.uniform(0, 100)
                    if self.class_condition == 'Unknown':
                        if self.aesituation < 83.92:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 96.05:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 87.84:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 87.84 <= self.disoporpc < 92.96:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 21.3:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 21.3 <= self.wicmiuorooh < 78.6:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    elif self.class_condition == 'Central Nervous System conditions':  # Other conditions
                        if self.aesituation < 93.43:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 99.9:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 91.44:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 91.44 <= self.disoporpc < 98.77:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 46.75:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 46.75 <= self.wicmiuorooh < 53.25:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    elif self.class_condition == 'Dislocation/fracture/joint injury/amputation':  # Other conditions
                        if self.aesituation < 46.4:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 93.16:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 39.34:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 39.34 <= self.disoporpc < 49.24:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 1.37:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 1.37 <= self.wicmiuorooh < 98.63:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    elif self.class_condition == 'Respiratory conditions':  # Other conditions
                        if self.aesituation < 98.34:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 99.78:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 97.67:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 97.67 <= self.disoporpc < 99.46:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 45.45:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 45.45 <= self.wicmiuorooh < 54.54:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    elif self.class_condition == 'Falls':  # Other conditions
                        if self.aesituation < 50:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 50:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 33.33:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 33.33 <= self.disoporpc < 66.66:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 33.33:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 33.33 <= self.wicmiuorooh < 66.66:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    elif self.class_condition == 'Cardiac conditions':  # Other conditions
                        if self.aesituation < 96.33:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 99.74:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 94.96:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 94.96 <= self.disoporpc < 98.91:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 48.17:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 48.17 <= self.wicmiuorooh < 51.84:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    elif self.class_condition == 'Collapse':  # Other conditions
                        if self.aesituation < 50:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 50:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 33.33:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 33.33 <= self.disoporpc < 66.66:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 33.33:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 33.33 <= self.wicmiuorooh < 66.66:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    else:  # Gastrointestinal conditions
                        if self.aesituation < 96.93:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 99.89:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 97.06:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 97.06 <= self.disoporpc < 99.15:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 47.62:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 47.62 <= self.wicmiuorooh < 52.38:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'


                elif 20 <= self.directedtoservice < 40:  # Recommend to attend A&E
                    self.num_cost += 87
                    self.num_cost += 86
                    self.aesituation = random.uniform(0, 100)
                    if self.class_condition == 'Unknown':  # Unknown
                        if self.aesituation < 83.92:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 96.05:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 87.84:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 87.84 <= self.disoporpc < 92.96:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 21.3:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 21.3 <= self.wicmiuorooh < 78.6:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    elif self.class_condition == 'Central Nervous System conditions':  # Other conditions
                        if self.aesituation < 93.43:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 99.9:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 91.44:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 91.44 <= self.disoporpc < 98.77:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 46.75:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 46.75 <= self.wicmiuorooh < 53.25:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    elif self.class_condition == 'Dislocation/fracture/joint injury/amputation':  # Other conditions
                        if self.aesituation < 46.4:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 93.16:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 39.34:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 39.34 <= self.disoporpc < 49.24:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 1.37:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 1.37 <= self.wicmiuorooh < 98.63:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    elif self.class_condition == 'Respiratory conditions':
                        if self.aesituation < 98.34:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 99.78:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 97.67:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 97.67 <= self.disoporpc < 99.46:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 45.45:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 45.45 <= self.wicmiuorooh < 54.54:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    elif self.class_condition == 'Falls':
                        if self.aesituation < 50:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 50:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 33.33:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 33.33 <= self.disoporpc < 66.66:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 33.33:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 33.33 <= self.wicmiuorooh < 66.66:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    elif self.class_condition == 'Cardiac conditions':
                        if self.aesituation < 96.33:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 99.74:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 94.96:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 94.96 <= self.disoporpc < 98.91:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 48.17:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 48.17 <= self.wicmiuorooh < 51.84:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    elif self.class_condition == 'Collapse':
                        if self.aesituation < 50:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 50:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 33.33:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 33.33 <= self.disoporpc < 66.66:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 33.33:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 33.33 <= self.wicmiuorooh < 66.66:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'
                    else:  # Gastrointestinal conditions
                        if self.aesituation < 96.93:  # A&E situation
                            self.suorae = random.uniform(0, 100)
                            if self.suorae < 99.89:  # SU
                                self.num_cost += 520
                                self.class_outcome = 'Admitted'
                            else:  # AE
                                self.num_cost += 41
                                self.class_outcome = 'Seen by A&E doctor'
                        else:  # Not A&E situation
                            self.disoporpc = random.uniform(0, 100)
                            if self.disoporpc < 97.06:  # Discharged
                                self.class_outcome = 'Discharged'
                            elif 97.06 <= self.disoporpc < 99.15:  # Out-patient clinic
                                self.class_outcome = 'Out-patient clinic'
                            else:  # PC
                                self.wicmiuorooh = random.uniform(0, 100)
                                if self.wicmiuorooh < 47.62:  # WIC
                                    self.class_outcome = 'WIC'
                                elif 47.62 <= self.wicmiuorooh < 52.38:  # MIU
                                    self.class_outcome = 'MIU'
                                else:  # OOH
                                    self.class_outcome = 'OOH'




                elif 40 <= self.directedtoservice < 60:  # Not directed to a service
                    self.class_outcome = 'Call Closed'

                else:  # Recommend to attend primary and community care
                    self.num_cost += 45
                    self.priandcomcare = random.uniform(0, 100)
                    if self.priandcomcare < 33.33:  # Spoke to a primary care service
                        self.class_outcome = 'Spoke to a primary care service'
                    elif 33.33 <= self.priandcomcare < 66.66:  # Emergency dentist
                        self.class_outcome = 'Emergency dentist'
                    else:  # Contact a primary service
                        if self.class_condition == 'Unknown':  # Unknown
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 21.3:  # WIC
                                self.class_outcome = 'WIC'
                            elif 21.3 <= self.wicmiuorooh < 78.6:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'


                        elif self.class_condition == 'Central Nervous System conditions':  # Other conditions
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 46.75:  # WIC
                                self.class_outcome = 'WIC'
                            elif 46.75 <= self.wicmiuorooh < 53.25:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                        elif self.class_condition == 'Dislocation/fracture/joint injury/amputation':
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 1.37:  # WIC
                                self.class_outcome = 'WIC'
                            elif 1.37 <= self.wicmiuorooh < 98.63:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                        elif self.class_condition == 'Respiratory conditions':
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 45.45:  # WIC
                                self.class_outcome = 'WIC'
                            elif 45.45 <= self.wicmiuorooh < 54.54:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                        elif self.class_condition == 'Falls':
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 33.33:  # WIC
                                self.class_outcome = 'WIC'
                            elif 33.33 <= self.wicmiuorooh < 66.66:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                        elif self.class_condition == 'Cardiac conditions':
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 48.17:  # WIC
                                self.class_outcome = 'WIC'
                            elif 48.17 <= self.wicmiuorooh < 51.84:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                        elif self.class_condition == 'Collapse':
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 33.33:  # WIC
                                self.class_outcome = 'WIC'
                            elif 33.33 <= self.wicmiuorooh < 66.66:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                        else:  # Gastrointestinal conditions
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 47.62:  # WIC
                                self.class_outcome = 'WIC'
                            elif 47.62 <= self.wicmiuorooh < 52.38:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'





        else:  # Attend a provider
            if self.class_condition == 'Unknown':  # Unknown
                self.srmicormiu = random.uniform(0, 100)
                if self.srmicormiu < 91.7:  # Self referral to A&E
                    self.num_cost += 87
                    self.num_cost += 86
                    self.aesituation = random.uniform(0, 100)
                    if self.aesituation < 83.92:  # Yes A&E situation
                        self.suorae = random.uniform(0, 100)
                        if self.suorae < 96.05:  # SU
                            self.num_cost += 520
                            self.class_outcome = 'Admitted'
                        else:  # AE
                            self.num_cost += 41
                            self.class_outcome = 'Seen by A&E doctor'
                    else:  # Not A&E situation
                        self.disoporpc = random.uniform(0, 100)
                        if self.disoporpc < 87.84:  # Discharged
                            self.class_outcome = 'Discharged'
                        elif 87.84 <= self.disoporpc < 92.96:  # Out-patient clinic
                            self.class_outcome = 'Out-patient clinic'
                        else:  # PC
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 21.3:  # WIC
                                self.class_outcome = 'WIC'
                            elif 21.3 <= self.wicmiuorooh < 78.6:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                elif 91.7 <= self.srmicormiu < 95.4:  # WIC
                    self.class_outcome = 'WIC'
                else:  # MIU
                    self.class_outcome = 'MIU'

            elif self.class_condition == 'Central Nervous System conditions':  # Other conditions
                self.srmicormiu = random.uniform(0, 100)
                if self.srmicormiu < 70.43:  # Self referral to A&E
                    self.num_cost += 87
                    self.num_cost += 86
                    self.aesituation = random.uniform(0, 100)
                    if self.aesituation < 93.43:  # Yes A&E situation
                        self.suorae = random.uniform(0, 100)
                        if self.suorae < 99.9:  # SU
                            self.num_cost += 520
                            self.class_outcome = 'Admitted'
                        else:  # AE
                            self.num_cost += 41
                            self.class_outcome = 'Seen by A&E doctor'
                    else:  # Not A&E situation
                        self.disoporpc = random.uniform(0, 100)
                        if self.disoporpc < 91.44:  # Discharged
                            self.class_outcome = 'Discharged'
                        elif 91.44 <= self.disoporpc < 98.77:  # Out-patient clinic
                            self.class_outcome = 'Out-patient clinic'
                        else:  # PC
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 46.75:  # WIC
                                self.class_outcome = 'WIC'
                            elif 46.75 <= self.wicmiuorooh < 53.25:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                elif 70.43 <= self.srmicormiu < 99.89:  # WIC
                    self.class_outcome = 'WIC'
                else:  # MIU
                    self.class_outcome = 'MIU'
            elif self.class_condition == 'Dislocation/fracture/joint injury/amputation':  # Other conditions
                self.srmicormiu = random.uniform(0, 100)
                if self.srmicormiu < 40.45:  # Self referral to A&E
                    self.num_cost += 87
                    self.num_cost += 86
                    self.aesituation = random.uniform(0, 100)
                    if self.aesituation < 46.4:  # Yes A&E situation
                        self.suorae = random.uniform(0, 100)
                        if self.suorae < 93.16:  # SU
                            self.num_cost += 520
                            self.class_outcome = 'Admitted'
                        else:  # AE
                            self.num_cost += 41
                            self.class_outcome = 'Seen by A&E doctor'
                    else:  # Not A&E situation
                        self.disoporpc = random.uniform(0, 100)
                        if self.disoporpc < 39.34:  # Discharged
                            self.class_outcome = 'Discharged'
                        elif 39.34 <= self.disoporpc < 49.24:  # Out-patient clinic
                            self.class_outcome = 'Out-patient clinic'
                        else:  # PC
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 1.37:  # WIC
                                self.class_outcome = 'WIC'
                            elif 1.37 <= self.wicmiuorooh < 98.63:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                elif 40.45 <= self.srmicormiu < 48.9:  # WIC
                    self.class_outcome = 'WIC'
                else:  # MIU
                    self.class_outcome = 'MIU'
            elif self.class_condition == 'Respiratory conditions':  # Other conditions
                self.srmicormiu = random.uniform(0, 100)
                if self.srmicormiu < 80.47:  # Self referral to A&E
                    self.num_cost += 87
                    self.num_cost += 86
                    self.aesituation = random.uniform(0, 100)
                    if self.aesituation < 98.34:  # Yes A&E situation
                        self.suorae = random.uniform(0, 100)
                        if self.suorae < 99.78:  # SU
                            self.num_cost += 520
                            self.class_outcome = 'Admitted'
                        else:  # AE
                            self.num_cost += 41
                            self.class_outcome = 'Seen by A&E doctor'
                    else:  # Not A&E situation
                        self.disoporpc = random.uniform(0, 100)
                        if self.disoporpc < 97.67:  # Discharged
                            self.class_outcome = 'Discharged'
                        elif 97.67 <= self.disoporpc < 99.46:  # Out-patient clinic
                            self.class_outcome = 'Out-patient clinic'
                        else:  # PC
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 45.45:  # WIC
                                self.class_outcome = 'WIC'
                            elif 45.45 <= self.wicmiuorooh < 54.54:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                elif 80.47 <= self.srmicormiu < 99.7:  # WIC
                    self.class_outcome = 'WIC'
                else:  # MIU
                    self.class_outcome = 'MIU'
            elif self.class_condition == 'Falls':  # Other conditions
                self.srmicormiu = random.uniform(0, 100)
                if self.srmicormiu == 0:  # Self referral to A&E
                    self.num_cost += 87
                    self.num_cost += 86
                    self.aesituation = random.uniform(0, 100)
                    if self.aesituation < 50:  # Yes A&E situation
                        self.suorae = random.uniform(0, 100)
                        if self.suorae < 50:  # SU
                            self.num_cost += 520
                            self.class_outcome = 'Admitted'
                        else:  # AE
                            self.num_cost += 41
                            self.class_outcome = 'Seen by A&E doctor'
                    else:  # Not A&E situation
                        self.disoporpc = random.uniform(0, 100)
                        if self.disoporpc < 33.33:  # Discharged
                            self.class_outcome = 'Discharged'
                        elif 33.33 <= self.disoporpc < 66.66:  # Out-patient clinic
                            self.class_outcome = 'Out-patient clinic'
                        else:  # PC
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 33.33:  # WIC
                                self.class_outcome = 'WIC'
                            elif 33.33 <= self.wicmiuorooh < 66.66:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                elif 0 <= self.srmicormiu < 99.92:  # WIC
                    self.class_outcome = 'WIC'
                else:  # MIU
                    self.class_outcome = 'MIU'
            elif self.class_condition == 'Cardiac conditions':  # Other conditions
                self.srmicormiu = random.uniform(0, 100)
                if self.srmicormiu < 62.23:  # Self referral to A&E
                    self.num_cost += 87
                    self.num_cost += 86
                    self.aesituation = random.uniform(0, 100)
                    if self.aesituation < 96.33:  # Yes A&E situation
                        self.suorae = random.uniform(0, 100)
                        if self.suorae < 99.74:  # SU
                            self.num_cost += 520
                            self.class_outcome = 'Admitted'
                        else:  # AE
                            self.num_cost += 41
                            self.class_outcome = 'Seen by A&E doctor'
                    else:  # Not A&E situation
                        self.disoporpc = random.uniform(0, 100)
                        if self.disoporpc < 94.96:  # Discharged
                            self.class_outcome = 'Discharged'
                        elif 94.96 <= self.disoporpc < 98.91:  # Out-patient clinic
                            self.class_outcome = 'Out-patient clinic'
                        else:  # PC
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 48.17:  # WIC
                                self.class_outcome = 'WIC'
                            elif 48.17 <= self.wicmiuorooh < 51.84:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                elif 62.23 <= self.srmicormiu < 99.85:  # WIC
                    self.class_outcome = 'WIC'
                else:  # MIU
                    self.class_outcome = 'MIU'
            elif self.class_condition == 'Collapse':  # Other conditions
                self.srmicormiu = random.uniform(0, 100)
                if self.srmicormiu == 0:  # Self referral to A&E
                    self.num_cost += 87
                    self.num_cost += 86
                    self.aesituation = random.uniform(0, 100)
                    if self.aesituation < 50:  # Yes A&E situation
                        self.suorae = random.uniform(0, 100)
                        if self.suorae < 50:  # SU
                            self.num_cost += 520
                            self.class_outcome = 'Admitted'
                        else:  # AE
                            self.num_cost += 41
                            self.class_outcome = 'Seen by A&E doctor'
                    else:  # Not A&E situation
                        self.disoporpc = random.uniform(0, 100)
                        if self.disoporpc < 33.33:  # Discharged
                            self.class_outcome = 'Discharged'
                        elif 33.33 <= self.disoporpc < 66.66:  # Out-patient clinic
                            self.class_outcome = 'Out-patient clinic'
                        else:  # PC
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 33.33:  # WIC
                                self.class_outcome = 'WIC'
                            elif 33.33 <= self.wicmiuorooh < 66.66:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                elif 0 <= self.srmicormiu < 99.84:  # WIC
                    self.class_outcome = 'WIC'
                else:  # MIU
                    self.class_outcome = 'MIU'
            else:  # Gastrointestinal conditions
                self.srmicormiu = random.uniform(0, 100)
                if self.srmicormiu < 85.49:  # Self referral to A&E
                    self.num_cost += 87
                    self.num_cost += 86
                    self.aesituation = random.uniform(0, 100)
                    if self.aesituation < 96.93:  # Yes A&E situation
                        self.suorae = random.uniform(0, 100)
                        if self.suorae < 99.89:  # SU
                            self.num_cost += 520
                            self.class_outcome = 'Admitted'
                        else:  # AE
                            self.num_cost += 41
                            self.class_outcome = 'Seen by A&E doctor'
                    else:  # Not A&E situation
                        self.disoporpc = random.uniform(0, 100)
                        if self.disoporpc < 97.06:  # Discharged
                            self.class_outcome = 'Discharged'
                        elif 97.06 <= self.disoporpc < 99.15:  # Out-patient clinic
                            self.class_outcome = 'Out-patient clinic'
                        else:  # PC
                            self.wicmiuorooh = random.uniform(0, 100)
                            if self.wicmiuorooh < 47.62:  # WIC
                                self.class_outcome = 'WIC'
                            elif 47.62 <= self.wicmiuorooh < 52.38:  # MIU
                                self.class_outcome = 'MIU'
                            else:  # OOH
                                self.class_outcome = 'OOH'
                elif 85.49 <= self.srmicormiu < 99.95:  # WIC
                    self.class_outcome = 'WIC'
                else:  # MIU
                    self.class_outcome = 'MIU'
        return (self.class_gender, self.class_age, self.class_condition, self.class_outcome, self.num_cost)

    def creation(self):
        self.Odata_row = 2500
        self.Odata_column = 5
        self.Odata = np.zeros([self.Odata_row, self.Odata_column], dtype=object)
        for i in range(self.Odata_row):
            self.Odata_Gender, self.Odata_Age, self.Odata_Condition, self.Odata_Outcome, self.Odata_Cost = Odatacreation.NRandomGenerator(
                Odatacreation)
            self.Odata_onerecord = [self.Odata_Gender, self.Odata_Age, self.Odata_Condition, self.Odata_Outcome,
                                    self.Odata_Cost]
            # print (np.dtype(self.Odata_Gender))
            for j in range(self.Odata_column):
                self.Odata[i][j] = self.Odata_onerecord[j]
        # print (self.Odata)
        np.savetxt('NRandomGeneratorData.csv', self.Odata, delimiter=',', fmt='%s,%s,%s,%s,%s')


od = Odatacreation()
od.creation()
