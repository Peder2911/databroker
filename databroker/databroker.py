
import os
import json
import logging 

from .resolvers import resolve
from databroker.exceptions import BadRequestError
from flask import Flask,request

logger = logging.getLogger(__name__)

sources = {}
try:
    with open(os.getenv("BROKER_SOURCES")) as f:
        sources = json.load(f)
except (TypeError,FileNotFoundError):
    logger.warning("No source file found")

app = Flask(__name__)
app.config["SOURCES"] = sources

@app.route("/",methods=["POST"])
def broker():
    try:
        data = resolve(request.json,app.config["SOURCES"])
    except BadRequestError:
        return {
            "message": "bad request"
        }
    return {
        "message": "ok",
        "data": str(data) 
    }
