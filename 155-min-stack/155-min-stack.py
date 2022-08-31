class MinStack:

    def __init__(self):
        self.stack = [] #initialize both stacks one as the actual stack and one to keep the minimum value
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val) # append vaue to the stack
        val = min(val, self.minStack[-1] if self.minStack else val) # val now equals the minimum vaue between current val and the top of the minimum stack, if minStack is not empty 
        self.minStack.append(val) # append the val

    def pop(self) -> None:
        self.stack.pop() # built in method to pop from both stacks
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] #returns the top of the stack

    def getMin(self) -> int:
        return self.minStack[-1] #returns the top of the minStack which should be the minimum value overall
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()