# openhsi
Module to Use the USYD OpenHSI.

## openhsi.py class
Wrapper class and example code for getting images from the OpenHSI using a ximea detetor (with IMX252 sensor, e.g. [MX031CG-SY](https://www.ximea.com/en/products/xilab-application-specific-custom-oem/embedded-vision-and-multi-camera-setup-xix/sony-imx252-fast-color-industrial-camera)).

## Spectral Calibration
Draft of proccess to calibrate wavelength scale for the sensor.


# Setup

## Requirements

* Python 3.6+
* ximea sdk installed

## Installation
Ensure Ximea SDK is installed first. See https://www.ximea.com/support/wiki/apis/Python

### To install openhsi package
`pip3 install git+https://github.com/SydneyAstrophotonicInstrumentationLab/openhsi`

### To upgrade in place
`pip3 install --upgrade --no-deps --force-reinstall  git+https://github.com/SydneyAstrophotonicInstrumentationLab/openhsi`
