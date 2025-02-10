# EnviroBot: Smart Obstacle Avoidance and Climate Monitoring
## Code Files

### Obstacle Avoidance - `obs_avoid.ino`
- **Description:** This Arduino code file manages the obstacle avoidance functionality of the smart vacuum cleaner.
- **Functionality:** Uses the ultrasonic sensor to detect obstacles and controls the DC motors to navigate around them.

### Temperature, Humidity, Heat Index, and Motion Detection - `main.py`
- **Description:** This Python script runs on a Raspberry Pi Pico to measure environmental conditions and detect motion.
- **Functionality:** Utilizes sensors to collect data on temperature, humidity, and motion, then processes and stores this data in Firebase.

### Temperature Prediction - `app.py`
- **Description:** This Python application predicts future temperature trends based on historical data.
- **Functionality:** By running `python app.py`, users can access a web interface that provides temperature predictions and insights.
## Table of Contents
- [Motivation](#motivation)
  - [Efficiency Boost](#efficiency-boost)
  - [Time-Saving](#time-saving)
  - [Safety Assurance](#safety-assurance)
  - [Technology Showcase](#technology-showcase)
- [Objectives](#objectives)
  - [Versatile Robotic Vehicle](#versatile-robotic-vehicle)
  - [Remote Control Functionality](#remote-control-functionality)
  - [Obstacle Avoidance Algorithms](#obstacle-avoidance-algorithms)
  - [Automatic Cleaning System](#automatic-cleaning-system)
- [Deliverables](#deliverables)
  - [Robotic Vehicle](#robotic-vehicle)
  - [Mobile App](#mobile-app)
  - [Safety Sensors](#safety-sensors)
  - [Cleaning System](#cleaning-system)
  - [Voice Control](#voice-control)
  - [Demo and Instructions](#demo-and-instructions)
- [Sensors Used](#sensors-used)
  - [Intruder Detection Timestamp](#intruder-detection-timestamp)
  - [Temperature, Heat Index, and Humidity Data](#temperature-heat-index-and-humidity-data)
  - [Usefulness of Timestamps](#usefulness-of-timestamps)
  - [Usefulness of Temperature, Heat Index, and Humidity Data](#usefulness-of-temperature-heat-index-and-humidity-data)
- [Smart Vacuum Cleaner Project - Simulation Setup](#smart-vacuum-cleaner-project---simulation-setup)
  - [Components and Connections](#components-and-connections)
    - [2 DC Motors with Mega Arduino](#2-dc-motors-with-mega-arduino)
    - [Mega Arduino with Ultrasonic Sensor](#mega-arduino-with-ultrasonic-sensor)
    - [Mega Arduino with Servo Motor](#mega-arduino-with-servo-motor)
    - [Mega Arduino with L298N](#mega-arduino-with-l298n)
    - [Mega Arduino with Humidity Sensor](#mega-arduino-with-humidity-sensor)
    - [Mega Arduino with Motion Sensor](#mega-arduino-with-motion-sensor)
- [Predicting Temperature](#predicting-temperature)
- [Summary](#summary)

## Motivation

### Efficiency Boost
We're responding to the growing need for simplifying daily chores by automating cleaning tasks.

### Time-Saving
Automating cleaning tasks saves time and physical effort, freeing up more time for leisure or other productive activities.

### Safety Assurance
Our autonomous obstacle avoidance ensures safer navigation, reducing the chances of accidents, especially in dynamic or low-visibility environments.

### Technology Showcase
This project demonstrates the power of robotics and automation, inspiring further advancements and innovations in the field.

## Objectives

### Versatile Robotic Vehicle
Create a robot that can be controlled manually or drive by itself, adapting to different needs.

### Remote Control Functionality
Develop a phone app to control the robot from anywhere easily.

### Obstacle Avoidance Algorithms
Teach the robot to see and avoid obstacles automatically, ensuring safe movement.

### Automatic Cleaning System
Incorporate a vacuum cleaner into the robot to autonomously clean surfaces, saving time and effort.

## Deliverables

### Robotic Vehicle
A smart vehicle capable of autonomous navigation or remote control.

### Mobile App
An intuitive phone app to control the vehicle remotely.

### Safety Sensors
Built-in sensors for obstacle avoidance and safe navigation.

### Cleaning System
A vacuum system that automatically cleans floors and surfaces.

### Voice Control
Voice command functionality for convenient control.

### Demo and Instructions
A demonstration of the system's capabilities along with clear user instructions.

## Sensors Used

### Intruder Detection Timestamp
Firebase records the time of intrusion detection, providing crucial information for security monitoring. Knowing the exact time of intrusion allows for timely response and potential investigation.

### Temperature, Heat Index, and Humidity Data
Firebase stores real-time temperature, heat index, and humidity readings, offering insights into environmental conditions. This data is essential for maintaining comfort levels and optimizing the cleaning process. For example, if the temperature rises above a certain threshold, the vacuum cleaner may adjust its cleaning schedule to avoid overheating components.

### Usefulness of Timestamps
Timestamps allow for precise event tracking, facilitating analysis of intrusion patterns over time. By identifying recurring intrusion times, users can implement additional security measures during vulnerable periods.

### Usefulness of Temperature, Heat Index, and Humidity Data
Real-time environmental data enables users to monitor indoor conditions remotely and make informed decisions. For instance, if the humidity level becomes too high, indicating poor air quality, users can take steps to improve ventilation or activate air purifiers. Additionally, the heat index helps assess perceived temperature, aiding in comfort management and potentially reducing energy consumption by adjusting heating or cooling systems accordingly.

## Smart Vacuum Cleaner Project - Simulation Setup

### Components and Connections

#### 2 DC Motors with Mega Arduino
![2 DC Motors](https://github.com/Leonallr10/IOT_obstacles-avoidance-/assets/118210551/d87b274b-c8ed-4152-9010-882ba625b36f)
- **Description:** This setup involves connecting two DC motors to the Mega Arduino for the propulsion and movement of the robotic vacuum cleaner.
- **Usage:** Enables the vacuum cleaner to navigate and move around the cleaning area.

#### Mega Arduino with Ultrasonic Sensor
![Ultrasonic Sensor](https://github.com/Leonallr10/IOT_obstacles-avoidance-/assets/118210551/6530ab50-92c0-4264-9db6-cc679fa31202)
- **Description:** The ultrasonic sensor is connected to the Mega Arduino to detect obstacles in the vacuum cleaner’s path.
- **Usage:** Facilitates obstacle avoidance by measuring distance and preventing collisions.

#### Mega Arduino with Servo Motor
![Servo Motor](https://github.com/Leonallr10/IOT_obstacles-avoidance-/assets/118210551/f4a5417a-4b19-407a-a6b4-e62f1f2509b3)
- **Description:** This setup includes a servo motor connected to the Mega Arduino for precise control of components, such as adjusting the angle of the vacuum cleaner’s nozzle.
- **Usage:** Enhances cleaning efficiency by allowing precise adjustments.

#### Mega Arduino with L298N
![L298N Motor Driver](https://github.com/Leonallr10/IOT_obstacles-avoidance-/assets/118210551/8bbb1228-d3a7-4335-979c-0734c6b9ab78)
- **Description:** The L298N motor driver is used to control the DC motors. It interfaces with the Mega Arduino to manage motor speed and direction.
- **Usage:** Ensures efficient motor control and provides the necessary power for movement.

#### Mega Arduino with Humidity Sensor
![Humidity Sensor](https://github.com/Leonallr10/IOT_obstacles-avoidance-/assets/118210551/b80d1936-c451-4043-8f0a-e365ecbaf27a)
- **Description:** The humidity sensor is connected to the Mega Arduino to measure the humidity levels in the environment.
- **Usage:** Monitors environmental conditions to maintain optimal cleaning performance and comfort.

#### Mega Arduino with Motion Sensor
![Motion Sensor](https://github.com/Leonallr10/IOT_obstacles-avoidance-/assets/118210551/2ff5d36a-0ef7-4883-87da-7a69654ccce7)
- **Description:** This setup includes a motion sensor connected to the Mega Arduino to detect movement in the area.
- **Usage:** Enhances security by detecting intruders and can adjust cleaning schedules based on room occupancy.

## Predicting Temperature

Additionally, we have added a prediction page to forecast future climate temperature. By running the code `python app.py`, users can access the prediction page and get insights into upcoming temperature trends.

## Summary
The smart vacuum cleaner integrates multiple components with the Mega Arduino to achieve autonomous cleaning, obstacle avoidance, environmental monitoring, and security features. This comprehensive setup demonstrates the power of robotics and automation in everyday applications, providing both efficiency and convenience.

## Sample data - for login
`Username`: `leonal`

`password`: `123456`
