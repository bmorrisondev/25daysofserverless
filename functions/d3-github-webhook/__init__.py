import logging
import re
# import urllib
import random
import string
import pymongo
import os

import azure.functions as func
from azure.storage.blob import BlockBlobService

png_base_path = "https://raw.githubusercontent.com/bmorrisondev/25daysofserverless/master"

class ImageItem:
    name = ''
    url = ''

def random_string(size = 6, chars=string.ascii_letters  + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try: 
        webhook = req.get_json()

        images_to_add = []

        regex_pattern = '[^\/]*$'

        for commit in webhook.get('commits'):
            for added_item in commit.get('added'):
                if added_item.endswith("png"):
                    image_item = ImageItem()
                    regexObj = re.search(regex_pattern,added_item)
                    image_item.name = regexObj[0]
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
            block_blob_service.copy_blob(container_name, blob_name, file.url)
            blob_url = block_blob_service.make_blob_url(container_name, blob_name)
            blob_urls.append(blob_url)

        # Write URLs to Cosmo using Mongo API
        mongo_cs = os.environ["CosmoMongoApiCs"]
        cosmo_client = pymongo.MongoClient(mongo_cs)
        db = cosmo_client["day3"]
        images_collection = db["images"]

        for url in blob_urls:
            record = { "url": url }
            images_collection.insert_one(record)
        
        return func.HttpResponse("ok")
    
    except Exception as err:
        return func.HttpResponse(
            f"{err}",
            status_code = 500
        )