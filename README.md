I. Background.
There are many ways to capture perpetrators trespassing property lines such as buildings
and vehicles. In this case, this is one that allows it to be modified using software and hardware
components while other systems are compact, making it exceedingly difficult to expand or
modify. There are many options that are obviously more reliable than the one developed in this
study.

II. Challenges
The Raspberry PI 3 1.2 offers an array of GPIO pins that allows the implementation of
electrical components with 2 on board serial interfaces (one is designed for the Picamera) with
its own independent transfer speed. The operating system designed for the Raspberry PI used to
be Raspbian which allowed the usage of the Picamera with Python’s picamera library from its
inherent support. This operating system, however, became deprecated because a few months ago,
Raspberry PI OS became the official system for the Raspberry PI devices. This change created
driver issues with some of the Python libraries; the picamera library for python did not work as
intended.
The OS change for the computer device opened certain opportunities to work around the
issue. The Picamera was expunged from the blueprint. This led to the implementation of two
USB webcams into the system. The limitation of using these two stream devices was the USB
transfer speed bus is limited to approximately 400 Mbps, and Python’s opencv library did not
recognize these two cameras simultaneously. The simultaneous streaming of two USB webcams
became out of the question for this system.

III. Resolution
Since these challenges made the original implementation of the system a relatively
impossible task, the solution to solve this problem would be by calling USB webcam shell
commands from the Python script in an alternating manner. Webcam 1 shoots a photo then
followed by Webcam 2, 10 times. After the shooting procedure completes, these photos taken by
each camera were joined into correspondent GIF files.

IV. Workflow
The perpetrator triggers the PIR motion sensor. After the trigger, the USB webcams will
alternately take pictures 10 times each for each to capture the trespasser. Once the snapshots are
taken, these will be converted into an array that converts these into a GIF file. Finally these
corresponding GIFs will be used as attachments for an e-mail sent with the SMTP protocol as the
output of the triggering event.

