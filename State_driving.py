from enum import Enum

class State(Enum):
    STOP = 0
    SIMPLEDRIVE = 1
    WLANDRIVE = 2
    DESTINATION = 3
    FOLLOW = 4