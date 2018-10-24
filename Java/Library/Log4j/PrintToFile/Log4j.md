
# Log4j How To:

## Create your Java Project inside Eclipse

## Setup

Download the latest log4j .jar file from https://logging.apache.org/log4j/1.2/download.html
Move the file to a comfortable place (maybe a lib folder inside your Java Project)
Add log4j.jar to buildpath

## Create a log4j.properties file

Make sure it is either in the src folder or you add it to the build path
here is an example
    
    # Log4j Hierarchy
    # TRACE < DEBUG < INFO < WARN < ERROR < FATAL

    # Define the root logger with appender file
    log = <File path>
    log4j.rootLogger = DEBUG, FILE

    # Define the file appender
    log4j.appender.FILE=org.apache.log4j.FileAppender
    log4j.appender.FILE.File=${log}/<New log file name>

    # Define the layout for file appender
    log4j.appender.FILE.layout=org.apache.log4j.PatternLayout
    log4j.appender.FILE.layout.conversionPattern=%d [HH:mm:ss] %5p [%t] - %c.%m %m%n
    
## add to your java class:

    package <package name>;
    import org.apache.log4j.Logger;

    import java.io.*;
    import java.sql.SQLException;

    public class <class name>
    {

        static Logger log = Logger.getLogger(<class name>.class);

        public static void main(String[] args)throws IOException,SQLException

        {
          log.debug("<message you want to send>");
          log.info("Hello this is an info message");
        }

    }
