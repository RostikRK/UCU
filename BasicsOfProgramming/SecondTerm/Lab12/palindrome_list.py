"""
Palindrome class realization.
"""
from arraystack import ArrayStack   # or from linkedstack import LinkedStack
import math

class Palindrome:
    """
    Palindrom class
    """
    def __init__(self) -> None:
        pass
    def read_file(self, path):
        """
        Reads file
        """
        if path.endswith(".lst"):
            with open(path, 'r+', encoding="utf-8") as file:
                res = [line.split()[0] for line in file.readlines()]
        else:
            with open(path) as file:
                # for line in file.readlines():
                #     print(line)
                res = [line[:-1] for line in file.readlines()]
        return res
    def find_palindromes(self, path1, path2):
        """
        Reads file and finds palindroms in it after writes them in the file
        """
        check_list = self.read_file(path1)
        palindromes = []
        for word in check_list:
            stack = ArrayStack()
            for char in word:
                stack.add(char)
            end = ""
            for _ in range(math.ceil(len(word)//2)):
                end += stack.pop()
            if word[:math.ceil(len(word)//2)] == end:
                palindromes.append(word)
        self.write_to_file(path2, palindromes)
        return palindromes
    def write_to_file(self, path, words):
        """
        Writes palindroms in the file
        """
        with open(path, 'w') as file:
            for word in words:
                file.write(word + "\n")
