import logging
import pymongo
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        mongo_cs = os.environ["CosmoMongoApiCs"]
        cosmo_client = pymongo.MongoClient(mongo_cs)
        db = cosmo_client["day4"]
        tasks_collection = db["tasks"]
        tasks = tasks_collection.find({"isDeleted": { "$ne": "true" }})
        func.HttpResponse(tasks)
    except Exception as err:
        return func.HttpResponse(
            f"{err}",
            status_code = 500
        )
