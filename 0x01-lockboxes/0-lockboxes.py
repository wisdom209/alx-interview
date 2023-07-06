#!/usr/bin/python3
"""implementing lock boxes module"""


def canUnlockAll(boxes):
    """can unlock all boxes function"""
    if not boxes or isinstance(boxes, list) is False:
        return False
    if len(boxes) > 0:
        boxes[0].append('open')
    else:
        return False

    for index, box in enumerate(boxes):
        for inner in box:
            if isinstance(inner, int):
                if (inner != index):
                    boxes[inner].append('open')
    for box in boxes:
        if box[-1] != 'open':
            return False
    return True
