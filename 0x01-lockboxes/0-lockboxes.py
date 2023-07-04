#!/usr/bin/python3
"""implementing lock boxes module"""

# algo

# get a similar lengthed array and mark one as open
# get keys from one and open, making sure you mark every one as open, skip already opened
# get from only opened boxes
# at the end of iterations make sure all boxes are marked open
# let's go

def sortBoxes(boxes):
	open_box = []
	closed_box = []
	for box in boxes:
		if len(box) > 0 and box[-1] == 'open':
			open_box.push(box)
		else:
			closed_box.push(box)
	boxes = open_box.extend(closed_box)

def canUnlockAll(boxes):
	"""can unlock all boxes function"""
	if len(boxes) > 0:
		boxes[0].append('open')
	else: 
		return False
	
	for index, box in enumerate(boxes):
		for inner in box:
			if type(inner) is int:
				if (inner != index):
					boxes[inner].append('open')
	for box in boxes:
		if box[-1] != 'open':
			return False
	return True

