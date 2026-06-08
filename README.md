📊 Supermarket Sales Dashboard
An interactive sales analytics dashboard built with Streamlit and Plotly. Upload your supermarket sales CSV and instantly explore KPI metrics and revenue breakdowns by product line.

📁 Project Structure
ai_dashboard_project/
├── app.py                  # Main Streamlit source code
├── README.md               # Project documentation (this file)
├── dataset_info.md         # Dataset details and link
├── instructions.md         # How to run the project
└── screenshots/
    ├── screenshot_metrics.png
    └── screenshot_chart.png
🚀 Features
KPI Cards — Total Revenue, Total Quantity Sold, Average Rating
Dataset Preview — Scrollable table of the first 5 rows
Interactive Bar Chart — Revenue broken down by Product Line (Plotly)
Wide Layout — Clean, professional dashboard styling
📦 Requirements
Python 3.7+
streamlit
pandas
plotly
Install all dependencies:

pip install streamlit pandas plotly
▶️ How to Run
streamlit run app.py
The dashboard opens automatically at http://localhost:8501

📊 Dataset
The app expects a file named sales.csv in the same directory.
See dataset_info.md for the dataset link and column reference.

🌐 Running on Google Colab (optional)
If running in Colab, use pyngrok to expose the local port:

!pip install streamlit pyngrok
!streamlit run app.py &>/content/logs.txt &

from pyngrok import ngrok
ngrok.set_auth_token("YOUR_NGROK_TOKEN")
public_url = ngrok.connect(8501)
print(public_url)
⚠️ Replace YOUR_NGROK_TOKEN with your token from ngrok.com
