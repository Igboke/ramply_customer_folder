# Ramply Excel Format Script
## Introduction
This script is designed to help you download files in the Excel files easily. Follow the instructions below to get started.

## Prerequisites
- Python 3.x installed on your system (i already installed it)

## Installation
1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/Igboke/ramply_excel_format.git
    ```
   If you are not familiar with Git, you can download the repository as a ZIP file:
   - Go to the repository page on GitHub.
   - Click on the "Code" button.
   - Select "Download ZIP".
   - Extract the ZIP file to your desired location.

2. Navigate to the project directory:
    ```sh
    cd ramply_excel_format
    ```

3. Install the required libraries:
    - You can copy all the commands and paste in cmd using shift + insert
    - Open Command Prompt (cmd) by pressing `Win + R`, typing `cmd`, and pressing `Enter`.
    - Navigate to the project directory in the Command Prompt:
        ```sh
        cd path\to\ramply_excel_format
        ```
      To get the path to the folder, you can open the folder in File Explorer, click on the address bar, and copy the path.
    - Paste the path in the Command Prompt by pressing `Shift + Insert` with cd before it like the example above.
    - Install the required libraries:
        ```sh
        pip install -r requirements.txt
        ```


## Usage
1. Place the Excel file you want to format in the `input` folder.
2. Run the script for downloading all files in folder:
    ```sh
    python update.py
    ```
3. The downlaoded files will be saved in the `output` folder.
4. Run the script for downloading only the folders:
    ```sh
        python main.py
    ```

## Configuration
- You can modify the script to change the formatting rules as per your requirements. Open `format_excel.py` and edit the relevant sections.

## Troubleshooting
- Ensure that the input Excel file is not open in any other application while running the script.
- Check that the input file is in the correct format and located in the `input` folder.

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

## Contact
For any questions or issues, please contact danieligboke669 at gmail dot com.
