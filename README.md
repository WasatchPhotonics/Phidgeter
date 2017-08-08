Phidgeter - logging, network, display and convenience functions for
Phidgets.

Usage:

Work with relays:

    from phidgeter import relay

    phd_relay = relay.Relay()
    phd_relay.one_toggle()
    phd_relay.two_on()

Emit data from a Phidget IR sensor on the command line:
   
    python scripts/ir_demo.py

Visualize the data with the [BlueGraph] (https://github.com/WasatchPhotonics/BlueGraph "BlueGraph package"):

    python scripts/TempGraph.py

![BlueGraph Screenshot] (/docs/IR_Temp_BlueGraph.gif "IR Temp BlueGraph screenshot")


Setup on Fedora Core:

    Make sure to use libphidgets-2.1.8 and PhidgetsPython 2.1.8

    cd ~/Downloads/libphidget*/
    ./configure
    sudo make && sudo make install

    cd ~/Downloads/PhidgetsPython
    sudo python setup.py install

Make phidget devices available to all users
    cd ~/Downloads/libphidget/udev/
    sudo cp 99-phidgets.rules /etc/udev/rules.d/

    Unplug and re-plug device.
