CheatShield AI - Advanced Exam Surveillance

Overview

CheatShield AI is an advanced cheating detection system that uses AI-powered object detection to monitor exam environments in real-time. This tool can analyze video feeds to detect suspicious activities, such as the use of unauthorized devices (cell phones, tablets, books) and suspicious hand movements indicative of paper exchanges.

Features

Real-Time Video Analysis: Supports both live camera feeds and pre-recorded videos.

AI-Powered Detection: Uses YOLOv8 for object and movement detection.

Multiple Cheating Indicators: Detects unauthorized devices like mobile phones, laptops, books, and tablets.

Hand Movement Tracking: Flags suspicious hand movements indicating potential paper exchanges.

User-Friendly Interface: Simple UI built using Tkinter.

Requirements

Ensure the following dependencies are installed before running the application:

pip install opencv-python numpy tkinter torch ultralytics pillow

Installation

Clone the repository:

git clone https://github.com/ravikirank2018/CheatShield-AI---Advanced-Exam-Surveillance.git

Install dependencies:

pip install -r requirements.txt

Download the YOLOv8 model (if not included):

wget https://github.com/ultralytics/yolov8/releases/download/v8.0/yolov8n.pt

Usage

Run the Application

To start the application, run:

python cheatshield_ai.py

Options

Upload Video: Allows you to select and analyze a pre-recorded video.

Use Camera: Uses a live webcam feed to detect cheating in real-time.

How It Works

The application loads the YOLOv8 model to detect objects in frames.

It scans for faces, hands, and unauthorized devices.

If a hand moves significantly between two different persons, it flags a suspicious hand movement.

If a cheating tool (like a mobile phone or book) is detected, it displays an alert.
