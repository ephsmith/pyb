from datetime import datetime, timedelta
import os, sys
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    return datetime.strptime(line.split()[1], DATETIME_FORMAT)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    sd_events = list(filter(lambda x: "Shutdown initiated" in x,
                            loglines))
    print(sd_events, file=sys.stderr, flush=True)
    return convert_to_datetime(sd_events[-1]) - \
        convert_to_datetime(sd_events[0])
