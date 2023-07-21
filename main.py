# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
from unittest import main

# Read data from 'adult.data.csv' file
with open('adult.data.csv', 'r') as file:
  data = [line.strip().split(",") for line in file]

# Call the function and pass the data directly
demographic_data = demographic_data_analyzer.calculate_demographic_data(
  data, print_data=True)

# Run unit tests automatically
main(module='test_module', exit=False)
