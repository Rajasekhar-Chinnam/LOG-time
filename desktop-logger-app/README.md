# Desktop Logger App

## Overview
The Desktop Logger App is a Python application designed to automatically log user login and logout times, as well as track idle time. This application starts automatically when the system boots up, providing seamless tracking of user activity.

## Features
- Logs user login and logout times.
- Tracks idle time when the user is inactive.
- Automatically starts on system boot.

## Project Structure
```
desktop-logger-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── logger.py        # Handles logging of user activity
│   ├── startup.py       # Configures the application to start on boot
│   └── idle_tracker.py   # Monitors user activity and calculates idle time
├── requirements.txt     # Lists project dependencies
└── README.md            # Documentation for the project
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd desktop-logger-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python src/main.py
   ```
2. The application will log your login and logout times and track idle time automatically.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.