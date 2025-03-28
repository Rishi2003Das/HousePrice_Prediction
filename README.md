# HousePrice_Prediction
An end-to-end machine learning model on California House Price dataset from Kaggle, for house price prediction with regression model.


# 🏡 **California House Price Prediction**  

🚀 **A Machine Learning-powered web application for predicting California house prices.**  
Built using **Flask, Scikit-learn, and Pickle**, this project provides an easy-to-use web interface for estimating housing prices based on key features like median income, house age, and geographical location.  

---

## 📌 **Project Overview**
This project predicts **house prices** in California using a **trained regression model**. It features:
- A **Flask-based web app** for easy interaction.
- **Machine Learning Model** trained on California housing data.
- **Postman API support** for direct JSON-based predictions.
- A **responsive UI** with user-friendly design.

---

## 🚀 **Tech Stack**
- **Frontend**: HTML, CSS (Bootstrap)
- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn, NumPy, Pandas
- **Model Deployment**: Pickle
- **API Testing**: Postman
- **Version Control**: Git, GitHub

---

## 🛠 **Installation & Setup**
### **🔹 Step 1: Clone the Repository**
```bash
git clone https://github.com/Rishi2003Das/HousePrice_Prediction.git
cd HousePrice_Prediction
```

### **🔹 Step 2: Create a Virtual Environment**
```bash
python3 -m venv venv  # For Linux/Mac
venv\Scripts\activate  # For Windows
source venv/bin/activate  # Linux/Mac
```

### **🔹 Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **🔹 Step 4: Run the Flask App**
```bash
python app.py
```
The application will start at **`http://127.0.0.1:5000/`**.

---

## 📡 **Using the API in Postman**
### **Endpoint**:  
```
POST http://127.0.0.1:5000/predict_api
```
### **Sample JSON Input**
```json
{
    "data": {
        "MedInc": 5.2,
        "HouseAge": 15,
        "AveRooms": 6.8,
        "AveBedrms": 1.1,
        "Population": 3000,
        "AveOccup": 3.5,
        "Latitude": 37.77,
        "Longitude": -122.42
    }
}
```
### **Sample JSON Response**
```json
{
    "prediction": 250000.75
}
```

---

## 🎨 **User Interface**
- **Home Page**: Users can input house details and get predictions.
- **Login System**: Ensures authenticated access.
- **Mobile-Responsive Design**: Works on all devices.

![UI Preview](https://source.unsplash.com/1600x900/?realestate,houses)

---

## 🔐 **Authentication System**
This project includes **user authentication** using **Flask-Login**:
- User login and signup
- Secure password storage with **Werkzeug**
- Session-based authentication

---

## 📂 **Project Structure**
```
HousePrice_Prediction/
│-- templates/
│   ├── home.html        # Main UI
│   ├── login.html       # Login page
│-- static/
│   ├── style.css        # Stylesheet
│-- app.py               # Main Flask app
│-- regmodel.pkl         # Trained ML model
│-- scaling.pkl          # Scaler for input data
│-- requirements.txt     # Dependencies
│-- README.md            # Documentation
```

---

## 📝 **Future Enhancements**
✅ Add database integration for storing user inputs.  
✅ Deploy on **AWS / Heroku**.  
✅ Implement **Real-time price trends visualization**.  

---

## 👨‍💻 **Contributors**
💡 **Rishi Das** - [GitHub](https://github.com/Rishi2003Das)  

Feel free to contribute by submitting issues or pull requests! 🚀

---

## 📜 **License**
This project is **open-source** under the **MIT License**.  

🔗 **GitHub Repo**: [HousePrice_Prediction](https://github.com/Rishi2003Das/HousePrice_Prediction)

---
⭐ **Star this repo** if you found it useful! 😊 Happy coding! 🚀