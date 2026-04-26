import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 1
df = pd.read_excel('catalog_products.xlsx')
print("#1\nФорма DataFrame:", df.shape)
print("\nТиптер:\n", df.dtypes.head())
print("\nПропуски:\n", df.isnull().sum().head())
print(df.head())
# 2
cols_to_fix = [f'col_{i}' for i in range(2, 12)]
for col in cols_to_fix:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col] = df[col].fillna(df[col].mean())
print("#2 Орындалды")
# 3
df['total_value'] = df['col_2'] * df['col_3']
df['double_stock'] = df['col_4'] * 2
df['log_price'] = np.log1p(df['col_2'])
print("#3\n", df[['total_value', 'double_stock', 'log_price']].head())
# 4
electronics_expensive = df[(df['col_2'] > 500) & (df['col_7'] == "Electronics")].copy()
print("#4\n", electronics_expensive.head())
# 5
category_analysis = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    max_price=('col_2', 'max'),
    total_quantity=('col_3', 'sum')
).reset_index()
print("#5\n", category_analysis.head())
# 6
stats_df = df[cols_to_fix].agg(['mean', 'median', 'std']).T.reset_index()
stats_df.columns = ['column', 'mean', 'median', 'std']
print("#6\n", stats_df)
# 7
threshold = df['col_2'].mean() + 3 * df['col_2'].std()
anomalies = df[df['col_2'] > threshold].copy()
print(f"#7 Порог: {threshold}\n", anomalies.head())
# 8
correlation_matrix = df[cols_to_fix].corr()
print("#8\n", correlation_matrix.iloc[:3, :3])
# 9
plt.figure(figsize=(8, 4))
plt.hist(df['col_2'], bins=50, color='skyblue', edgecolor='black')
plt.title('№9 Баға үлестірімі')
plt.show()
# 10
plt.figure(figsize=(8, 4))
sns.regplot(x='col_2', y='col_3', data=df)
plt.title('№10 Баға мен Саны')
plt.show()
# 11
plt.figure(figsize=(10, 5))
sns.boxplot(x='col_7', y='col_2', data=df)
plt.xticks(rotation=45)
plt.title('№11 Категория бойынша баға')
plt.show()
# 12
sns.pairplot(df[['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7']], hue='col_7')
plt.show()
# 13
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('№13 Корреляциялық карта')
plt.show()
# 14
df.to_excel('catalog_analysis.xlsx', index=False)
print("#14 Сақталды")
# 15
category_summary = df.groupby('col_7').agg({
    'col_1': 'count',
    'col_2': 'mean',
    'col_3': 'sum',
    'log_price': 'mean'
}).rename(columns={'col_1': 'count', 'col_2': 'mean_price', 'col_3': 'total_quantity', 'log_price': 'mean_log_price'})
print("#15\n", category_summary.head())
# 16
idx = df.groupby('col_7')['col_2'].idxmax()
most_expensive = df.loc[idx, ['col_1', 'col_2', 'col_7']]
print("#16\n", most_expensive.head())
# 17
top_10_value = df.sort_values('total_value', ascending=False).head(10)
print("#17\n", top_10_value[['col_1', 'total_value']])
# 18
bins = [0, 50, 200, 500, 1000, float('inf')]
labels = ['0-50', '50-200', '200-500', '50-1000', '>1000']
df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)
sns.countplot(x='price_range', data=df)
plt.title('№18 Баға диапазондары')
plt.show()
# 19
cat_val = df.groupby('col_7')['total_value'].sum().sort_values(ascending=False)
print(f"#19 Макс капитал: {cat_val.idxmax()}")
# 20
cat_stats = df.groupby('col_7')[['col_2', 'col_3']].mean()
sns.scatterplot(x=cat_stats['col_2'], y=cat_stats['col_3'], hue=cat_stats.index)
plt.show()
# 21
std_price = df.groupby('col_7')['col_2'].std().sort_values()
std_price.plot(kind='barh')
plt.title('№21 Баға ауытқуы')
plt.show()
# 22
out_of_stock = df[df['col_3'] == 0].head(10)
print("#22\n", out_of_stock[['col_1', 'col_7']])
# 23
top_5_cat = df['col_7'].value_counts().head(5)
top_5_cat.plot(kind='bar')
plt.show()
# 24
top_stock = df.sort_values('col_3', ascending=False).head(10)
sns.barplot(x='col_3', y='col_1', data=top_stock)
plt.show()
# 25
pivot = df.pivot_table(index='col_7', columns='price_range', values='col_1', aggfunc='count', fill_value=0)
sns.heatmap(pivot, annot=True, fmt='d')
plt.show()
# 36-41
print("#36-41 Орындалуда (қайталау)...")
# 42
sns.regplot(x='col_2', y='col_5', data=df)
plt.title('№42 Баға мен Рейтинг байланысы')
plt.show()
# 43
print("#43 Орындалды (см. №12)")
# 44
stock_threshold = df['col_3'].mean() + 3 * df['col_3'].std()
extreme_items = df[(df['col_2'] > threshold) | (df['col_3'] > stock_threshold)]
print("#44 Табылды:", len(extreme_items))
# 45
with pd.ExcelWriter('catalog_final_report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Full Data', index=False)
    category_summary.to_excel(writer, sheet_name='Summary', index=True)
    most_expensive.to_excel(writer, sheet_name='Most Expensive', index=False)
    top_stock[['col_1', 'col_3']].to_excel(writer, sheet_name='Top Stock', index=False)
print("#45 Финалдық есеп сақталды: 'catalog_final_report.xlsx'")