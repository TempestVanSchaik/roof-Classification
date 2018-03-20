#Downloads training images:

import sys
sys.path.append("..")
sys.path.append(".")
from azure.storage.blob import BlockBlobService
import zipfile
from KEYS import *

# Blob storage account details kept in git-ignored KEYS.py
ACCOUNT_NAME = accountName
ACCOUNT_KEY = accountKey
CONTAINER_NAME = containerName
BLOB_NAME  = blobName 

block_blob_service = BlockBlobService(account_name=ACCOUNT_NAME, account_key=ACCOUNT_KEY)

root = os.path.expanduser('~')
print("root: " + root)
downloadDir = os.path.expanduser('~') + "/Desktop/RoofData/images/"  


if not os.path.exists(downloadDir):
    os.makedirs(downloadDir)

filePath = os.path.expanduser('~') + "/Desktop/RoofData/images/roofImages.zip" 
open(filePath, "w")
block_blob_service.get_blob_to_path(CONTAINER_NAME, BLOB_NAME, filePath)

#download zipped training data, and then unzip it 
zip_ref = zipfile.ZipFile(filePath, 'r')
zip_ref.extractall(downloadDir)
zip_ref.close()

print("Data downloaded to: " + downloadDir)