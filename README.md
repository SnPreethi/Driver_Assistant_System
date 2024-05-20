# Driver Assistant System - Major Project 2024

### TABLE OF CONTENTS
- [Problem Statement](https://github.com/SnPreethi/Driver_Assistant_System/blob/main/README.md#problem-statement)
- [Solutions](https://github.com/SnPreethi/Driver_Assistant_System/blob/main/README.md#solutions)
- [Overview of the Project](https://github.com/SnPreethi/Driver_Assistant_System/blob/main/README.md#overview-of-the-project)
- [Project Background](https://github.com/SnPreethi/Driver_Assistant_System/blob/main/README.md#project-background)
- [Hardware Requirements](https://github.com/SnPreethi/Driver_Assistant_System/blob/main/README.md#hardware-requirements)
- [Software Requirements](https://github.com/SnPreethi/Driver_Assistant_System/blob/main/README.md#software-requirements)
- [Workflow of the System](https://github.com/SnPreethi/Driver_Assistant_System/blob/main/README.md#workflow-of-the-system)
- [Results Adapted for Indian Scenarios](https://github.com/SnPreethi/Driver_Assistant_System/blob/main/README.md#results-adapted-for-indian-scenarios)
- [References](https://github.com/SnPreethi/Driver_Assistant_System/blob/main/README.md#references)

### PROBLEM STATEMENT
<p align="justify">Addressing the conversations around road safety is one of the important concerns in today's modern society. Despite remaining as a central topic in the discussions on safety and public welfare, millions worldwide continue to lose their lives or suffer injuries in road accidents due to human error, road and vehicular conditions, or environmental factors.</p>

### SOLUTIONS
<p align="justify">Improving road safety is a multifaceted approach. It involves the implementation and usage of better technology, improved infrastructure, strict enforcement of traffic laws, and increasing public awareness. In terms of technology in autombiles, Advanced Driver Assistant Systems (ADAS) are emerging as a promising frontier in the quest for safer roads. It holds the potential to revolutionalize vehicle safety by providing drivers with critical insights and assistance in navigating complex road scenarios.</p>

### OVERVIEW OF THE PROJECT
<p align="justify">
With a particular focus on the Indian context, this project -  'Driver Assistant System' monitors both the external and internal environments, trying to shed light on the following modules.<ol>
<li>Drowsiness Detection</li>
<li>Lane Detection</li>
<li>Lane Departure Warning</li>
<li>Lane Keeping Assistance</li>
<li>Object Detection and Recognition; and</li>
<li>Collision Warning</li>
</ol></p>

## PROJECT BACKGROUND
<p align ="justify">The "Driver Assistant System" is developed by Preethi Somayajula and team as a part of an academic requirement in B.Tech CSE (AIML). It aims to demonstrate the practical application of theoretical knowledge gained during the course of study. All the results presented within this repository were generated during the development phase of this project.<br></p>

Some of the other details regarding the above mentioned content are listed below.<br>
<ol>
<li>Team Number - 10</li>
<li>Institution - MLR Institute of Technology</li>
<li>Team members - Preethi Somayajula, Madadapu Hemanth Sai, M. Sai Krishna, Vemuri Abhinaya </li>
</ol>

## SYSTEM REQUIREMENTS AND ARCHITECTURE
### HARDWARE REQUIREMENTS
<p align="justify">
Listed below are the primary hardware components utilized in building the prototype, along with their significance.<ul>
<li>Jetson Orin Nano: Primary processing unit for efficient computation and analysis.</li>
<li>Raspberry Pi Camera Module 3: Captures video footage for monitoring internal and external environments.</li>
<li>ADXL-345 Accelerometer: Detects sudden movements or impacts indicative of drowsiness events.</li>
<li>Arduino Nano: Manages sensor interfacing and control tasks.</li>
<li>GSM SIM800I Module: Facilitates communication for sending texts and making calls.</li>
<li>GSM Neo-6m Module: Provides accurate geographic positioning information.</li>
<li>LM2596 Step-down converter: Regulates voltage levels for consistent power delivery.</li>
<li>Zero PCB: Houses and organizes electronic components.</li>
<li>15 pin to 22 pin cable: Establishes connections between components and subsystems.</li>
<li>Power bank(10000 to 20000 mAh): Provides portable power source for continuous operation.</li>
<li>External Speaker: Provides audio feedback or alerts as needed.</li>
</ul>
Below is the block diagram of interconnection of the various hardware components.</p>

<div align="center">

 ![Block Diagram](https://github.com/SnPreethi/Driver_Assistant_System/assets/170320349/c5c38bc3-ceb4-48f7-bdf6-5594a26cc85b)

</div>

### SOFTWARE REQUIREMENTS
<p align="justify">
The software requirements for this project are listed below.<ul>
<li>addict</li>
<li>numba</li>
<li>scipy</li>
<li>pycuda</li>
<li>torchsummary</li>
<li>onnx (version 1.12.0)</li>
<li>onnxruntime (version 1.12.0)</li>
<li>opencv-python (version 4.5.4.60)</li>
<li>torch (version 1.11.0+cu113)</li>
<li>torchvision (version 0.12.0+cu113)</li>
<li>torchaudio (version 0.11.0)</li>
<li>YOLO v8</li>
<li>ultrafast lane detector v2</li>
<li>imutils</li>
<li>pygame</li>
<li>Jetson Orion Nano Software Development Kit (SDK)</li>
<li>Python 3.7+</li>
<li>OpenCV</li>
<li>Scikit-learn</li>
<li>Dlib</li>
<li>ADXL-345 Sensor Library</li>
<li>SIM800I GSM Module Library</li>
<li>NeoGPS Library</li>
</ul>
</p>

### WORKFLOW OF THE SYSTEM
<div align="center">
  
![Final_Overall_Workflow](https://github.com/SnPreethi/Driver_Assistant_System/assets/170320349/4bb481d4-5d7f-499b-a06c-373fa68b8343)

</div>


## RESULTS ADAPTED FOR INDIAN SCENARIOS

<p align="justify">
The Driver Assistant System was tested in various scenarios, both during the day and at night, to evaluate its performance in real-time monitoring and driver assistance. Some of the outputs generated are captured in the form of videos and images, which can be accessed above. The comprehensive integration of several modules allows the system to monitor both external and internal environments simultaneously. Despite its shortcomings, this project represents a significant step toward the development of more robust driver assistance systems. Below are a few sample images collected during the testing of this project.
</p>

### EXTERNAL ENVIRONMENT
<div align="center">
<img src="https://github.com/SnPreethi/Driver_Assistant_System/assets/170320349/3acba733-1a94-4188-a237-422a924b9eef" width ="500" />
</div>

### INTERNAL ENVIRONMENT
<div align ="center">
  <img src="https://github.com/SnPreethi/Driver_Assistant_System/assets/170320349/15dfb3c7-5661-4987-81d5-e597317282b9" width="300" hspace="10" />
  <img src="https://github.com/SnPreethi/Driver_Assistant_System/assets/170320349/f9fce1ba-869d-4b37-a30c-a1ce72cb07f7" width="300" />
</div>

## REFERENCES
- [Lane detection](https://github.com/jason-li-831202/Vehicle-CV-ADAS)
- [ultrafast lane detection](https://github.com/cfzd/Ultra-Fast-Lane-Detection-v2)
- [Drowsiness Detection](https://github.com/akshaybahadur21/Drowsiness_Detection)
- [YOLO v8](https://github.com/rigvedrs/YOLO-V8-CAM) 
