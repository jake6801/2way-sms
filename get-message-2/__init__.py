import logging, json

import azure.functions as func
from services.account_service import get_final_message


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = get_final_message()
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})