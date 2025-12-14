1class Solution:
2    def interpret(self, command: str) -> str:
3        return command.replace("()", "o").replace("(al)", "al")