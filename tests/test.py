import subprocess
from subprocess import Popen, PIPE, STDOUT

PROJECTNAME = "Untitled" #TODO: Change this to an environment variable
CRITPATH = """
"""
# This stuff doesn't have to be here, it can be outlined in the game itself via "test critpath with <commands>"
# when building complex paths and making fuzz tests, this may be what I eventually want to do

def run(script):
    p = Popen(['interpreter/glulxe/glulxe', '%s.inform/Build/output.gblorb' % PROJECTNAME], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    return p.communicate(input=script)[0].rstrip()

def test_criticalpath():
    pass

if __name__ == "__main__":
    test_criticalpath()


# TODO:
"""
-Create some sort of Task class that represents a discrete unit of game progress
e.g. picking up an item
-Make a game phase class that represents a unit of game state where some Tasks
are no longer available, and other tasks are not yet available.
e.g. a "wait" task makes it night time and progresses the game
-Every task has some sort of confirmation text that it parses the output for
-The assert functions of these tasks are put onto a global queue, and run in order
to chomp the output text to find the expected string and assert it is what it should be.
"""
