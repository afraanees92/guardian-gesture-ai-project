# Guardian Gesture AI Project

An AI-powered smart emergency detection and alert system developed using AWS Cloud services and Python.

This project automatically detects emergency-related objects, gestures, and situations from uploaded images using Amazon Rekognition and instantly sends alert notifications through Amazon SNS.

---

# Project Objective

The objective of this project is to create a cloud-based real-time emergency monitoring system that can identify dangerous or emergency situations from images and notify users immediately through email alerts.

---

# Technologies Used

## Programming Language
- Python

## Cloud Platform
- Amazon Web Services (AWS)

## AWS Services Used
- Amazon S3
- AWS Lambda
- Amazon Rekognition
- Amazon SNS
- AWS IAM

---

# Project Architecture

1. User uploads an image into the Amazon S3 bucket
2. Amazon S3 automatically triggers the AWS Lambda function
3. Lambda function processes the uploaded image
4. Amazon Rekognition analyzes image labels
5. Emergency-related labels are identified
6. Amazon SNS sends an email alert notification to the subscribed user

---

# Features

- Real-time image-based emergency detection
- Automatic serverless execution using AWS Lambda
- Detects:
  - Person
  - Hand
  - Finger
  - Face
  - Fire
  - Smoke
  - Crowd
  - Human
  - Gesture
- Sends instant email alerts
- Includes confidence percentage
- Includes detection timestamp
- Fully automated workflow
- Cloud-native and scalable architecture

---

# Sample Alert Message

Detected: Fire  
Confidence: 95.37%  
Image: image2.jpeg  
Time: 2026-05-07 21:25:53

---

# IAM Permissions Used

The Lambda execution role was configured with the following permissions:

- AmazonRekognitionFullAccess
- AmazonS3ReadOnlyAccess
- AmazonSNSFullAccess
- AWSLambdaBasicExecutionRole

---

# Folder Structure

guardian_gesture_AI_project/

├── screenshots/  
├── lambda_function.py  
├── README.md

---

# Screenshots Included

- S3 bucket creation
- SNS subscription setup
- Lambda function creation
- IAM permission configuration
- Lambda code implementation
- S3 trigger configuration
- Test image uploads
- Email alert detection results

---

# Future Enhancements

- Live webcam integration
- SMS alert notifications
- Mobile app integration
- Video stream analysis
- Machine learning-based custom gesture detection
- Dashboard monitoring system

---

# Learning Outcomes

Through this project, I learned:

- AWS serverless architecture
- Event-driven cloud computing
- Image recognition using Amazon Rekognition
- Real-time cloud automation
- SNS notification services
- IAM role and policy management
- Cloud security and permissions handling

---

# Author

Afra Anees

Cloud & AI Enthusiast