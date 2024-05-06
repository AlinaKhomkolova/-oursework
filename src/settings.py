from pathlib import Path

ROOT_PATH = Path(__file__).parent

DATA_PATH = ROOT_PATH.joinpath("data")
OPERATIONS_PATH = DATA_PATH.joinpath("/home/alina/coursework/data/operations.json")

SRC_PATH = ROOT_PATH.joinpath("src")
CLASS_PATH = SRC_PATH.joinpath("classes.py")
FUNCTION_PATH = SRC_PATH.joinpath("function.py")


MAIN_PATH = ROOT_PATH.joinpath("main.py")
