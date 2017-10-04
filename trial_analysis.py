# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:19:42 2017

@author: ramir
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'Vacuum (mbar)' : (1.0E-5, 1.0E-5, 1.0E-5),
                   'Evaporation Pressure (mbar)' : (0.15,0.15,0.3),
                    'Evaporation time (min)' : (10,18,20),
                   'Al thick (nm)' : (150.,179.,154.),
                    'Junction thick(nm)' : (119.,101.,119.),
                    'Pb thick (nm)' : (202.,202.,202.),
                    'R Pb (Ohm)' : (0,64.,460),
                    'R Al (Ohm)' : (0,9.4,6.0),
                    'Result' : ('Inconclusive. Did not measure chip resistance beforehand',
                                'No superconducting properties',
                                'V vs. I looks like a resistor')
                    },
                    index = np.arange(1,4))

df.to_csv('trial_analysis.csv')