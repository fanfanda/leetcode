class Solution:
    '''包含min函数的栈'''
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]
        
    def min(self):
        return self.min_stack[-1]

class Solution:
    stack = []
    min_stack = []
    def push(self, node):
        self.stack.append(node)
        if not self.min_stack or node <= self.min():
            self.min_stack.append(node)
    def pop(self):
        if self.top() == self.min():
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]
    def min(self):
        return self.min_stack[-1]


t = Solution()