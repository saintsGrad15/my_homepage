import json
import os
import logging
from util import util
from util import section_crud

from flask import Flask, request
from flask_cors import CORS
from config import config

util.setup_logging()

logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

@app.route("/api/sections", methods=["GET"])
def get_sections():
    with open(os.path.join(util.CONFIG_DIRECTORY_PATH, "sections.json")) as fp:
        sections_json = json.load(fp)

        return json.dumps(sections_json), 200, {}

@app.route("/api/addsection", methods=["POST"])
def add_section():
    try:
        request_json = request.json
    except Exception as e:
        logger.exception(e)

        return str(e), 400, {}

    section = request_json["section"]
    index = request_json.get("index")

    validation_result = util.validate_section_schema(section)

    if validation_result is True:
        section_crud.add_section(section_json=section, index=index)

        return "{}", 200, {}
    else:
        return json.dumps(validation_result), 400, {}

if __name__ == "__main__":
    app.run(host="localhost", port=config.PORT, debug=True)
