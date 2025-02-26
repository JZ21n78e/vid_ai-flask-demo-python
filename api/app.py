from flask      import Flask, request, current_app, jsonify
# from .utilities import status ,submit

# importing sys
import sys
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '/home/jzruz/21projects/vid_ai-flask-demo-python/api/vid_ai')

from main import submit,status

app = Flask(
    __name__,
    static_url_path= '', 
    static_folder  = '../web'
)



@app.route('/')
def index():
    return current_app.send_static_file('index.html')

@app.route('/kwds', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"data": "list , of , keywords , will , be shown , here"}
        return jsonify(data)

@app.route('/demo/shotstack', methods = ['POST'])
def post_render():
    data  = request.json
    try:
        reply = submit(data)

        return jsonify({
            "status":   "success",
            "message":  "OK",
            "data":     {
                "id":       reply.id,
                "message":  reply.message
            }
        })
    except Exception as e:
        return jsonify({
            "status":   "fail",
            "message":  "Bad Request",
            "data":     e
        })

@app.route('/demo/shotstack/<renderId>')
def render(renderId):
    try:
        reply = status(renderId).to_dict()

        return jsonify({
            "status":   "success",
            "message":  "OK",
            "data":     {
                "data":     reply.get('data', None),
                "status":   reply.get('status', None),
                "url":      reply.get('url', None)
            }
        })
    except Exception as e:
        return jsonify({
            "status":   "fail",
            "message":  "Bad Request",
            "data":     e
        })
