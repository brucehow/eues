# Episodic Ultradian Events  &middot; [![Python 3.7.2](https://img.shields.io/badge/python-3.7.2-blue.svg)](https://www.python.org/downloads/release/python-372/)

This project was proposed by Dr Dominique Blache and focuses on near-real-time analysis of episodic ultradian events (EUEs) in body temperature profiles.

This software package processes raw data generated by telemetric systems that can in near-real-time detect EUEs of temperature and store the characteristics of the detected EUEs. As the shape of EUEs can vary, the software offers options to test different mother wavelets and validates their best fit.

## Application Structure
The application structure is based on Jean-Paul Calderone's Filesystem structure of a Python project. The application structure and explainations are as below:
```
eues
├── LICENSE
├── README.md
└── core
    ├── gui                         <-- GUI package for interface
    │   └── __init.py__
    ├── kernel                      <-- Kernal package for data handling
    │   ├── __init.py__
    │   ├── get_features.py         <-- Wavelet characteristic functions
    │   ├── reconstruct.py          <-- Data preprocessing and reconstruction
    │   └── visualise_features.py
    ├── tests                       <-- Test package for unit testing
    │   └── __init.py__
    └── main.py                     <-- Main application module
```

## Authors
- [Bruce How](https://github.com/brucehow)
- [Kristian Tricoli](https://github.com/KristianTricoli)
- [Jeremy Quinlivan](https://github.com/JXQuinlivan)
- [Ramsey Fu](https://github.com/RamseyTwT)
- [Aimon Wong](https://github.com/aimonh)

## License

This project is licensed under the [MIT License](https://github.com/brucehow/eues/blob/master/LICENSE).
