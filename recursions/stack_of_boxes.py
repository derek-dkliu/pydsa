"""
because of the restriction of the stack that upper boxes should be smaller in size,
we need to sort the boxes in descending order of size first, and build the stack by
considering whether or not to put a particular box in the stack by this order.
"""
# time:  O(n*n)
# space: O(n*n)
def stack_boxes(boxes):
    boxes.sort(key=lambda x: x[0], reverse = True)
    return place_boxes(boxes, 0, None, {})

def place_boxes(boxes, index, bottom, memo):
    if index == len(boxes): return 0
    if (bottom, index) in memo: return memo[(bottom, index)]

    h1 = place_boxes(boxes, index + 1, bottom, memo)
    h2 = 0
    box = boxes[index]
    if bottom is None or (box[0] < bottom[0] and box[1] < bottom[1] and box[2] < bottom[2]):
        h2 = box[1] + place_boxes(boxes, index + 1, box, memo)
    memo[(bottom, index)] = max(h1, h2)
    return memo[(bottom, index)]

boxes = [
    (3,5,5),
    (2,2,3),
    (6,8,6),
    (1,1,1),
    (9,12,5)
]
print(stack_boxes(boxes))