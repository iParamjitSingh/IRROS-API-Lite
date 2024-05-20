from flask import Flask, request, send_file
from io import BytesIO
from irros import getRoute


app = Flask(__name__)


@app.route('/')
def home():
    return 'IRROS API is UP!'


@app.route('/route')
def route():
    src = request.args.get('src')
    dest = request.args.get('dest')
    
    # perosonalization parameter
    per_str = request.args.get('per')
    if per_str is not None:
        per = per_str.lower() == 'true'
    else:
        per = False  

    # Testing
    print('source: ', src)
    print('destination: ', dest)
    print('personalization: ', per)

    fig = getRoute(src, dest, per)
    img_buffer = BytesIO()
    fig.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    fig.clf()
    return send_file(img_buffer, mimetype='image/png')