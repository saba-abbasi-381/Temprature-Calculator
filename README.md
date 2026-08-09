# 🌡️ Temperature Converter

A simple and interactive temperature conversion web application built with **Python and Streamlit**. The project uses **Object-Oriented Programming (OOP)** to separate the conversion logic from the user interface.

## 📌 Overview

The Temperature Converter allows users to convert temperatures between **Celsius and Fahrenheit** through a simple Streamlit interface.

The project follows a basic frontend-backend structure:

* **Frontend:** Streamlit interface for user interaction
* **Backend:** Python class containing the temperature conversion logic

This project was built to practice **Python OOP, modular programming, and Streamlit application development**.

## ✨ Features

* 🌡️ Celsius → Fahrenheit conversion
* 🌡️ Fahrenheit → Celsius conversion
* 🖥️ Interactive Streamlit interface
* 🧩 Backend logic implemented using a Python class
* 🔄 Separate frontend and backend files
* ⚠️ Warning message when no conversion type is selected

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Object-Oriented Programming (OOP)**

## 📂 Project Structure

```text
Temperature-Converter/
│
├── app.py
├── backend.py
└── README.md
```

### `app.py`

Contains the Streamlit frontend and handles:

* User input
* Conversion selection
* Button interaction
* Displaying the conversion result

### `backend.py`

Contains the `TemperatureConverter` class and the conversion methods:

* `celsius_to_fahrenheit()`
* `fahrenheit_to_celsius()`

## ⚙️ How It Works

1. The user enters a temperature.
2. The user selects a conversion type.
3. The Streamlit interface passes the temperature to the backend class.
4. The appropriate conversion method is called.
5. The converted temperature is displayed to the user.

## 🚀 Installation & Usage

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Temperature-Converter
```

### 2. Install Streamlit

```bash
pip install streamlit
```

### 3. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📚 What I Learned

Through this project, I practiced:

* Building interactive interfaces with Streamlit
* Creating and using Python classes
* Applying Object-Oriented Programming concepts
* Separating frontend and backend logic
* Handling user input and button interactions
* Connecting a Streamlit frontend with backend Python logic

## 🔮 Future Improvements

Possible improvements for future versions include:

* Add more temperature units such as Kelvin
* Add input validation
* Improve error handling
* Add conversion history
* Improve the user interface

## 👩‍💻 Author

**Saba Abbasi**

Aspiring AI Engineer | Python Developer

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.
