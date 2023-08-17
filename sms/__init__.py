import logging
import json
import azure.functions as func

data = {
    'symendID': 12345,
    'paymentExtension': False,
    'cancellation': False
}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(json.dumps(data, indent=2), 
            mimetype='application/json',
            status_code=200)
