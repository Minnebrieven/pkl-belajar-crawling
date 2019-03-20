import mongotor, asyncio
from sanic import Sanic
from sanic.response import json,text

app = Sanic(__name__)

@app.route("/test")
async def test(request):
    return await text('its work')

@app.route("/insertmongotor")
async def post_json(request):
    mongotor.do_insert(request.json)
    return json({'received':True,'message':request.json})

if __name__ == "__main__":
    server = app.create_server(host="157.230.242.8", port=1711)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(server)
    loop.run_forever()