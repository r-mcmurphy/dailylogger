import sys
import readline
import argparse
from views import home_view, missed_days_view, time_mgr, log_mgr

parser = argparse.ArgumentParser(description='A program to log your daily routines.')
parser.add_argument('-l', '--log', action='store_true', help='avoid unnecessary interaction - jump straight to logging')

if __name__ == '__main__':
    args = parser.parse_args()
    if args.log:
        missed_days_view(time_mgr.get_all_missed_days(log_mgr))
    else:
        home_view()
