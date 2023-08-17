import logging, json, random
from services.test_data import extensionFinalMessage, cancellationFinalMessage

import azure.functions as func
from services.account_service import get_closer_message


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    randIndx = random.randint(0, len(extensionFinalMessage["messages"])-1)
    try:
        req_body = req.get_json()
    except ValueError:
        pass

    data = get_closer_message(req_body, randIndx)
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})