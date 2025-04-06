import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('transactions_data.csv',delimiter=',',skip_blank_lines=True)
df.head()
print(df.columns)

df['unusual_time'] = [1,0,1]


weights = {'amount':0.3,
           'account_history':0.1,
           'unusual_location':0.2,
           'unusual_time':0.2
           }

amount_weight = weights['amount']

def normalize(series):
    return (series - series.min()) / (series.max() - series.min())


normalize(df['amount'])
normalize(df['account_history'])

df['normal_account_history'] = normalize(df['account_history'])
df['normal_amount'] = normalize(df['amount'])

print(df['account_type'].unique())

def risk_calculation():

    amount_risk = np.where(
    df['account_type'] == 'High-Value',
    0.1 * df['normal_amount'],              
    weights['amount'] * df['normal_amount'] )

    history_risk = weights['account_history'] * df['normal_account_history']
    time_risk = weights['unusual_time'] * df['unusual_time']
    location_risk = weights['unusual_location'] * df['unusual_location']

    df['total_risk'] = amount_risk + history_risk + time_risk + location_risk
    df['risk'] = df['risk'] = np.where(df['total_risk'] > 0.5, 'High', 'Low')


risk_calculation()

high_risk_df = df[df['risk'] == 'High']


plt.figure(figsize = (10, 6))
sns.barplot(x=df['account_id'], y=df['total_risk'], hue=df['risk'], palette='coolwarm')
plt.title('Total Risk of Sample Transactions')
plt.xlabel('Account ID')
plt.ylabel('Total Risk')
plt.axhline(0.5, color='gray', linestyle='--', label='Risk Threshold')
plt.show()


print(df.head())

###Risk Mitigation Strategies
# 1. If the amount is too high relative to the account type, extra authentication like OTP (One Time Password) should be implemented.
# 2. If the account history is too low, large transactions should not be allowed until the account history improves.
# 3. if the time is unusual i.e at night, the transaction should be blocked.
# 4. If the transaction was at an unusual location, an email can be sent for confirmation. For example, "Is this you?" with the location where the transaction is being taken place included.###
# 5. If anything looks suspicious about the transaction, the transaction should immediaitely be flagged as high risk and should be blocked or kept on hold.




