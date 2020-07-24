# from flask import Flask
# from flask import request
#
# app = Flask(__name__)
# @app.route('/profile/create')
# def createProfile():
#     return "successfully profileCreate"
# @app.route('/myname')
# def getName():
#     return "Hello Arpita"
# @app.route('/')
# def hello():
#     return "Hello Arpita World!"
# @app.route('/hcm', methods=['GET', 'POST'])
# def parse_request():
#     data = request.data  # data is empty
#     print("Data 0",data)
#     return "HCM"
#     # need posted data here
# @app.route('/post', methods=['POST'])
# def post_route():
#     if request.method == 'POST':
#         print(request)
#         data = request.get_json(force = True)
#         print("HAarish",data)
#         print('Data Received: "{data}"'.format(data=data))
#         return "Request Processed.\n"
# if __name__ == '__main__':
#     app.run()