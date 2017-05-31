from sanic import Sanic
from sanic.response import json

from JumpScale9AYS.ays.server.ays_if import ays_if
from JumpScale9AYS.ays.server.webhooks_if import webhooks_if

app = Sanic(__name__)

app.blueprint(ays_if)
app.blueprint(webhooks_if)

app.static('/apidocs', 'JumpScale9AYS/ays/server/apidocs/index.html')
app.static('/', 'JumpScale9AYS/ays/server/index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, workers=1)
