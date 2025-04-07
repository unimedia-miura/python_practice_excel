import pandas as pd

df = pd.read_excel('sample.xlsx', engine='openpyxl')

df['Total Sales'] = df['Price'] * df['Count']

df['Tax'] = df['Price'] * df['Count'] * 0.1

total_sales = (df['Price']*df['Count']).sum()
print(f"Total Sales: {total_sales}")
df.loc['Total'] = df.sum(numeric_only=True)

df.to_excel('caluculated_data.xlsx')

print("Data caluculation is done and saved to caluculated_data.xlsx")