# Pipowermeter
Measure DC power out of a solar panel or a wind turbine with any model of raspberry pi using a DFrobot SEN0291 I2C wattmeter module to evaluate power efficiency.
Produces CSV files to be able to make statistics over a long period of time.

## Features

- Continuously measure power
- Set the periodicity of the measurement (in minutes)
- Generate .csv files
    - Append one line for every measure
    - date/time (yyyymmddhhmmss) | Device name | Device location | date/time (Human readable) | value (w) | consommation (since last measure, Wh) [ optional weather infos via openweathermap ]
- OpenWeathermap infos (you need an internet connection)
    - Temperature (°C) | Wind speed (Km/h) | Cloudiness (%)

### Don't forget to use a resistor to dissipate the power !

## Usage


```bash
git clone https://github.com/romaindudek/pipowermeter.git
```

The installer is setting up a service that will continuously take the measure. If for any reason the pi is shut down or the service is stopped, this service will automatically restart, preventing the measurement ton stop.

The csv files will be stored in the data directory inside the current directory. They are named using the patern : [Device name]_[YYYYmmddHHmm].csv using the starting date/time of the measure. 

Stopping the measure will not erase those files.

App installation and instructions via :
```bash
./setup.py
```

