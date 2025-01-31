# Real-Time Drowsiness Detection System

### 🚗 **Stay Alert, Stay Safe!**

Welcome to the **Real-Time Drowsiness Detection System**, a powerful tool designed to help monitor driver alertness and prevent accidents caused by drowsiness. Using cutting-edge technologies like **Python**, **Raspberry Pi**, **OpenCV**, and **Dlib**, this system continuously tracks your facial features and gives immediate feedback when drowsiness is detected.

---

### 💡 **Project Overview**

Drowsiness detection is a critical feature in many safety applications, especially for drivers. This system uses face landmark detection to monitor your eye movements and detects signs of fatigue, alerting you with a buzzer and LCD display when it's time to take a break.

---

### 🔧 **Technologies Used**

- **Python**: The programming language used to bring this system to life.
- **Raspberry Pi**: The brains of the project, running the entire application and handling real-time image processing.
- **OpenCV**: For capturing video feed and processing the frames for face detection.
- **Dlib**: For accurate face landmark detection and calculating eye aspect ratio to detect drowsiness.
- **Buzzer**: Alerts the user with sound when drowsiness is detected.
- **LCD Display**: Displays a real-time warning message when the system detects signs of drowsiness.

---

### ⚙️ **How It Works**

1. **Face Detection**: The system uses OpenCV to capture video from a webcam connected to the Raspberry Pi.
2. **Landmark Detection**: Dlib is used to detect facial landmarks, focusing on the eyes.
3. **Drowsiness Calculation**: By measuring the **Eye Aspect Ratio (EAR)**, the system identifies whether the eyes are closing for too long, a sign of drowsiness.
4. **Alert**: When the EAR falls below a certain threshold, the system sounds a buzzer and displays a warning on the LCD screen.
5. **Continuous Monitoring**: The system runs in real-time, keeping you safe and alert throughout the session.

---

### 🔨 **Setup Instructions**

1. **Hardware Requirements**:
   - Raspberry Pi (any model with camera support)
   - Camera module or USB webcam
   - LCD Display (16x2)
   - Buzzer

2. **Software Requirements**:
   - Raspberry Pi OS
   - Python 3
   - OpenCV (`pip install opencv-python`)
   - Dlib (`pip install dlib`)
   - RPi.GPIO (for controlling the buzzer and LCD)

3. **Installation**:
   - Clone this repository:
     ```bash
     git clone https://github.com/Insane30/Drowsiness-Detection.git
     cd Drowsiness-Detection
     ```
   - Install required libraries:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the system:
     ```bash
     python drowsiness_detection.py
     ```

---

### 📸 **Preview**

![Drowsiness Detection](images/preview.jpg)  
*Real-time face detection and alert system in action.*

---

### 🎥 **Project Demonstration Video**

Watch the project in action!  

[![Drowsiness Detection System Demo](https://img.youtube.com/vi/5FL2j0Voyw8/hqdefault.jpg)](https://youtu.be/5FL2j0Voyw8?si=8bHkGyG3G_7uwuuM)

---

### ⚠️ **Future Improvements**

- **Multiple User Support**: Implement a multi-user mode to track multiple drivers.
- **Machine Learning Integration**: Use deep learning models for more accurate drowsiness detection.
- **Mobile Application**: Develop a mobile app that syncs with the Raspberry Pi system for remote monitoring.

---

### 🤝 **Contributing**

Feel free to fork the repository, open issues, or submit pull requests. Contributions are always welcome to improve this project and make it even more efficient and accurate.

---

Stay safe, stay alert! 🧑‍🔧💡
