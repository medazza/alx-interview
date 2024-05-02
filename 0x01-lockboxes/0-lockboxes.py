#!/usr/bin/python3
'''
    A Module for working with lockboxes
'''


def canUnlockAll(boxes):
    '''
        prototype: def canUnlockAll(boxes)
        boxes is a list of lists
        A key with the same number as a box opens that box
        all keys will be positive integers
        Return True if all boxes can be opened, else False
    '''
    total_boxes = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= total_boxes or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return total_boxes == len(seen_boxes)
