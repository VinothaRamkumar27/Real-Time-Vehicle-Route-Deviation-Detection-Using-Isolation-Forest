# 🚗 Vehicle Anomaly Detection using Isolation Forest

This project implements an anomaly detection system using the **Isolation Forest algorithm** to identify anomalies in vehicle route durations. It uses data preprocessing, training/testing split, model training, and visualization techniques (like KDE and bell curves) to detect anomalies in vehicle trip durations across various location IDs.

---

## 📦 Features

- Load and preprocess vehicle telemetry data (`duration`, `location_id`)
- Split data into training and testing sets (70/30)
- Apply **Isolation Forest** for anomaly detection
- Save results to Excel files
- Visualize results using **Kernel Density Estimation (KDE)**
- Highlight anomalies and normal values on a **bell curve plot**

---

## 🧠 Technologies Used

| Task                     | Tool/Library         |
|--------------------------|----------------------|
| Data handling            | `pandas`, `numpy`    |
| Machine Learning         | `sklearn.ensemble.IsolationForest` |
| Data Visualization       | `matplotlib`, `seaborn` |
| Excel export             | `openpyxl`           |
| Interpolation            | `scipy.interpolate.interp1d` |

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install pandas numpy openpyxl matplotlib seaborn scikit-learn scipy
```
2. Update File Path
Make sure to set the correct Excel file path in the script:

```bash
file_path = r"C:\Path\To\Your\File\m3data.xlsx"
```
3. Run the Script
```bash
python detect_anomalies.py
```
## 🧠 How It Works

The anomaly detection system follows these key steps:

### 1. 📥 Data Loading
The system starts by reading vehicle telemetry data from an Excel file. The primary features used are:
- `duration`: Time taken for a trip
- `location_id`: Identifier for a route or region

### 2. ✂️ Data Splitting
The dataset is split into:
- **Training Set (70%)**: Used to train the Isolation Forest model
- **Testing Set (30%)**: Reserved for evaluation and further testing

### 3. ⚙️ Model Training
The **Isolation Forest** algorithm is applied to detect anomalies in the training data:
- It builds an ensemble of decision trees.
- Anomalies are data points that are isolated quickly in the tree structure.

### 4. 🔍 Anomaly Detection
Each data point is labeled as:
- `Normal` (1) – if it fits well within the general pattern
- `Anomaly` (-1) – if it significantly deviates from the majority

The model’s output is added as a new column `status`.

### 5. 📊 Visualization
A **KDE (Kernel Density Estimation)** plot is generated for each `location_id`:
- The plot shows a bell-curve-like distribution of trip durations.
- Detected anomalies are overlaid using red “X” markers.
- Normal values are shown as blue dots, helping to visually distinguish outliers.

### 6. 💾 Result Export
All final results — including vehicle number, duration, location, and anomaly status — are exported to an Excel file (`anomaliesm3.xlsx`) for easy review or reporting.

## Sample Outputs

![Alt Text](https://github.com/VinothaRamkumar27/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-Forest/blob/249b36f8d37315bb07f691f3cddd0c7db5e36719/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-For/Sample%20outputs/999f264c-2879-40b5-ae32-5558eb96b7b0.png)

![Alt Text](https://github.com/VinothaRamkumar27/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-Forest/blob/249b36f8d37315bb07f691f3cddd0c7db5e36719/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-For/Sample%20outputs/fc08736f-cfe2-4525-815f-d3ee15307e69.png)

![Alt Text](https://github.com/VinothaRamkumar27/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-Forest/blob/249b36f8d37315bb07f691f3cddd0c7db5e36719/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-For/Sample%20outputs/7beceeb5-a07a-41ef-a177-c4a05a4c3dcd.png)

![Alt Text](https://github.com/VinothaRamkumar27/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-Forest/blob/249b36f8d37315bb07f691f3cddd0c7db5e36719/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-For/Sample%20outputs/2b44e4c9-9295-4533-a156-ecd76d36e072.png)

![Alt Text](https://github.com/VinothaRamkumar27/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-Forest/blob/249b36f8d37315bb07f691f3cddd0c7db5e36719/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-For/Sample%20outputs/4ee18063-1952-496c-a1de-8e9222127da3.png)

![Alt Text](https://github.com/VinothaRamkumar27/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-Forest/blob/249b36f8d37315bb07f691f3cddd0c7db5e36719/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-For/Sample%20outputs/4f29fb47-7820-4a2f-b16d-57655ec7b693.png)

![Alt Text](https://github.com/VinothaRamkumar27/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-Forest/blob/249b36f8d37315bb07f691f3cddd0c7db5e36719/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-For/Sample%20outputs/6e0511a2-a069-4313-805b-8c025052ee8b.png)

![Alt Text](https://github.com/VinothaRamkumar27/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-Forest/blob/249b36f8d37315bb07f691f3cddd0c7db5e36719/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-For/Sample%20outputs/8397646e-ebd2-4544-a039-b5f04c8cbaae.png)

![Alt Text](https://github.com/VinothaRamkumar27/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-Forest/blob/249b36f8d37315bb07f691f3cddd0c7db5e36719/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-For/Sample%20outputs/9037ba7e-e396-4b78-8e38-a34d392b3694.png)

![Alt Text](https://github.com/VinothaRamkumar27/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-Forest/blob/249b36f8d37315bb07f691f3cddd0c7db5e36719/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-For/Sample%20outputs/b3d25473-a359-440a-bed2-25694bb5868b.png)

![Alt Text](https://github.com/VinothaRamkumar27/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-Forest/blob/249b36f8d37315bb07f691f3cddd0c7db5e36719/Real-Time-Vehicle-Route-Deviation-Detection-Using-Isolation-For/Sample%20outputs/fa792d12-6c50-45d5-a1e9-a45e089d7a6d.png)

## ✅ Conclusion

This project effectively applies the **Isolation Forest** algorithm to detect anomalies in vehicle trip data based on duration and location identifiers. The system identifies patterns in the data and flags unusual values that may indicate route deviations, delays, or other irregularities.

By preprocessing the data, splitting it into training and testing sets, and applying an unsupervised learning approach, the project ensures that anomalies are detected without needing labeled data. The results are then saved in Excel format, making it easy to interpret and integrate with external systems or reports.

This anomaly detection model provides a foundation for improving route efficiency, monitoring fleet behavior, and enhancing overall decision-making in transportation and logistics operations.




