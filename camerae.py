import os
import imageio as io
from PIL import Image

def capture():

    os.system("fswebcam -d /dev/video0 -r 1280x960 -S 4 /home/pi/supinger/images/1a.jpg")
    os.system("sudo fswebcam -d /dev/video2 -r 1280x960 -S 4 /home/pi/supinger/images/1b.jpg")

    os.system("fswebcam -d /dev/video0 -r 1280x960 -S 4 /home/pi/supinger/images/2a.jpg")
    os.system("sudo fswebcam -d /dev/video2 -r 1280x960 -S 4 /home/pi/supinger/images/2b.jpg")

    os.system("fswebcam -d /dev/video0 -r 1280x960 -S 4 /home/pi/supinger/images/3a.jpg")
    os.system("sudo fswebcam -d /dev/video2 -r 1280x960 /home/pi/supinger/images/3b.jpg")

    os.system("fswebcam -d /dev/video0 -r 1280x960 -S 4 /home/pi/supinger/images/4a.jpg")
    os.system("sudo fswebcam -d /dev/video2 -r 1280x960 -S 4 /home/pi/supinger/images/4b.jpg")

    os.system("fswebcam -d /dev/video0 -r 1280x960 -S 4 /home/pi/supinger/images/5a.jpg")
    os.system("sudo fswebcam -d /dev/video2 -r 1280x960 -S 4 /home/pi/supinger/images/5b.jpg")

    os.system("fswebcam -d /dev/video0 -r 1280x960 -S 4 /home/pi/supinger/images/6a.jpg")
    os.system("sudo fswebcam -d /dev/video2 -r 1280x960 -S 4 /home/pi/supinger/images/6b.jpg")

    os.system("fswebcam -d /dev/video0 -r 1280x960 -S 4 /home/pi/supinger/images/7a.jpg")
    os.system("sudo fswebcam -d /dev/video2 -r 1280x960 -S 4 /home/pi/supinger/images/7b.jpg")

    os.system("fswebcam -d /dev/video0 -r 1280x960 -S 4 /home/pi/supinger/images/8a.jpg")
    os.system("sudo fswebcam -d /dev/video2 -r 1280x960 /home/pi/supinger/images/8b.jpg")

    os.system("fswebcam -d /dev/video0 -r 1280x960 -S 4 /home/pi/supinger/images/9a.jpg")
    os.system("sudo fswebcam -d /dev/video2 -r 1280x960 -S 4 /home/pi/supinger/images/9b.jpg")

    os.system("fswebcam -d /dev/video0 -r 1280x960 -S 4 /home/pi/supinger/images/10a.jpg")
    os.system("sudo fswebcam -d /dev/video2 -r 1280x960 -S 4 /home/pi/supinger/images/10b.jpg")

    camera_a_snaps = []
    camera_b_snaps = []

    entries = os.listdir("/home/pi/supinger/images/")

    print(entries)

    for file in entries:

        if 'a' in file:
            print(file)
            im = Image.open("/home/pi/supinger/images/"+file)
            camera_a_snaps.append(im)
        elif 'b' in file:
            im = Image.open("/home/pi/supinger/images/"+file)
            camera_b_snaps.append(im)


    camera_a_snaps[0].save('/home/pi/supinger/images/product/angle1.gif',
                   save_all=True, append_images=camera_a_snaps[1:], optimize=True, duration=100, loop=0, quality=1)

    camera_b_snaps[0].save('/home/pi/supinger/images/product/angle2.gif',
                   save_all=True, append_images=camera_b_snaps[1:], optimize=True, duration=100, loop=0, quality=1)
#capture()

    
