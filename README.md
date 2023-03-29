Modular Motion Detection and Notification System Using the Raspberry PI

José Antonio Ruiz-Ramón

Supervised by: Dr. Fernando González

December 9, 2021

![image](https://user-images.githubusercontent.com/21689731/228671567-dd040e9c-5351-425b-87c8-40b6cdf1d6a7.png)


I. Background

There are various ways to capture perpetrators who trespass on property lines, such as buildings and vehicles. This study presents a method that can be modified using software and hardware components. While other systems may be more compact and reliable, they can also be challenging to expand or modify.

II. Challenges

The Raspberry PI 3 1.2 offers an array of GPIO pins that enable the implementation of electrical components, including two onboard serial interfaces (one designed for the Picamera) with independent transfer speeds. The operating system formerly used for the Raspberry PI was Raspbian, which allowed the usage of the Picamera with Python's picamera library due to its inherent support. However, this operating system became deprecated a few months ago when Raspberry PI OS became the official system for Raspberry PI devices. This change caused driver issues with some Python libraries, and the picamera library for Python did not function as intended.

The OS change for the computer device provided certain opportunities to work around this issue. The Picamera was removed from the blueprint, and two USB webcams were implemented into the system instead. However, the limitation of using these two stream devices was that the USB transfer speed bus is limited to approximately 400 Mbps, and Python's opencv library did not recognize these two cameras simultaneously. Therefore, the simultaneous streaming of two USB webcams was not possible for this system.

III. Resolution

Since these challenges made the original implementation of the system relatively impossible, the solution to this problem was to call USB webcam shell commands from the Python script in an alternating manner. Webcam 1 takes a photo, followed by Webcam 2, 10 times. After the shooting procedure is complete, the photos taken by each camera are joined into corresponding GIF files.

IV. Workflow

When a perpetrator triggers the PIR motion sensor, the USB webcams will alternately take 10 photos each to capture the trespasser. Once the snapshots are taken, they are converted into an array that is used to create GIF files. These corresponding GIFs are then used as attachments for an email sent with the SMTP protocol as the output of the triggering event.

