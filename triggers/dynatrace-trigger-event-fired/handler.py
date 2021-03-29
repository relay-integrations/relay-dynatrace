from relay_sdk import Interface, WebhookServer
from quart import Quart, request
import logging
import json

relay = Interface()
app = Quart('event-fired')

logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['POST'])
async def webhook():
    data = await request.get_json()
    logging.info("Received the following webhook payload: \n%s", json.dumps(data, indent=4))
    
    headers = ""

    for key, value in request.headers.items():
        headers = headers + ";" + key
        if key.lower().startswith("x-dynatrace"):
            relay.events.emit(data)
            return {'success': True}

    return {'message': 'not a valid Dynatrace event:' + headers}, 400, {}

if __name__ == '__main__':
    WebhookServer(app).serve_forever()
