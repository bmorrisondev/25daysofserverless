import logging
import random

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    selectedIndex = random.randint(0,3)
    options = [
        "Nun",
        "Gimmel",
        "Hay",
        "Shin"
    ]

    return func.HttpResponse(f"Have a day: {options[selectedIndex]}")
