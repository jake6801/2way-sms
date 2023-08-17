from twilio.rest import Client
import json, logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass

    account_sid = "AC9cda8136470937b99dcca0bf9baf1334"
    auth_token = "4f0ce0a3a9d9598c165965c03d635b13"
    client = Client(account_sid, auth_token)

    execution = client.studio \
    .v2 \
    .flows('FWa68dae8a51066c3d76a05c197ebc7a3a') \
    .executions \
    .create(
        to='+15879694816', 
        from_='MG10bb79be32902d180e2e091af1406f7f',
        parameters={
            "account": json.dumps(req_body)
        }
    )

    return func.HttpResponse("This HTTP triggered function executed successfully.",
        status_code=200)

