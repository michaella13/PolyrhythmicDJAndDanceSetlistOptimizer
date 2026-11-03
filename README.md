# Key points
- The assignment builds three layers, each one on top of the last:
    - `DoublyLinkedList`: the base data structure, using `head` and `tail` nodes. 
    - `PriorityQueue`: wraps a `DoublyLinkedList` that is always kept in ascending order, so the largest value is always at index `-1`. Each method mostly calls an existing linked list method.
    - `fill_cups`: uses the priority queue for a greedy algorithm that always fills the two cup types with the most cups left.

# Lessons learned
- After working in C all semester, this helped me understand Python better, especially `self`. It refers to the object itself, and works a lot like passing a pointer to a struct in C. Attributes saved with `self.` stay with the object, while plain local variables disappear when the method ends.
- Thinking through the greedy algorithm helped me see why always taking from the two largest piles gives the minimum time: it keeps one pile from being left with nothing to pair with.
- Bug I hit: my first `fill_cups` only pushed values back into the queue when both counts were above 0. When the second-largest count was 0, the remaining cups disappeared from the queue, so `5 0 0` stopped after 1 second instead of 5. The fix was to always push both values back and only skip subtracting from the one that was already 0. Lesson: test edge cases like zeros, not just the example given.


# Use of AI
I used Claude as a tutor throughout, mainly to explain Python concepts in terms of C, which I know better. I worked through `_get_node`, `insert_ordered`, `__getitem__`, `__setitem__`, `pop`, `PriorityQueue.__init__` and `push`, the `fill_cups` approach, and `main` myself, with hints and corrections when I got stuck. 

# Other notes
- I'm especially interested in this material because I want to use it in my final project.