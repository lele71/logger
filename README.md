**Class Logger**

Produces a log file, in the location specified at instance time, in the format:

yyyymmdd-app\_name.log, app\_name passed in the instance phase typically is the name of the application that generates the log.

By default it logs any message, to filter messages use the addFilter () method, while to remove filters use the removeFilter () method.

**Instance:**

`	`*logger(position, appName)*

Where:

`	`position: is the relative path for log file

`	`appName i the name of the application name will compose the log file name



**Log level:**

{

`            `0: 'NOSET',

`            `10: 'DEBUG',

`            `20: 'INFO',

`            `30: 'WARNING',

`            `40: 'ERROR',

`            `50: 'CRITICAL',

`            `100: 'TOSTDOUT'

}

**Public methods:**

*bool log(level, msg, timestamp = ‘None’, istanza=’default’*):

logs a message with specified level. Level can be either an int that represents the code or a string with the level (regardless of the upper or lower case), anything else generates an error and a False return with the message “Level not correct”.

If a timestamp is also passed, this will be the one written in the file, otherwise the timestamp will be generated during the writing phase, be careful if the log message is not immediately written for any reason, the timastamp of the event and the one reported in the log may be different.

If the instance is different from 'default' , the content of the instance is written instead of appName, .

String produced:

yyy-mm-dd hh: mm: ss.ms appName / instance <level> msg

If level is present in an addFilter call no log will be produced.
Return:
True if all went well 
False if something went wrong. 
If it returns false, it stores the error that can be requested with getLastError ()

- *bool addFilter(filter[])*:

  adds one or more filters. 
  Both int and strings can be used, even mixed. 
  If an int or string is not recognized, a False return is generated with the error message “Level% s not correct”, the correct levels are applied instead. 
  Capitalization is not relevant.

`	`Usage:

`	`addFilter ([20,10])

`	`addFilter ([10, "info"])

`	`addFilter (["debug", "INFO"])

`	`Calls to log () with filter = a 20 or 10 will not produce any logs.

`	`Return:

`	`True if all went well

`	`False if something went wrong.

`	`If it returns false, it stores the error that can be requested with getLastError ()

- *bool removeFilter(filter[])*:

  removes one or more filters. 
  Both int and strings can be used, even mixed. 
  If an int or string is not recognized, a False return is generated with the error message “Level% s not correct”, the correct levels are applied instead. 
  Capitalization is not relevant.

`	`Usage:

`	`removeFilter ([20,10])

`	`removeFilter ([10, "info"])

`	`removeFilter (["debug", "INFO"])

`	`Calls to log () with filter = 20 or 10 will now produce logs provided they were first placed 	in an addFilter () call, otherwise everything will remain unchanged.

`	`Return:

`	`True if all went well

`	`False if something went wrong.

`	`If it returns false, it stores the error that can be requested with getLastError ()

- *str getLastError():*

  Return a string with the last error
- *list getFilter():*

  Return a list with the active filters
- *dict getAvailableFilter():*

  Return a dictionary with the available filters.





