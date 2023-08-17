import logging, json

import azure.functions as func
from services.account_service import get_account


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try: 
        req_body = req.get_json()
    except ValueError:
          pass

    data = get_account(req_body)
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})