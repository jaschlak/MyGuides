
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
    log4j.rootLogger = DEBUG, toConsole, toFile

    #Console
    log4j.appender.toConsole = org.apache.log4j.ConsoleAppender
    log4j.appender.toConsole.layout = org.apache.log4j.PatternLayout
    log4j.appender.toConsole.layout.ConversionPattern = %d{HH:mm:ss} %5p [%t] - %c.%M - %m%n

    #DailyRollingFile
    log4j.appender.toFile = org.apache.log4j.DailyRollingFileAppender
    log4j.appender.toFile.File = ./<filepath>/<file name>.log
    log4j.appender.toFile.DatePattern = '.'yyyy-MM-dd
    log4j.appender.toFile.layout = org.apache.log4j.PatternLayout
    log4j.appender.toFile.layout.ConversionPattern = %d %5p [%t] - %c.%M %L - %m%n
    
## add to your java class:

Here is an example

    package <package name>;
    import org.apache.log4j.Logger;

    import java.io.*;
    import java.sql.SQLException;

    public class <class name>
    {

        static Logger log = Logger.getLogger(<class name>.class);

        public static void main(String[] args)throws IOException,SQLException

        {
            try 
            {
                throw new Exception("<exception text>");
                
            } catch (Exception e) 
            {
                log.error(e);
            }
        }

    }
