import logging
import sys
import json
import os

from typing import Dict, Union
from jschon import create_catalog, JSON, JSONSchema

_module_directory_path = os.path.dirname(os.path.abspath(__file__))
_config_directory_path = os.path.join(os.path.dirname(_module_directory_path), "config")

print(os.path.join(_config_directory_path, "section_schema.json"))

def setup_logging():
    # Use this format for more verbosity
    LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))

    logger.addHandler(handler)

def validate_section_schema(section_json: Dict) -> Union[bool, Dict]:
    with open(os.path.join(_config_directory_path, "section_schema.json")) as fp:
        schema_json = json.load(fp)

    create_catalog('2020-12')

    schema = JSONSchema(schema_json)

    result = schema.evaluate(JSON(section_json))

    if result.valid is True:
        return True
    else:
        return result.output("basic")