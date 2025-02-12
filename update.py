import os
import pandas as pd
import requests
import gdown  
import logging

# Configure logging for error handling
logging.basicConfig(filename="ramply_excel_downloadfiles.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
EXCEL_PATH = "BUSINESS REGISTRATION DOCUMENT SUBMISSION (Responses).xlsx" #excel file name
PARENT_FOLDER = "Business_Submissions"  # Parent folder for all businesses
SHEET_NAME = "Form Responses 1"  # From your excel file

# Map columns to filenames (you can adjust this as needed, the goal is to have unified filename)
COLUMN_TO_FILENAME = {
    "Business Address (Proof Of Address)": "Proof_Of_Address",
    "Certificate Of Incorporation / Business Name Registration Certificate": "Certificate_Of_Incorporation",
    "Memart / Application of Registration": "Application_Of_Registration",
    "Status Report (Must not be Older than 3months)": "Status_Report",
    "Residential Address (Proof of Address – Bank Statement or Utility Bill)": "Residential_Address_Proof",
    "Photo ID Upload": "Photo_ID",
    "Video Declaration": "Video_Declaration",
}

def download_file(url, output_path):
    """Download files from Google Drive or direct links."""
    try:
        if "drive.google.com" in url:
            file_id = url.split("id=")[-1]
            gdown.download(f"https://drive.google.com/uc?id={file_id}", output_path, quiet=False)
        else:
            response = requests.get(url)
            with open(output_path, "wb") as f:
                f.write(response.content)
        logger.info(f"Downloaded {url} to {output_path}")
    except Exception as e:
        logger.error(f"Failed to download {url}: {e}")

def main():
    try:    
        # Read the file
        df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)
        
        # Create parent folder
        os.makedirs(PARENT_FOLDER, exist_ok=True)

        for _, row in df.iterrows():
            business_name = row["Business Name"]
            if not business_name:
                continue

            # Create business folder
            business_folder = os.path.join(PARENT_FOLDER, business_name.replace("/", "_"))
            os.makedirs(business_folder, exist_ok=True)

            # Download files for each column
            for col, filename_prefix in COLUMN_TO_FILENAME.items():
                url = row[col]
                if pd.notna(url) and url.strip():
                    # Clean URL (remove spaces and extra characters)
                    url = str(url).strip()
                    # Define output path
                    file_extension = os.path.splitext(url)[-1].split("?")[0]  # Extract extension
                    file_extension = file_extension if "." in file_extension else ".pdf"  # Default to PDF
                    output_path = os.path.join(business_folder, f"{filename_prefix}{file_extension}")
                    # Download
                    download_file(url, output_path)

            # Save non-file data (e.g., BVN, WhatsApp) to a metadata.txt
            metadata_path = os.path.join(business_folder, "metadata.txt")
            with open(metadata_path, "w") as f:
                f.write(f"Business Name: {business_name}\n")
                f.write(f"BVN: {row['BVN (Bank Verification Number)']}\n")
                f.write(f"WhatsApp: {row['WhatsApp Number']}\n")
                f.write(f"Email: {row['Ramply Email Address']}\n")
    except Exception as e:
        logger.error(f"Failed to process the Excel file: {e}")

if __name__ == "__main__":
    main()