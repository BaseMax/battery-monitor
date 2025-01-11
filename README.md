# Battery Monitor

**Battery Monitor** is a Python script that displays battery information on your system in a user-friendly format. It shows the battery percentage, charging status, time left, and battery health, with colored output to improve readability. The script works across multiple platforms including Windows, macOS, and Linux.

### Features

- Cross-platform support (Windows, macOS, Linux)
- Displays battery percentage, charging status, and time left
- Provides battery health status with color-coded outputs
- Clear and visually appealing terminal output similar to `screenfetch`

### Output Example

```bash
==============================
   Battery Monitor   
==============================
System: Windows 11
Machine: AMD64
Processor: Intel64 Family 6 Model 142 Stepping 10, GenuineIntel
==============================
Battery Percentage: 100%
Plugged In: Yes
Charging: Yes
Time Left: Charging
Battery Health: Healthy
==============================
Powered by Battery Monitor (github.com/basemax)
```

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/BaseMax/battery-monitor.git
    cd battery-monitor
    ```

2. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Requirements

- Python 3.x
- `psutil` library for fetching battery status
- `termcolor` library for colored output

You can install the required libraries by running:

```bash
pip install psutil termcolor
```

### Usage

To run the script, simply execute:

```bash
python battery-monitor.py
```

This will display your battery information in a clean, user-friendly format.

### File Structure

```
battery-monitor/
├── LICENSE
├── README.md
├── battery-monitor.py
├── requirements.txt
└── .git/
```

### License

MIT License.

Copyright 2025, Max Base
