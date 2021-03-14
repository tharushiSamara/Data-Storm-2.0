import pandas as pd
import numpy as np
import math 

test = pd.read_csv('F:\Data Storm 2.0\Dataset\Hotel-A-test.csv')
test = pd.read_csv('F:\Data Storm 2.0\Dataset\Hotel-A-test.csv')
predict = pd.read_csv('F:\Data Storm 2.0\Submission_3.csv')
#print(test.head())

test['res_state'] = predict['Reservation_Status']
test['Expected_checkin'] = pd.to_datetime(test['Expected_checkin'])
test['Expected_checkout'] = pd.to_datetime(test['Expected_checkout'])

test['staying_days'] = (test['Expected_checkout']-test['Expected_checkin']).dt.days
#print(test['staying_days'].head())

test['Dependants_without_babies']= test['Adults']+test['Children']
#print(test['Dependants_without_babies'].head())

test['after_discount'] = test['Room_Rate'] - ((test['Room_Rate'] * test['Discount_Rate'])/100)
#print(test['after_discount'].head())
test['Total_revenue'] = test['after_discount'] * (test['staying_days'] * (test['Dependants_without_babies']/5))
#print(test['Total_revenue'].head())

Total = test['Total_revenue'].sum()
print('Expected Revenue is all travelers checked -in ',Total)

Net_revenue = 0
#loss = test.loc[test['Reservation_Status'] == 'Canceled' or test['Reservation_Status'] == 'No-Show']
for ind in test.index:
    if test['res_state'][ind] ==  1:
        Net_revenue = Net_revenue + (test['after_discount'][ind] * (test['staying_days'][ind] * (test['Dependants_without_babies'][ind]/5)))
        
 
#print(test['loss'].head())
#Reduced_Total = test['loss'].sum()

#print(Reduced_Total) 
loss = Total - Net_revenue
print("loss is: ",loss)
