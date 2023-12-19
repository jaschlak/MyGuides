# Command Prompt Java Heap Settings

    Useful command prompt diagnostic tools
    
# View Java Heap Size for machine

    java -XX:+PrintFlagsFinal -version | findstr /i "HeapSize PermSize ThreadStackSize"
    
# Change Java Heap size for machine

    set JAVA_OPTS="-Xms2048m -Xmx4096m"