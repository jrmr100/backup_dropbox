import dropbox
from dropbox.exceptions import AuthError, ApiError
import os
from dotenv import load_dotenv

load_dotenv()

from utils.logger import logger


def upload_file_dropbox(local_file_path, dropbox_folder_path):
    try:
        """
        Uploads a file from local storage to a specified Dropbox folder.
    
        Args:
            local_file_path (str): The full path to the file on your local machine.
            dropbox_folder_path (str): The path to the folder in your Dropbox where the file will be uploaded.
                                       e.g., '/my_uploads/' or '/' for the root.
            access_token (str): Your Dropbox API access token.
        """
        access_token = os.getenv("DROPBOX_ACCESS_TOKEN")
        dbx = dropbox.Dropbox(access_token)

        # Ensure the Dropbox folder path is valid
        if not dropbox_folder_path.startswith('/'):
            dropbox_folder_path = '/' + dropbox_folder_path
        if not dropbox_folder_path.endswith('/'):
            dropbox_folder_path = dropbox_folder_path + '/'

        # Get the file name from the local path
        file_name = os.path.basename(local_file_path)
        dropbox_file_path = f"{dropbox_folder_path}{file_name}"


        with open(local_file_path, 'rb') as f:
            logger.info(f"Uploading '{local_file_path}' to '{dropbox_file_path}' on Dropbox...")
            dbx.files_upload(f.read(), dropbox_file_path, mode=dropbox.files.WriteMode('overwrite'))
            logger.info(f"Successfully uploaded '{file_name}' to Dropbox!")
            logger.info(f"You can find it at: https://www.dropbox.com/home{dropbox_file_path}")
        dbx.close()
        return True

    except AuthError:
        logger.info("ERROR: Invalid Dropbox Access Token. Please check your token and try again.")
    except ApiError as err:
        if err.error.is_path() and err.error.get_path().is_not_found():
            logger.info(f"ERROR: Dropbox folder '{dropbox_folder_path}' not found. Please ensure the folder exists.")
        elif err.user_message_text:
            logger.info(f"ERROR: {err.user_message_text}")
        else:
            logger.info(f"ERROR: An API error occurred: {err}")
    except FileNotFoundError:
        logger.info(f"ERROR: Local file not found at '{local_file_path}'. Please check the path.")
    except Exception as e:
        logger.info(f"An unexpected error occurred: {e}")

