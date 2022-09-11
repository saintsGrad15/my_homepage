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
    """
    Validate `section_json` against its JSON schema.

    Arguments:
        section_json {Dict} -- A "section" json, expected to be compliant with "/server/config/section_schema.json

    Returns:
        Union[bool, Dict] -- True if `section_json` validated against its schema, a JSON report of `section_json`'s errors otherwise.
    """

    with open(os.path.join(_config_directory_path, "section_schema.json")) as fp:
        schema_json = json.load(fp)

    create_catalog('2020-12')

    schema = JSONSchema(schema_json)

    result = schema.evaluate(JSON(section_json))

    if result.valid is True:
        return True
    else:
        return result.output("basic")

def add_section(section_json: Dict, index: int = None) -> None:
    """
    Add `section_json` to the "sections" document.

    Arguments:
        section_json {Dict} -- A "section" json, expected to be compliant with "/server/config/section_schema.json

    Keyword Arguments:
        index {int} -- The zero-based index at which to insert `section_json`. (default: {None})
    """

    sections_json_path = os.path.join(_config_directory_path, "sections.json")

    with open(sections_json_path) as fp:
        sections_json: list = json.load(fp)

    if index is None:
        index = len(sections_json)

    sections_json.insert(index, section_json)

    with open(sections_json_path, mode="w") as fp:
        json.dump(sections_json, fp, indent=4, sort_keys=True)
