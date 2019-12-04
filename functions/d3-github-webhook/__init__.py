import logging
import re
import random
import string
import pymongo
import os

from .helpers import random_string
from .ImageItem import ImageItem

import azure.functions as func
from azure.storage.blob import BlockBlobService


def main(req: func.HttpRequest) -> func.HttpResponse:
    png_base_path = "https://raw.githubusercontent.com/bmorrisondev/25daysofserverless/master"

    try: 
        webhook = req.get_json()
        images_to_add = []
        regex_pattern = '[^\/]*$'

        for commit in webhook.get('commits'): # Iterate through all the commits in the push
            for added_item in commit.get('added'): # Iterate through added items
                if added_item.endswith("png"): # Find items with png
                    image_item = ImageItem() # Create the object to store name and url
                    regexObj = re.search(regex_pattern,added_item)
                    image_item.name = regexObj[0] # Parse out the file name
                    image_item.url = f"{png_base_path}/{added_item}"
                    images_to_add.append(image_item)
                    logging.info(f'found {image_item.name} at {image_item.url}') 

        
        # Copy files to Azure Storage Account, create URLs for the blobs and return for saving to Cosmo
        azure_path = "images"
        container_name = 'day3'

        blob_cs = os.environ["BlobServiceCs"]

        block_blob_service = BlockBlobService(
            connection_string = blob_cs
        )

        blob_urls = []
        for file in images_to_add:
            blob_name = f"{azure_path}/{random_string()}_{file.name}"
            block_blob_service.copy_blob(container_name, blob_name, file.url) # Download the file into ASA
            blob_url = block_blob_service.make_blob_url(container_name, blob_name) # Get a direct link to the blob in ASA
            blob_urls.append(blob_url)

        # Write URLs to Cosmo using Mongo API
        mongo_cs = os.environ["CosmoMongoApiCs"]
        cosmo_client = pymongo.MongoClient(mongo_cs)
        db = cosmo_client["day3"]
        images_collection = db["images"]

        for url in blob_urls:
            record = { "url": url }
            images_collection.insert_one(record) # Add the URL to the Cosmo DB collection
        
        return func.HttpResponse("ok")
    
    except Exception as err:
        return func.HttpResponse(
            f"{err}",
            status_code = 500
        )