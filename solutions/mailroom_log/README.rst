########
Mailroom
########

Mailroom is a multi-class assignment in UWPCE Python Certificate Program.

This version is using logging. It is by no means complete; I have just demonstrated a couple of different ways of logging to get output to both the console and a logfile. For production code, you would want to carefully consider what should be logged and at what level. In addition to the logging statements themselves sprinkled in various files, the following additions/changes are critical:

=========================  ===============================
     File                       Content/Changes
-------------------------  -------------------------------
mailroom/setup_logging.py  Command to run to setup logging
mailroom/log_file.yaml     Example configuration file
bin/mailroom               Edited to run the setup logging  
                           function at startup
=========================  ===============================





