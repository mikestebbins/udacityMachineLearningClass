#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#for each in enron_data:
#    print each
    
count = 0

for each in enron_data:
    if (enron_data[each]["poi"] is True):
        count = count + 1      
#print count

#enron_data['SKILLING JEFFREY K']["total_payments"]
#enron_data['FASTOW ANDREW S']["total_payments"]
#enron_data['LAY KENNETH L']["total_payments"]

print enron_data['LAY KENNETH L']

quantified_salary = 0
email_address = 0

for each in enron_data:
    if (enron_data[each]["email_address"] != 'NaN'):
#        print enron_data[each]["email_address"]
        email_address = email_address + 1
    if (enron_data[each]["salary"] != 'NaN'):
        quantified_salary =  quantified_salary + 1
        
print email_address
print quantified_salary

total_count = 0
no_payments = 0
for each in enron_data:
    total_count = total_count + 1
    if (enron_data[each]["total_payments"] == 'NaN'):
        no_payments = no_payments + 1
        
print "total count:",total_count
print "NaN total payments:",no_payments
        
no_payments = 0
number_of_pois = 0
for each in enron_data:
    if (enron_data[each]["poi"] == True):
        number_of_pois = number_of_pois + 1
        print each
        print enron_data[each]["total_payments"]
        if (enron_data[each]["total_payments"] == 'NaN'):
            no_payments = no_payments + 1
            
print "poi's:",number_of_pois   
print "poi's with NaN total payments:",no_payments
    