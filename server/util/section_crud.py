import os
import json

from typing import Dict, List
from util import util

def get_sections() -> List[Dict]:
    with open(os.path.join(config_path, "sections.json")) as fp:
        sections_json = json.load(fp)

    return sections_json


def add_section(section_json: Dict, index: int = None) -> None:
    """
    Add `section_json` to the "sections" document.

    Arguments:
        section_json {Dict} -- A "section" json, expected to be compliant with "/server/config/section_schema.json

    Keyword Arguments:
        index {int} -- The zero-based index at which to insert `section_json`. (default: {None})
    """

    sections_json_path = os.path.join(util.CONFIG_DIRECTORY_PATH, "sections.json")

    with open(sections_json_path) as fp:
        sections_json: list = json.load(fp)

    if index is None:
        index = len(sections_json)

    sections_json.insert(index, section_json)

    with open(sections_json_path, mode="w") as fp:
        json.dump(sections_json, fp, indent=4, sort_keys=True)
