import datetime
import logging
import requests
import os

import azure.functions as func

logicAppPostUrl = os.environ["D2LogicAppUrl"]

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    requests.post(url = logicAppPostUrl)

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
