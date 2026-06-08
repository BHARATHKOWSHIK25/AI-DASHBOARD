# ▶️ Instructions to Run the Project

---

## Option A — Run Locally (Recommended)

### Step 1 — Install Python
Make sure Python 3.7+ is installed:
```bash
python --version
```

### Step 2 — Install Dependencies
```bash
pip install streamlit pandas plotly
```

### Step 3 — Get the Dataset
Download `sales.csv` from Kaggle or use the direct link in `dataset_info.md`.  
Rename the file to `sales.csv` and place it in the same folder as `app.py`.

```
ai_dashboard_project/
├── app.py
├── sales.csv     ← place here
```

### Step 4 — Run the App
```bash
streamlit run app.py
```

### Step 5 — Open in Browser
Streamlit will print a local URL:
```
Local URL:  http://localhost:8501
```
Open it in your browser. The dashboard loads automatically.

---

## Option B — Run on Google Colab

### Step 1 — Install packages
```python
!pip install streamlit pyngrok plotly pandas
```

### Step 2 — Upload your CSV
```python
from google.colab import files
uploaded = files.upload()   # upload sales.csv
```

### Step 3 — Write and run the app
```python
%%writefile app.py
# paste the full contents of app.py here
```
```python
!streamlit run app.py &>/content/logs.txt &
```

### Step 4 — Expose with ngrok
Get a free token at [ngrok.com](https://dashboard.ngrok.com/signup), then:
```python
from pyngrok import ngrok
ngrok.set_auth_token("YOUR_NGROK_TOKEN")
public_url = ngrok.connect(8501)
print(public_url)
```
Click the printed URL to open the live dashboard.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Run `pip install streamlit pandas plotly` |
| `FileNotFoundError: sales.csv` | Make sure `sales.csv` is in the same folder as `app.py` |
| Port 8501 already in use | Run `pkill streamlit` then retry |
| Blank chart | Check that `Product line` and `Total` columns exist in your CSV |
| Colab dashboard not loading | Make sure ngrok token is valid and `streamlit` is running in background |
