import logging

import azure.functions as func


def main(msg: func.ServiceBusMessage):
    logging.info('The following message was sent to Lucy: %s',
                 msg.get_body().decode('utf-8'))
