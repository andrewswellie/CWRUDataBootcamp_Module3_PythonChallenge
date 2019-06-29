# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:09:38 2019

@author: andre
"""

#import os
#import csv
#
#us_state_abbrev = {
#    'Alabama': 'AL',
#    'Alaska': 'AK',
#    'Arizona': 'AZ',
#    'Arkansas': 'AR',
#    'California': 'CA',
#    'Colorado': 'CO',
#    'Connecticut': 'CT',
#    'Delaware': 'DE',
#    'Florida': 'FL',
#    'Georgia': 'GA',
#    'Hawaii': 'HI',
#    'Idaho': 'ID',
#    'Illinois': 'IL',
#    'Indiana': 'IN',
#    'Iowa': 'IA',
#    'Kansas': 'KS',
#    'Kentucky': 'KY',
#    'Louisiana': 'LA',
#    'Maine': 'ME',
#    'Maryland': 'MD',
#    'Massachusetts': 'MA',
#    'Michigan': 'MI',
#    'Minnesota': 'MN',
#    'Mississippi': 'MS',
#    'Missouri': 'MO',
#    'Montana': 'MT',
#    'Nebraska': 'NE',
#    'Nevada': 'NV',
#    'New Hampshire': 'NH',
#    'New Jersey': 'NJ',
#    'New Mexico': 'NM',
#    'New York': 'NY',
#    'North Carolina': 'NC',
#    'North Dakota': 'ND',
#    'Ohio': 'OH',
#    'Oklahoma': 'OK',
#    'Oregon': 'OR',
#    'Pennsylvania': 'PA',
#    'Rhode Island': 'RI',
#    'South Carolina': 'SC',
#    'South Dakota': 'SD',
#    'Tennessee': 'TN',
#    'Texas': 'TX',
#    'Utah': 'UT',
#    'Vermont': 'VT',
#    'Virginia': 'VA',
#    'Washington': 'WA',
#    'West Virginia': 'WV',
#    'Wisconsin': 'WI',
#    'Wyoming': 'WY',
#}
## Credit for this state list goes to 
## afhaque at https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
#
#resource_files = os.listdir('Resources')
#
#for f in resource_files:
#    emp_ID=list()
#    name=list()
#    dob=list()
#    ssn=list()
#    state=list()
#    with open(os.path.join('Resources',f),'r') as data:
#        csvdata = csv.reader(data)
#        next(csvdata)
#        for line in csvdata:
#            emp_ID.append(line[0])
#            name.append(line[1])
#            dob.append(line[2])
#            ssn.append(line[3])
#            state.append(line[4])
#    output_lines = list()
#    with open('output_'+f.split('.')[0]+'.csv','w',newline='') as data:
#        output_writer = csv.writer(data, delimiter=',')
#        output_writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
#        for x in range(len(emp_ID)):
#            dob_new=dob[x].split('-')[1]+'/'+dob[x].split('-')[2]+'/'+dob[x].split('-')[0]
#            ssn_new='****-**-'+ssn[x].split('-')[2]
#            output_writer.writerow([str(emp_ID[x]),name[x].split(' ')[0],name[x].split(' ')[1],dob_new,ssn_new,us_state_abbrev[state[x]]])
    
