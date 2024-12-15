import os
from bs4 import BeautifulSoup

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get a list of all HTML files in the current directory
html_files = [file for file in os.listdir(current_dir) if file.endswith('.html')]

# Initialize a variable to store the total sum
total_sum_of_reservations = 0

# Loop through each HTML file
for html_file in html_files:
    # Read HTML content from the file
    with open(os.path.join(current_dir, html_file), 'r') as file:
        html_source = file.read()

    # Initialize Beautiful Soup with the HTML source
    soup = BeautifulSoup(html_source, 'html.parser')

    # Find all 'Number of reservations' elements using the appropriate CSS selector
    reservations_elements = soup.select('td[data-label="Number of reservations"]')

    # Initialize a variable to store the sum for this file
    sum_of_reservations = 0

    # Loop through each 'Number of reservations' element and add its value to the sum
    for element in reservations_elements:
        value = int(element.text.strip())
        sum_of_reservations += value

    # Add the sum for this file to the total sum
    total_sum_of_reservations += sum_of_reservations

    # Print the sum for this file
    print(f"Sum of Number of reservations in '{html_file}':", sum_of_reservations)

# Print the total sum of 'Number of reservations' values across all files
print("Total Sum of Number of reservations in all files:", total_sum_of_reservations)
