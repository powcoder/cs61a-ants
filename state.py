https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
class State:
    """A State holds a current game state and all of its attributes"""

    def __init__(self):
        """Create a new gamestate"""
        self.gs = {}

    def getState(self, key=None):
        if key:
            return self.gs[key]
        return self.gs

    def updateState(self, key, val):
        self.gs[key] = val
