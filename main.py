import logging
import pandas as pd
import os

# Configure logging for error handling
logging.basicConfig(filename="ramply_excel_folderonly.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
FILE_PATH = "C:/Users/Lenovo/Desktop/ramply_excel_format/BUSINESS REGISTRATION DOCUMENT SUBMISSION  (Responses).xlsx"
SHEET_NAME = "Form Responses 1"      
COLUMN_NAME = "Business Name"                  
PARENT_DIR = "C:/Users/Lenovo/Desktop/ramply_excel_format/ramply_customer_folder"

# Read the file
if FILE_PATH.endswith('.xlsx'):
    df = pd.read_excel(FILE_PATH, sheet_name=SHEET_NAME)
elif FILE_PATH.endswith('.csv'):
    df = pd.read_csv(FILE_PATH)
else:
    logger.error(f"Unsupported file format. Use .xlsx or .csv.")

# Create folders
for folder_name in df[COLUMN_NAME]:
    folder_name = str(folder_name).strip()  # Clean whitespace/convert to string
    if folder_name:
        folder_path = os.path.join(PARENT_DIR, folder_name)
        try:
            os.makedirs(folder_path, exist_ok=False)  # Create folder (fails if exists)
            logger.info(f"Created folder: {folder_path}")
        except FileExistsError:
            logger.error(f"Folder already exists: {folder_path}")
        except Exception as e:
            logger.error(f"Failed to create folder: {folder_path}. Error: {e}")