from colorama import init, deinit, Fore
import sys
import os

class Utility:
    def __init__(self):
        pass

    @staticmethod
    def print_detailed_error():
        exc_type, exc_obj, exc_tb = sys.exc_info()
        filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        Utility.print_error("Error of type " + str(exc_type) + " occurred at " + filename + " line "
                         + str(exc_tb.tb_lineno) + ":")

    @staticmethod
    def print_error(error):
        init()
        print(Fore.RED + str(error) + Fore.RESET)
        deinit()

    @staticmethod
    def print_warning(warning):
        init()
        print(Fore.YELLOW + str(warning) + Fore.RESET)
        deinit()
