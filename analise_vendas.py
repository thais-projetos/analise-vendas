import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Criar um DataFrame fictício de vendas
data = {
    'Date': pd.date_range(start='2023-01-01', periods=12, freq='ME'),
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'] * 3,
    'Sales': [150, 200, 300, 100, 160, 220, 310, 130, 180, 250, 320, 140],
    'Region': ['North', 'South', 'East', 'West'] * 3
}

df = pd.DataFrame(data)

# Mostrar as primeiras linhas do dataset
print("Data Preview:")
print(df.head())

# Estatísticas descritivas
print("\nSummary statistics:")
print(df.describe())

# Total de vendas por produto
sales_by_product = df.groupby('Product')['Sales'].sum().reset_index()
print("\nTotal Sales by Product:")
print(sales_by_product)

# Visualização - Vendas por Produto
plt.figure(figsize=(8, 5))
sns.barplot(data=sales_by_product, x='Product', y='Sales')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('sales_by_product.png')
plt.show()

# Vendas por Região
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=sales_by_region, x='Region', y='Sales', palette='magma')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('sales_by_region.png')
plt.show()

# Análise temporal - Vendas por mês
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Date', y='Sales', hue='Product', marker='o')
plt.title('Monthly Sales by Product')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales.png')
plt.show()