import logging, json

import azure.functions as func
from services.account_service import add_accounts


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        req_body = req.get_json()
    except ValueError:
        pass

    data = add_accounts(req_body.get('account'))
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})