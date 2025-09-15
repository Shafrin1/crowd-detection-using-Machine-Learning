# crowd-detection-using-Machine-Learning

A real-time **crowd detection system** using **OpenCV** and **Haarcascade classifier** to detect faces from a live webcam feed. The system counts the number of faces detected and alerts if a crowd is present.

---

## 🔹 Features
- Real-time video capture using webcam
- Face detection using `haarcascade_frontalface_default.xml`
- Crowd status indicator:
  - **No Crowd** → when 0 faces are detected
  - **Crowd Detected** → when ≥ 1 face is detected
- Rectangle overlay on detected faces
- Press **`q`** to quit the program

---

## 🔹 Technologies Used
- **Python 3**
- **OpenCV**
- **NumPy**

---

## 🔹 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Shafrin1/crowd-detection-using-Machine-Learning.git
   cd crowd-detection-using-Machine-Learning
