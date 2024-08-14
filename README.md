# Employee Punching System using Face Recognition

## Overview

This project is an Employee Punching System that leverages advanced face recognition technology to simplify attendance tracking. The system uses **OpenCV** for facial recognition, **HarCascade** for face detection, and **Streamlit** for a sleek interface. It efficiently records punch-ins with a single press of 'O' and logs the data into a CSV file, ensuring accurate records with the help of the datetime package.

## Features

- **Face Detection & Recognition:** Utilizes OpenCV and HarCascade to detect and recognize employee faces.
- **Attendance Logging:** Logs punch-in details such as name and timestamp into a CSV file.
- **Speech Feedback:** Uses the Windows SAPI to provide verbal confirmation of attendance.
- **Streamlit Integration:** Displays the attendance records in a user-friendly interface.
- **Customizable Background:** Includes an option to display the captured video feed on a custom background.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- scikit-learn
- pandas
- Streamlit
- win32com.client

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/employee-punching-system.git
    cd employee-punching-system
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure the `dataset/faces_data.pkl` and `dataset/labels.pkl` files exist in the dataset directory. These files contain the face data and corresponding labels.

4. Place the `haarcascade_frontalface_default.xml` file in the `model/` directory.

## Usage

1. Run the script to start the face recognition and attendance system:
    ```bash
    python employee_punching_system.py
    ```

2. The system will start capturing video from the webcam. Press 'O' to log attendance and 'Q' to quit.

3. Attendance will be saved in a CSV file under the `Attendance` directory with the format `Attendance_<date>.csv`.

4. To view the attendance records using Streamlit, run:
    ```bash
    streamlit run view_attendance.py
    ```

## Project Structure

- `employee_punching_system.py`: Main script to run the face recognition and attendance system.
- `view_attendance.py`: Script to view attendance records using Streamlit.
- `dataset/`: Directory containing the face data and labels.
- `model/`: Directory containing the face detection model.
- `Attendance/`: Directory where attendance logs are saved.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

This README file should provide a clear understanding of the project's functionality and how to set it up and use it.
