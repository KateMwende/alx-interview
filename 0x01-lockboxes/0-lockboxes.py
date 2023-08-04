#!/usr/bin/env python3
"""Method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    method:
        all boxes can be opened?
    Args:
        boxes a list of lists
    Returns:
        boolean. True if all boxes can be opened else false
    """
    keys = [0]  # keys available in first box

    # loop through the available keys and open corresponding boxes
    for key in keys:
        """loop through opened boxes and their keys to open more boxes """
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)  # add new key to available keys
    if len(keys) == len(boxes):
        return True
    return False
