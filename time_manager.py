import datetime


WEEKDAYS = {
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday'
}


class TimeManager():
    def __init__(self):
        pass
        
    def today(self):
        td = datetime.datetime.now()
        if td.hour < 12:
            td = td - datetime.timedelta(days=1)
        datestr = td.strftime("%Y-%m-%d")
        return datestr

    def get_specific_date(self, datestr):
        str_res = ""
        for c in datestr:
            if c.isdigit():
                str_res += c
        if len(str_res) == 8:
            year = str_res[:4]
            month = str_res[4:6] if str_res[4]!="0" else str_res[5]
            day = str_res[6:8] if str_res[6]!="0" else str_res[7]
            return datetime.datetime(int(year), int(month), 
                    int(day)).date().strftime("%Y-%m-%d")
        elif len(str_res) == 6:
            year = "20"+str_res[:2]
            month = str_res[2:4] if str_res[2]!="0" else str_res[3]
            day = str_res[4:6] if str_res[4]!="0" else str_res[5]
            return datetime.datetime(int(year), int(month), 
                    int(day)).date().strftime("%Y-%m-%d")
        else: return None

    def n_days_ago(self, n):
        n = int(n)
        return (datetime.datetime.strptime(self.today(),"%Y-%m-%d")
                -datetime.timedelta(n)).strftime("%Y-%m-%d")

    def get_all_missed_days(self, log_mgr):
        """Returns list of string formatted days that don't have entry in log"""
        tday = datetime.datetime.strptime(self.today(),"%Y-%m-%d")
        data = log_mgr.get_log_data()
        first_day = sorted(data.keys())[0]
        pointer = datetime.datetime.strptime(first_day, "%Y-%m-%d") + datetime.timedelta(1)
        missed_days = []
        while pointer != tday:
            pointer += datetime.timedelta(1)
            d = pointer.strftime("%Y-%m-%d")
            if d not in data.keys():
                missed_days.append(d)
        return missed_days


    def check_date(self, day, trackable):
        day = datetime.datetime.strptime(day, "%Y-%m-%d")
        timestmp = trackable.period
        if timestmp[0] == "W": # Each digit specifies one weekday
            for d, ch in enumerate(timestmp[1:]):
                if ch == "1" and day.weekday() == d:
                    return True
            else:
                return False
        elif timestmp[0] == "M": # Each 2 digits specify the monthday
            s = timestmp[1:]
            days = [int(s[i:i+2]) for i in range(0, len(s), 2)]
            if day.day in days:
                return True
            else:
                return False
        elif timestmp[0] == "Y": # Each 4 digits specify the number of month
            s = timestmp[1:]     # and the number of day (MMDD)
            days = [(int(s[i:i+4][:2]), int(s[i:i+4][2:])) for i in range(0, len(s), 4)]
            for d in days:
                if d[0] == day.month and d[1] == day.day:
                    return True
            else:
                return False
        elif timestmp[0] == "P": # This is meant to track actions that take place periodically
            tday = datetime.datetime.today()
            s = timestmp[1:]
            start, active_dur, inactive_dur = s.split(" ")
            start = datetime.datetime.strptime(day, "%Y-%m-%d")
            active_dur = int(active_dur)
            inactive_dur = int(inactive_dur)
            if tday - start < 0:
                return False # At the moment of creation I don't feel the need
            return False     # for that feature, so it's not done yet