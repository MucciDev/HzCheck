#HzCheck  
HzCheck is a Python library that provides various tools for retrieving information about a network and its devices. It was created to help people get network information using Python.

I started this project just two days ago, and I've already added a bunch of useful functions that allow you to get information such as the WiFi name, the devices connected to the WiFi, the IP addresses of devices, and more.

#Installation
To install HzCheck, simply use pip:

"pip install hzcheck"

#Usage
Here's an example of how to use the library to get the WiFi name and the devices connected to it:

import hzcheck

wifi_name = hzcheck.get_wifi_name()
print(f'WiFi name: {wifi_name}')

devices = hzcheck.get_connected_devices()
print(f'Connected devices: {devices}')
You can find more detailed documentation for each function in the library in the documentation file.

#Contributing
If you'd like to contribute to the project, please feel free to open a pull request on GitHub.

#License
This project is licensed under the MIT License - see the LICENSE file for details.
