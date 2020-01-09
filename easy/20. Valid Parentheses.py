
class Solution(object):
    def isValid(self, s):
        self.stack = []
        for i in s:
            if i == '{' or i =='[' or i =='(':
                self.stack.append(i)
            elif i == '}':
                if len(self.stack) == 0:
                    return False
                elif self.stack[-1] == '{':
                    self.stack.pop()
                    continue
                else:
                    return False
            elif i == ']':
                if len(self.stack) == 0:
                    return False
                elif self.stack[-1] == '[':
                    self.stack.pop()
                    continue
                else:
                    return False
            elif i == ')':
                if len(self.stack) == 0:
                    return False
                elif self.stack[-1] == '(':
                    self.stack.pop()
                    continue
                else:
                    return False

        if len(self.stack) > 0:
            return False
        else:
            return True
