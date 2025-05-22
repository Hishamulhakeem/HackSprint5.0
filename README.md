# 🌾 Real-Time Agriculture Solutions Panel

A comprehensive AI-powered platform providing intelligent, real-time solutions for modern farming. This project integrates cutting-edge machine learning techniques with practical tools to help farmers make data-driven decisions for better yield, disease control, market insight, and assistance.

---

## 🚀 Features

### 1. 🧪 Crop and Soil Management
Optimize crop yields by recommending the most suitable crop based on soil attributes provided by the user.
- **Input:** Soil parameters (N, P, K values, pH, moisture, etc.)
- **Output:** Best-suited crop for the soil
- **Model:** Trained ML classifier using real agricultural datasets

---

### 2. 🌿 AI-Driven Crop Disease Predictor
Detect plant diseases from leaf images using a CNN (Convolutional Neural Network).
- **Input:** Upload or capture image of infected crop
- **Output:** Predicted disease with treatment guide
- **Extras:** Embedded educational video for treatment suggestions

---

### 3. 📈 Predicting Prices of Agri-Horticultural Commodities
Forecast crop prices across different seasons using statistical and machine learning models.
- **Input:** Crop name, location, and season
- **Output:** Predicted Minimum, Average, and Maximum prices
- **Use Case:** Helps farmers decide when and where to sell crops for maximum profit

---

### 4. 🤖 Q&A Chatbot (RAG-based)
An intelligent chatbot using Retrieval-Augmented Generation (RAG) to answer agriculture-related queries.
- **Input:** User's natural language questions
- **Output:** Accurate, contextual answers fetched from relevant documents
- **Functionality:** Acts as a personal assistant for farmers and agri-professionals

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript (with frameworks or plain)
- **Backend:** Python (Flask / FastAPI)
- **Machine Learning:** 
  - Crop recommendation: Random Forest / Decision Tree
  - Disease prediction: CNN (TensorFlow / PyTorch)
  - Price prediction: Time Series + Regression Models
- **RAG Chatbot:** Hugging Face Transformers + FAISS
- **Deployment:** Streamlit / Flask Web App / Docker (optional)

---

## 🖼️ Screenshots

### 📋 Dashboard
![image](https://github.com/user-attachments/assets/68ade5a5-d5a5-40f8-afb0-1ce9e2af98fc)


### 🌿 Disease Predictor
![image](https://github.com/user-attachments/assets/44db2714-f8ea-446d-ba9f-0151b1e7b451)


---

## 📚 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/agriculture-ai-panel.git
   cd agriculture-ai-panel
