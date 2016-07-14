"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        queue = []
        for comp in path.split('/'):
            if not comp or comp == '.' or (comp == '..' and len(queue) == 0):
                continue
            elif comp == '..':
                queue.pop()
            else:
                queue.append(comp)
        return '/' + '/'.join(queue)
