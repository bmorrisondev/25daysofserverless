import logging
import pymongo
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        document = {
            "title": body.get_json("title")
        }
        mongo_cs = os.environ["CosmoMongoApiCs"]
        cosmo_client = pymongo.MongoClient(mongo_cs)
        db = cosmo_client["day4"]
        tasks_collection = db["tasks"]
        tasks_collection.insert_one(document)
        func.HttpResponse("ok")
    except Exception as err:
        return func.HttpResponse(
            f"{err}",
            status_code = 500
        )
