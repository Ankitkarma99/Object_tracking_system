# **🎯 Object Tracking System (Streamlit + YOLO)**

[![Python](https://img.shields.io/badge/Python-3.11-blue)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)]()
[![Ultralytics YOLO](https://img.shields.io/badge/YOLO-Object_Tracking-green)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-Video_Processing-purple)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

---

## 📘 Overview

The **Object Tracking System** is a Streamlit-based web application for **tracking objects in videos** using the **YOLO (You Only Look Once) model**.
Users can upload a video, and the app will detect and track objects in real-time, displaying the results frame by frame.

---

## 🚀 Features

* Upload video files (`.mp4`) for tracking
* Real-time object tracking using **YOLOv8**
* Visualization of tracked objects with bounding boxes
* Lightweight and interactive interface with **Streamlit**

---

## 🛠 Tech Stack

| Technology           | Use                           |
| -------------------- | ----------------------------- |
| **Python 3.11+**     | Core programming language     |
| **Streamlit**        | Web interface                 |
| **OpenCV**           | Video and image processing    |
| **Ultralytics YOLO** | Object detection and tracking |
| **os**               | File handling                 |

---

## 📁 Project Structure

```
📦 Object-Tracking-System
 ┣ 📜 app.py               # Streamlit interface
 ┣ 📜 main.py              # YOLO object tracking script
 ┣ 📂 videos/              # Sample video files
 ┃   ┣ 📄 vid2.mp4
 ┃   ┗ 📄 vid3.mp4
 ┣ 📜 yolo11n.pt           # YOLO model file
 ┗ 📂 README.md
```

---

## 📥 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/object-tracking-system.git
cd object-tracking-system
```

### 2️⃣ Install Dependencies

```bash
pip install streamlit opencv-python ultralytics
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

* Upload a video file (`.mp4`)
* Watch real-time object tracking results

---

## 📄 Usage

1. Open the Streamlit app in the browser.
2. Click **Upload Video** and select your file.
3. The YOLO model will process each frame and track objects.
4. The output is displayed interactively on the Streamlit interface.

---

## 📝 Notes

* Ensure your **YOLO model file (`yolo11n.pt`)** is present in the project directory.
* Larger videos may take more processing time.
* Press **q** in `main.py` if running outside Streamlit to quit the video window.

---

## 🤝 Contribution

Pull requests are welcome! Improve the app by adding:

* Multiple video format support
* Real-time webcam tracking
* Advanced tracking visualization

---

## 📜 License

MIT License

---
