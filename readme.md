# Python mqtt script to serve clapToLightUp iot project

This script reads the "do not disturb" time from mqtt broker and publishes 'True' if the current time belongs to the given interval, 'False' otherwise.