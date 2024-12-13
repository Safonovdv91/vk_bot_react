from enum import Enum


class GameStage(Enum):
    WAIT_INIT = "WAIT_INIT"
    REGISTRATION_GAMERS = "REGISTRATION_GAMERS"
    WAITING_READY_TO_ANSWER = "WAITING_CALLBACK"
    WAITING_ANSWER = "WAITING_ANSWER"
    FINISHED = "FINISHED"
    CANCELED = "CANCELED"