import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import seaborn as sns
sns.set()

fileName = '866192035974276_AXIO.csv'
max_fuel_limit = 40
num_packet_to_check = 50
df = pd.read_csv(fileName)
df['created_at'] = pd.to_datetime(df['created_at'])

df2 = df[df.fuel_litre < max_fuel_limit]
df3 = pd.DataFrame({'fuel': df2.fuel_litre,
                    'engine': df2.engine_status,
                    'created_at':df2.created_at,
                    'voltage': df2.voltage})

# plt.plot(df.fuel_litre)
# plt.title('Fuel Data')
# plt.figure()
# plt.plot(df3.fuel)
# plt.title('Corrected Fuel Data')
# df3.head()

fuel = list(df3.fuel)

temp = fuel[0]
num_refill = 0
count = 0
refilled = []
for i,data in enumerate(fuel):
    if data - temp>5:
        count += 1
        if count > num_packet_to_check:
            num_refill += 1
            count = 0
            refilled.append(data-temp)
            print('\n# New Refill #')
            print('Current Fuel: {}'.format(data))
            print('prev Fuel: {}'.format(temp))
            print('Refill amount: {}'.format(data-temp))
            print('DateTime: {}'.format(df3.iloc[i,0]))
            
        else:
            continue
    count = 0
    temp = data

total_refilled = sum(refilled)
initial_fuel = fuel[0]
remaining_fuel = fuel[-1]
total_used = total_refilled - (initial_fuel + remaining_fuel)

print('\n\n###################################-S-U-M-M-A-R-Y-#####################################')
print('\nTotal Number of Refill: {}'.format(num_refill))
print('Total Refill Amount: {}'.format((refilled)))
print('\nTotal Refilled Fuel: {}'.format(total_refilled))
print('Total Used Fuel: {}'.format(total_used))
print('Total Fuel Remaining: {}'.format(remaining_fuel))


plt.plot(df.fuel_litre)
plt.title('Fuel Data')
plt.figure()
plt.plot(df3.fuel)
plt.title('Corrected Fuel Data')
plt.show()
