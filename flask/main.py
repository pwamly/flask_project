from flask import Flask
from flask import jsonify
from flask import request
import logging 

app = Flask(__name__)
logging.basicConfig(filename='log_test.txt ', level=logging.DEBUG)


quarks =  {
        "access_token": "8c6lQ8L2TXyY--uzEUY1mnZPboWdyaplw2lcHDkOp3nmnWIkOgUHFfHGtgVwk8dfGRTHaEm4ytMogdEabfHQth5J1E2d5btyesQEX6WVr_2ROZ7PE9e0zsLMmkzJKvxLoUdmLQSB4leFWf0Zav84AoI6M20c45SiwJclgQsLuU4i9QZihcyEKz4s5Y79IlHTlYTedFHBv_ZPfx_dLFVDgrs_Ncfoyp-8_oCYFb8IuktBg1XK_jqfl_3kicUVWjRveuDYEzN-DYGvFmcMJ8JNR3e223jubv7jkjwfC9Mwg9XtM6W6MCi_Nfmc2XsBlYH1",
        "token_type": "bearer",
        "expires_in": 3599
          }

@app.route('/token', methods=['POST'])
def hello_world():
    app.logger.info('token returned succefuly..................') 
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    app.logger.info(' SENDING AIRTEL B2C - [-- testing info log --]')
    return jsonify(quarks)



@app.route('/API/BillerPayment/BillerPay', methods=['POST'])
def returnOne(name):
    
    return jsonify({'quarks' : theOne})







if __name__ == "__main__":
    app.run(debug=True)