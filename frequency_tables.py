import pandas as pd

# Set the file path manually
file_name = "FILE PATH"

# Prompt the user for the lower class limit, class width, and relative frequency precision
lower_class_limit = float(input("Enter the lower class limit: "))
class_width = float(input("Enter the class width: "))
rel_freq_precision = int(input("Enter the relative frequency precision: "))

# Read the cigarette tax data from the text file
with open(file_name, 'r') as file:
    tax_data = [float(line.strip()) for line in file]

# Create a pandas DataFrame to hold the frequency distribution data
freq_dist = pd.DataFrame(columns=['Tax', 'Frequency'])
rel_freq_dist = pd.DataFrame(columns=['Tax', 'Relative Frequency'])

# Set the precision for the lower class limit
precision = len(str(class_width + 1).split('.')[1])

# Iterate through the range of upper class limits
upper_class_limit = lower_class_limit + class_width
while upper_class_limit <= (max(tax_data) + (class_width * 2)):

    # Count the number of data points that fall within the class limits
    frequency = len(
        [x for x in tax_data if lower_class_limit <= x < upper_class_limit])

    # Round down the lower class limit to the same precision as one more than the class width
    lower_class_limit = round(lower_class_limit, precision)
    upper_class_limit = round(upper_class_limit, precision)

    # Add the class limits and frequency to the frequency distribution DataFrame
    temp_df = pd.DataFrame({'Tax': [f'{lower_class_limit}-{upper_class_limit-0.01}'],
                           'Frequency': [frequency]})
    freq_dist = pd.concat([freq_dist, temp_df], ignore_index=True)

    # Calculate the relative frequency for each class interval
    rel_frequency = round(frequency / len(tax_data), rel_freq_precision)
    
    # Add the class limits and relative frequency to the relative frequency distribution DataFrame
    temp_df = pd.DataFrame({'Tax': [f'{lower_class_limit}-{upper_class_limit-0.01}'],
                           'Relative Frequency': [rel_frequency]})
    rel_freq_dist = pd.concat([rel_freq_dist, temp_df], ignore_index=True)
    lower_class_limit = upper_class_limit
    upper_class_limit += class_width

print(freq_dist)
print(rel_freq_dist)
