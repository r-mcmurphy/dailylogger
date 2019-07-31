import os
import sys
import readline
from views import home_view, missed_days_view, time_mgr, log_mgr


if __name__ == '__main__':
    try:
        if sys.argv[1] == "-l" or sys.argv[1] == "--log":
            missed_days_view(time_mgr.get_all_missed_days(log_mgr))
        else:
            raise IndexError
    except IndexError:
        home_view()
