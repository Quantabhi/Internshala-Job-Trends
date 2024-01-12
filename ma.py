from bs4 import BeautifulSoup
import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt

base_url = 'https://internshala.com/internships/'
num_pages = 150

# Create an empty dictionary to store category counts
category_counts = {}

for page in range(1, num_pages + 1):
    url = f'{base_url}{page}'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('div', class_='internship_meta')
    for job in jobs:
        category = job.find('h3', class_='heading_4_5 profile').text.strip()

        # Combine similar categories for Content Writing
        if "Content Writing" in category:
            category = "Content Writing"

        # Combine similar categories for Marketing
        if "Marketing" in category:
            category = "Marketing"
              # combine  similar categories for  Business Development
        if "Business Development" in category:
            category = "Business Development"
            # combine  similar categories for  Business Development
        if "Sales" in category:
            category = "Sales"

        # Update category count in the dictionary
        category_counts[category] = category_counts.get(category, 0) + 1

# Convert the dictionary data to a DataFrame for Seaborn
data = {'Category': list(category_counts.keys()), 'Count': list(category_counts.values())}
df = pd.DataFrame(data)

# Sort the DataFrame by count in descending order
df = df.sort_values(by='Count', ascending=False)

# Create a horizontal bar plot using Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Count', y='Category', data=df, palette='viridis')
plt.title('Analyzing the top internships posted on the Internshala website')
plt.xlabel('Count')
plt.ylabel('Internship Category')
plt.show()
