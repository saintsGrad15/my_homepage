import os
import json

from typing import Dict, List
from util import util

_sections_json_path = os.path.join(util.CONFIG_DIRECTORY_PATH, "sections.json")

def get_sections() -> List[Dict]:
    """
    Return the "sections" document.

    Returns:
        List[Dict] -- The "sections" document.
    """

    with open(_sections_json_path) as fp:
        sections_json = json.load(fp)

    return sections_json

def write_sections(sections_json: List[Dict]) -> None:
    with open(_sections_json_path, mode="w") as fp:
        json.dump(sections_json, fp, indent=4, sort_keys=True)

def add_section(section_json: Dict, index: int = None) -> None:
    """
    Add `section_json` to the "sections" document.

    Arguments:
        section_json {Dict} -- A "section" json, expected to be compliant with "/server/config/section_schema.json

    Keyword Arguments:
        index {int} -- The zero-based index at which to insert `section_json`. (default: {None})
    """

    sections_json = get_sections()

    if index is None:
        index = len(sections_json)

    sections_json.insert(index, section_json)

    write_sections(sections_json)


def delete_section(index: int) -> None:
    """
    Delete zero-based `index` from the "sections" document.

    Arguments:
        index {int} -- The zero-based index to delete.

    Raises:
        ValueError: `index` is out of bounds.
    """

    sections_json = get_sections()

    if index > len(sections_json) - 1:
        raise ValueError(f"`index` is out of bounds for \"sections\" (length: ${len(sections_json)}"
    )

    del sections_json[index]

    write_sections(sections_json)
