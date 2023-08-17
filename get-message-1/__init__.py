import logging, json, random
from services.test_data import firstMessages

import azure.functions as func
from services.account_service import get_first_message


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    randIndx = random.randint(0, len(firstMessages["messages"])-1)

    try:
        req_body = req.get_json()
    except ValueError:
        pass

    # data = get_first_message(req_body.get('account'))
    data = get_first_message(req_body, randIndx)
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})