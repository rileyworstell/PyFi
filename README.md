This is the PyFi Application!!
This ia a Command Line Interface Application.
If you want to take a look at the code I recommend starting with the PyFi.py file!

This application allows you to enter monthly expenses and monthly income and will
tell you how long it will take you to reach your investing goals!! ^-^

## How to run:

You can build this through docker!!
To build this image pull down this branch and in your terminal run:
`docker build --tag=pyfi:tag .`
To run the image:
`docker run --rm -it pyfi:tag`

NOTE: If you run this using docker, as of now we have not supported showing graphs from the docker container.

If you don't want to run this using docker, you can open up your terminal to the pulled repository and run `python PyFi_cli.py` .

## How to test:

You can test this project by running the test_PyFi.py file.
Feel free to add any tests as you see fit!

## requirements.txt

As of now this file is empty, but as this project expands any libraries will be put in this file
