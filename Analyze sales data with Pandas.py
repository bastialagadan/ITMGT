{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "251576ff-6c9b-473c-9b5e-fc773429d35c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sales Data Analysis\n",
    "\n",
    "This notebook analyzes sales data using the provided Invoices and Customers datasets. It answers easy, medium, and hard-level questions using data analysis and visualization techniques.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b8fb1579-7326-41e7-9ac1-b766b8435639",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(  invoice_no  customer_id  category  quantity    price payment_method  \\\n",
       " 0    I138884          229  Clothing         5  1500.40    Credit Card   \n",
       " 1    I317333         3433     Shoes         3  1800.51     Debit Card   \n",
       " 2    I127801          644  Clothing         1   300.08           Cash   \n",
       " 3    I173702         4900     Shoes         5  3000.85    Credit Card   \n",
       " 4    I337046         1089     Books         4    60.60           Cash   \n",
       " \n",
       "   invoice_date   shopping_mall  \n",
       " 0     5/8/2022          Kanyon  \n",
       " 1   12/12/2021  Forum Istanbul  \n",
       " 2    9/11/2021       Metrocity  \n",
       " 3   16/05/2021    Metropol AVM  \n",
       " 4   24/10/2021          Kanyon  ,\n",
       "     age first_name gender  id last_name\n",
       " 0  48.0   Nicholas      M   0    Flores\n",
       " 1   NaN    Jeffery      M   1      Rowe\n",
       " 2  57.0     Alexis      F   2    Benton\n",
       " 3  73.0        Amy      F   3   Johnson\n",
       " 4  20.0      David      M   4     Moore)"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "invoices = pd.read_csv(\"/Users/andresebastianramosalagadan/Downloads/fct_invoice.csv\")\n",
    "customers = pd.read_json(\"/Users/andresebastianramosalagadan/Downloads/dim_customer.json\")\n",
    "\n",
    "invoices.head(), customers.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "49ed0463-96bf-454b-a779-28bc722d3ad6",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "### Easy Q1: How many unique customers are in the dataset?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "d3b09724-910b-4856-92dc-ae710c3176e3",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['age', 'first_name', 'gender', 'id', 'last_name'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(customers.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "f0f0a005-e2b7-476d-816b-00376dea2515",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unique customers: 5191\n"
     ]
    }
   ],
   "source": [
    "unique_customers = customers['id'].nunique()\n",
    "print(\"Unique customers:\", unique_customers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "05aa8112-dc47-438b-8c9b-379b576a8a59",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "### Easy Q2: Product categories and number of unique categories"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "5dea2cdf-b948-4645-8e69-8eab8ae4ae4c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Categories: ['Clothing' 'Shoes' 'Books' 'Cosmetics' 'Food & Beverage' 'Toys'\n",
      " 'Technology' 'Souvenir']\n",
      "Number of unique categories: 8\n"
     ]
    }
   ],
   "source": [
    "categories = invoices['category'].unique()\n",
    "num_categories = invoices['category'].nunique()\n",
    "print(\"Categories:\", categories)\n",
    "print(\"Number of unique categories:\", num_categories)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "865dd3b5-1cfb-491a-a3ad-d16e5922971a",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "### Easy Q3: Most popular payment method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "846cb7b2-deb3-417b-9122-1e0f63468402",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Most used payment method: Cash\n",
      "Used 44447 times\n"
     ]
    }
   ],
   "source": [
    "payment_counts = invoices['payment_method'].value_counts()\n",
    "most_used_method = payment_counts.idxmax()\n",
    "most_used_count = payment_counts.max()\n",
    "print(\"Most used payment method:\", most_used_method)\n",
    "print(\"Used\", most_used_count, \"times\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "f71c6ec3-2ed4-4b24-b271-e4257bb21628",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "### Medium Q1: Three most popular categories by total sales"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "f7b76483-9e65-4c70-b76a-1d1eb470b1d2",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['invoice_no', 'customer_id', 'category', 'quantity', 'price',\n",
       "       'payment_method', 'invoice_date', 'shopping_mall'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "invoices.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "a53aa9d9-5c56-41bf-8332-0b7b1f5c6bf1",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "invoices['total'] = invoices['quantity'] * invoices['price']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "8aeeabed-257f-4064-8cca-137cf8145e49",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "category\n",
       "Clothing      1.139968e+08\n",
       "Shoes         6.655345e+07\n",
       "Technology    5.786235e+07\n",
       "Name: total, dtype: float64"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_categories = invoices.groupby('category')['total'].sum().sort_values(ascending=False).head(3)\n",
    "top_categories"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "aa222ba1-446d-49c8-aa76-827012288d08",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(payment_method\n",
       " Cash           44447\n",
       " Credit Card    34931\n",
       " Debit Card     20079\n",
       " Name: count, dtype: int64,\n",
       " 'Cash',\n",
       " 44447)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "payment_counts = invoices['payment_method'].value_counts()\n",
    "\n",
    "\n",
    "most_common_payment = payment_counts.idxmax()\n",
    "most_common_payment_count = payment_counts.max()\n",
    "\n",
    "payment_counts, most_common_payment, most_common_payment_count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "aab26d18-8482-4c9a-9b99-e461c61a8f90",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "48.909121507909795"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "merged_df = invoices.merge(customers, left_on='customer_id', right_on='id')\n",
    "\n",
    "\n",
    "tech_buyers = merged_df[merged_df['category'] == 'Technology']\n",
    "\n",
    "\n",
    "average_tech_age = tech_buyers['age'].mean()\n",
    "average_tech_age"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "98e7e7e8-5788-4743-9679-f7e4ae0fc3db",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>age_range</th>\n",
       "      <th>10-19</th>\n",
       "      <th>20-29</th>\n",
       "      <th>30-39</th>\n",
       "      <th>40-49</th>\n",
       "      <th>50-59</th>\n",
       "      <th>60-69</th>\n",
       "      <th>70-79</th>\n",
       "      <th>80-89</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>category</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Books</th>\n",
       "      <td>12801.75</td>\n",
       "      <td>79461.75</td>\n",
       "      <td>84143.10</td>\n",
       "      <td>87203.40</td>\n",
       "      <td>74962.20</td>\n",
       "      <td>80476.80</td>\n",
       "      <td>54827.85</td>\n",
       "      <td>26664.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Clothing</th>\n",
       "      <td>1927413.84</td>\n",
       "      <td>10250732.80</td>\n",
       "      <td>11354126.96</td>\n",
       "      <td>11215189.92</td>\n",
       "      <td>10321851.76</td>\n",
       "      <td>10660642.08</td>\n",
       "      <td>7769371.28</td>\n",
       "      <td>4493698.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Cosmetics</th>\n",
       "      <td>109619.36</td>\n",
       "      <td>605915.32</td>\n",
       "      <td>723544.70</td>\n",
       "      <td>665034.96</td>\n",
       "      <td>587780.96</td>\n",
       "      <td>649990.76</td>\n",
       "      <td>419082.62</td>\n",
       "      <td>254531.60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Food &amp; Beverage</th>\n",
       "      <td>13582.31</td>\n",
       "      <td>73491.96</td>\n",
       "      <td>87246.86</td>\n",
       "      <td>89553.29</td>\n",
       "      <td>72425.04</td>\n",
       "      <td>80976.09</td>\n",
       "      <td>55050.98</td>\n",
       "      <td>31332.93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Shoes</th>\n",
       "      <td>993281.35</td>\n",
       "      <td>5924878.24</td>\n",
       "      <td>7200839.66</td>\n",
       "      <td>7025590.02</td>\n",
       "      <td>5852857.84</td>\n",
       "      <td>5978893.54</td>\n",
       "      <td>4480269.05</td>\n",
       "      <td>2628744.60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Souvenir</th>\n",
       "      <td>12375.15</td>\n",
       "      <td>54943.32</td>\n",
       "      <td>64092.72</td>\n",
       "      <td>66391.80</td>\n",
       "      <td>54943.32</td>\n",
       "      <td>55025.43</td>\n",
       "      <td>38673.81</td>\n",
       "      <td>23718.06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Technology</th>\n",
       "      <td>1129800.00</td>\n",
       "      <td>5261550.00</td>\n",
       "      <td>6159300.00</td>\n",
       "      <td>5954550.00</td>\n",
       "      <td>4435200.00</td>\n",
       "      <td>5471550.00</td>\n",
       "      <td>3638250.00</td>\n",
       "      <td>1946700.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Toys</th>\n",
       "      <td>60426.24</td>\n",
       "      <td>385100.80</td>\n",
       "      <td>420582.40</td>\n",
       "      <td>390906.88</td>\n",
       "      <td>345067.52</td>\n",
       "      <td>363955.20</td>\n",
       "      <td>273244.16</td>\n",
       "      <td>153932.80</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "age_range             10-19        20-29        30-39        40-49  \\\n",
       "category                                                             \n",
       "Books              12801.75     79461.75     84143.10     87203.40   \n",
       "Clothing         1927413.84  10250732.80  11354126.96  11215189.92   \n",
       "Cosmetics         109619.36    605915.32    723544.70    665034.96   \n",
       "Food & Beverage    13582.31     73491.96     87246.86     89553.29   \n",
       "Shoes             993281.35   5924878.24   7200839.66   7025590.02   \n",
       "Souvenir           12375.15     54943.32     64092.72     66391.80   \n",
       "Technology       1129800.00   5261550.00   6159300.00   5954550.00   \n",
       "Toys               60426.24    385100.80    420582.40    390906.88   \n",
       "\n",
       "age_range              50-59        60-69       70-79       80-89  \n",
       "category                                                           \n",
       "Books               74962.20     80476.80    54827.85    26664.00  \n",
       "Clothing         10321851.76  10660642.08  7769371.28  4493698.00  \n",
       "Cosmetics          587780.96    649990.76   419082.62   254531.60  \n",
       "Food & Beverage     72425.04     80976.09    55050.98    31332.93  \n",
       "Shoes             5852857.84   5978893.54  4480269.05  2628744.60  \n",
       "Souvenir            54943.32     55025.43    38673.81    23718.06  \n",
       "Technology        4435200.00   5471550.00  3638250.00  1946700.00  \n",
       "Toys               345067.52    363955.20   273244.16   153932.80  "
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Step 1: Merge invoices with customers to get age\n",
    "merged_df = invoices.merge(customers, left_on='customer_id', right_on='id')\n",
    "\n",
    "# Step 2: Calculate total sale per invoice row\n",
    "merged_df['total'] = merged_df['price'] * merged_df['quantity']\n",
    "\n",
    "# Step 3: Drop rows with missing age values\n",
    "merged_df = merged_df.dropna(subset=['age'])\n",
    "\n",
    "# Step 4: Create a new column for age range (decade)\n",
    "merged_df['age_range'] = (\n",
    "    (merged_df['age'] // 10 * 10).astype(int).astype(str) +\n",
    "    '-' +\n",
    "    ((merged_df['age'] // 10 * 10 + 9).astype(int).astype(str))\n",
    ")\n",
    "\n",
    "# Step 5: Create the pivot table\n",
    "pivot_table = pd.pivot_table(\n",
    "    merged_df,\n",
    "    values='total',\n",
    "    index='category',\n",
    "    columns='age_range',\n",
    "    aggfunc='sum',\n",
    "    fill_value=0\n",
    ")\n",
    "\n",
    "pivot_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "035fa1fe-8296-4cff-aa76-78ba5c13ee86",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
