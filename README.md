# Dev Logs

Configuring rpi through HDMI monitor, mouse and keyboard. The rpi has a wifi 
and bluetooth dongle and runs Rasbian on a 8GB SD card.  

HDMI revieved no signal so we opened the `config.txt` from the SD card throgh an
SD card reader. On the file added the following lines:  

``` 
hdmi_force_hotplug=1
hdmi_drive=2
``` 

We'll be connecting through SSH so we setup Raspbian with our Wifi network. All 
other configs will happen through SSH.

## Connect to through SSH

The challenge is getting the ip for which there are various options. What works 
best for me is to access my router and get the list of DHCP clients; client is 
called raspberrypi.

```
ssh pi@<raspberrypi-ip>
pi@192.168.0.18's password: raspberry
``` 

After you've logged in update your system:

```
sudo apt-get update
sudo apt-get upgrade 
```

## Configure HDMI Touchscreen (optional)

As an optional step we configured a Waveshare 5inch touchscreen HDMI to improve 
user interaction. The process is straight forward and can be followed at 
[waveshare](http://www.waveshare.com/wiki/5inch_HDMI_LCD).

## Testing with 16 channel Adafruit HAT

This is not the hat we'll be using but considering we have this one and there is 
better docs for it we'll run tests on this one first. The main reason to not use 
this module is that we'll be controlling two geared motors not servos.

## Configure I2C

>The I2C bus allows multiple devices to be connected to your Raspberry Pi, each 
with a unique address, that can often be set by changing jumper settings on the 
module. It is very useful to be able to see which devices are connected to your 
Pi as a way of making sure everything is working.

1. Install i2c tools and smbus.

```
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
```

2. Run `sudo raspi-config` and under advanced options choose i2c and enable it. 
3. Reboot
4. Add i2c modules

``` 
# /etc/modules
i2c-bcm2708 
i2c-dev
``` 

5. Make sure we don't have i2c or spi blacklisted at 
`/etc/modprobe.d/raspi-blacklist.conf`.

6. Test with `sudo i2cdetect -y 1`. You should get a table with any pins that 
you are using mapped on it. 

Follow this Adafruit [guide](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) 
for more details.

## Adafruit Python Library


## External resources
*  http://blog.mivia.dk/solved-hdmi-working-raspberry-pi/ 
*  https://www.raspberrypi.org/downloads/raspbian/ 
*  https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c 
*  https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/attach-and-test-the-hat 
*  https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md
*  http://www.waveshare.com/wiki/5inch_HDMI_LCD 
*  https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code