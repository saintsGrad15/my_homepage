import json
import os
import logging
from util import util

from flask import Flask, request
from flask_cors import CORS
from config import config

util.setup_logging()

logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

module_path = os.path.abspath(__file__)
config_path = os.path.join(os.path.dirname(module_path), "config")

@app.route("/api/sections", methods=["GET"])
def get_sections():
    with open(os.path.join(config_path, "sections.json")) as fp:
        sections_json = json.load(fp)

        return json.dumps(sections_json), 200, {}

@app.route("/api/addsection", methods=["POST"])
def add_section():
    try:
        request_json = request.json
    except Exception as e:
        logger.exception(e)

    validation_result = util.validate_section_schema(request_json["section"])

    if validation_result is True:
        # Continue...
        return "{}", 200, {}
    else:
        return json.dumps(validation_result), 400, {}

if __name__ == "__main__":
    app.run(host="localhost", port=config.PORT, debug=True)
