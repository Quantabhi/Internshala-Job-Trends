# Internship Category Analysis on Internshala

This Python script analyzes the top internship categories posted on the Internshala website. It scrapes data from multiple pages of internship listings and visualizes the counts of each category using Seaborn.

## How It Works

The script performs the following steps:

- Makes HTTP requests to Internshala internship pages.
- Extracts internship category data using BeautifulSoup.
- Combines similar categories for better analysis (e.g., Content Writing, Marketing).
- Updates and maintains category counts in a dictionary.
- Converts the dictionary data to a Pandas DataFrame for Seaborn.
- Sorts the DataFrame by count in descending order.
- Creates a horizontal bar plot using Seaborn to visualize the internship category counts.

##Disclaimer

This script is intended for educational purposes only. Use responsibly and ensure compliance with the terms of service of the websites you are scraping.
