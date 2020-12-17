# Pipowermeter
Measure DC power out of a solar panel or a wind turbine with raspberry pi zero W using a DFrobot SEN0291 I2C wattmeter module to evaluate its efficiency.

## Features

- Continuously measure power
- Set the periodicity of the measurement (in minutes)
- Generate .csv files
    - Append one line for every measure
    - Device name | date/time | value (w) | [ optional weather infos via openweathermap ]
- OpenWeathermap infos (you need an internet connection)
    - Temperature (°C) | Wind speed (Km/h) | Cloudiness (%)

### Don't forget to use a resistor to dissipate the power !

## Usage

The installer is setting up a service that will continuously take the measure. If for any reason the pi is shut down or the service is stopped, this service will automatically restart, preventing the measurement ton stop.

The csv files will be stored in the data directory inside the current directory. They are named using the patern : [Device name]_[YYYYmmddHHmm].csv using the starting date/time of the measure. 

Stopping the measure will not erase those files.

Starting, stopping, installing and uninstalling via :
```bash
./install.py
```

