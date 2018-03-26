import leankitbackend.timereport as t
import leankitbackend.history as h
import leankitbackend.cron_job as c
from os import getcwd

if __name__ == "__main__":

    c.get_data()  # doing a cron job
    h.time_report()  # doing an analysis over time
    Board, Cards, Data = t.Report_Stat()  # doing an analysis now

    
