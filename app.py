import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hi():
    return "I love this site!!!"

@app.route("/.well-known/acme-challenge/QCBwkR_csXKHuCDZaCLBH9cfS46r5p1xjYSF30YUetQ")
def for_ca():
    return "QCBwkR_csXKHuCDZaCLBH9cfS46r5p1xjYSF30YUetQ.i-lCVSLDd_qqsUaIchkxvHnTv_L6SiYXbcg7Z8nesQs"
    # e.g. return "lzrajCaq8vbw5Qz2o_XXXXXXXXXXXXXXXXXXz4RnfWtLKaIc6EdhsOsr4fb6RFZuUoabZW5dPW36cmc"

@app.route("/test")
def test():
    return "hello world"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

