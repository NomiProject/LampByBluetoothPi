<img src="http://www.pngmart.com/files/3/Bluetooth-PNG-Transparent-Picture.png" width="48">

# LampByBluetoothPi
Control the I/O (like a lamp through a relay) pin of Raspberry Pi from a Client-Server Bluetooth application

### Requirements

1. **Python 2.7 or 3.6**
    Download Python interpreter [here](https://www.python.org/).

2. **Raspberry Pi 3 Model B**
    Learn more about [RasberryPi project](https://www.raspberrypi.org/).

3. **PyBluez and Bluetooth support**
    ```bash
    sudo apt-get install python-pip python-dev ipython bluetooth libbluetooth-dev
    ```
    And then:
    ```bash
    sudo pip install pybluez
    ```

### Setup

1. Clone the repo (In your PC *and* RaspberryPi)

    ```bash
	$ git clone https://github.com/NomiProject/LampByBluetoothPi.git
	$ cd LampByBluetoothPi/
	```

2. **In your RasberryPi**, with bluetooth enabled, run:

    ```bash
    $ python server.py
    ```

    - Note: Opening `server.py`, you can change GPIO pin

2. **In your PC**, with bluetooth enabled, run:

    ```bash
    $ python client.py -s OPTION
    ```
    - Note 1: *OPTION* can be: **on**, **off** or **exit**;
    - Note 2: Opening `client.py`, you can change Raspberry MAC address or uncomment some lines to search new devices 

---

Developed by [Allex Lima](http://allexlima.com), [Daniel Bispo](https://github.com/danielbispov/), [Paulo Moraes](http://www.moraespaulo.com/) and [Renan Barroncas](https://github.com/renanbarroncas) with ❤️ using [Python](https://www.python.org/).
###### Copyright © 2017 [LampByBluetoothPi](https://github.com/NomiProject/LampByBluetoothPi.git) - Licensed by MIT LICENSE.
