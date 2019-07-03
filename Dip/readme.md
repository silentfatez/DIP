the files are to be uploaded to their respective pins.
for pin 2 and 4 there are seperate python files to play the vids via command line
All folders contain autoplay code so that it is able to boot up a continuos video on startup.
use the videos in media folder or change the code to use your own videos.

https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/all
use the above link to understand how to autoplay videos. For this project we used autostart which is method 2.

Basically pin 1 is the master pin to call the functions in all other pins.

This project was done in china which caused some functionality to be reduced.

It is possible to use firebase as a real time database in order to continuously check if the values have changed and if it has we are
able to sync the videos to play together
however due to limitations we have come up with a substitute using ssh but that has provided delays and the inability to scale
the project to using more pins.

May have to research more on databases in china.
