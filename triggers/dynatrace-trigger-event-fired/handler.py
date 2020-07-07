from nebula_sdk import Interface, WebhookServer
from quart import Quart, request

relay = Interface()
app = Quart('event-fired')

@app.route('/', methods=['POST'])
async def webhook():
    data = await request.get_json()
    headers = ""

    for key, value in request.headers.items():
        headers = headers + ";" + key
        if key.lower().startswith("x-dynatrace"):
            relay.events.emit(data)
            return {'success': True}

    return {'message': 'not a valid Dynatrace event:' + headers}, 400, {}

if __name__ == '__main__':
    WebhookServer(app).serve_forever()