# Importing necessary libraries for data handling and anomaly detection
import pandas as pd
import numpy as np
import glob
import os
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

#Install necessary packages
pip install openpyxl

# Define the file path
file_path = r"C:\Users\Vinotha R\Downloads\m3data.xlsx"

# Print the file path
print(file_path)

#Partitioning the datasets
import pandas as pd
from sklearn.model_selection import train_test_split

# File path where the preprocessed Excel file is stored
file_path = r"C:\Users\Vinotha R\Downloads\m3data.xlsx"

# Load the Excel file
df = pd.read_excel(file_path)

# Split the data into training and testing sets
train, test = train_test_split(df, test_size=0.30, random_state=42)

# Save the training and testing sets to Excel files
train.to_excel(r"C:\Users\Vinotha R\Downloads\training_setm3.xlsx", index=False)
test.to_excel(r"C:\Users\Vinotha R\Downloads\testing_setm3.xlsx", index=False)

print('Training and testing datasets have been saved as Excel files.')

#Print the result
vts= pd.read_excel(r"C:\Users\Vinotha R\Downloads\training_setm3.xlsx")
print(vts.head(5))

#Training the model
# Step 1: Prepare the data
# We only need the duration for anomaly detection
X=vts[['duration','location_id']]

# Step 2: Train the Isolation Forest model
model= IsolationForest(contamination='auto',random_state = 64)
vts['status'] = model.fit_predict(X)

# Step 3: Convert the anomaly labels to a more understandable format
# Anomalies are labeled as -1, and normal points as 1
vts['status'] = vts['status'].map({1:'Normal',-1:'Anomaly'})

# Step 4: Display results with the required columns
result=vts[['vehicle_number', 'duration', 'location_id', 'status']]
print(result)

#Export the data into excelsheet
data = result.to_excel(r"C:\Users\Vinotha R\Downloads\anomaliesm3.xlsx")

#Plotting the data
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import interp1d  # Importing interp1d for interpolation

# Step 5: Create a bell curve using kernel density estimation (KDE)
plt.figure(figsize=(12, 6))

# Loop through unique location_ids to create KDE plots
for loc in result['location_id'].unique():
    # Plot the KDE for the location
    sns.kdeplot(result[result['location_id'] == loc]['duration'], 
                 label=f'Location ID: {loc}', 
                 fill=True)

# Calculate the density values for the normal and anomaly points
kde = sns.kdeplot(result['duration'], bw_adjust=0.5)  # Adjust bandwidth for better fit
x_vals = np.linspace(result['duration'].min(), result['duration'].max(), 100)
densities = kde.get_lines()[0].get_data()[1]  # Get density values from the plot

# Create a mapping from duration to density using interpolation
density_map_func = interp1d(kde.get_lines()[0].get_data()[0], densities, bounds_error=False, fill_value=0)


# Scatter plot for normal and anomaly points
normal_data = result[result['status'] == 'Normal']
anomaly_data = result[result['status'] == 'Anomaly']

# Plot normal points at their interpolated density values
normal_density_values = density_map_func(normal_data['duration'].values)
plt.scatter(normal_data['duration'], normal_density_values, 
            color='blue', marker='o', label='Normal Points', alpha=0.6)

# Plot anomaly points at their interpolated density values
anomaly_density_values = density_map_func(anomaly_data['duration'].values)
plt.scatter(anomaly_data['duration'], anomaly_density_values, 
            color='red', marker='x', label='Anomaly Points', alpha=0.6)

# Adding labels and title
plt.title('Bell Curve of Duration by Location ID with Normal and Anomaly Points')
plt.xlabel('Duration')
plt.ylabel('Density')
plt.legend()
plt.grid()

# Show plot
plt.show()
