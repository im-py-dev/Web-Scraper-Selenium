from selenium import webdriver
import csv

# Set up Selenium webdriver
driver = webdriver.Chrome()

# Define the URL of the website to scrape
url = 'https://www.example.com'

# Navigate to the URL
driver.get(url)

# Find the elements containing the data you want to scrape
data_elements = driver.find_elements_by_css_selector('.example-data')

# Define a list to hold the extracted data
data = []

# Loop through each element and extract the text
for element in data_elements:
    text = element.text
    data.append(text)
   
# For Multple columns
for row in data_elements:
    columns = row.find_elements_by_css_selector('.example-col')
    row_data = {}
    for i, column in enumerate(columns):
        text = column.text
        header = f'Column {i + 1}'
        row_data[header] = text
    data.append(row_data)

# Save the data to a CSV file
with open('example_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Data'])
    for item in data:
        writer.writerow([item])

# Close the webdriver
driver.quit()
