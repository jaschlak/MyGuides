# Splunk queries

    This is a place to drop useful splunk queries
    Note: starting search with metasearch is useful as it prefilters reading from the tsidx files instead of the journal.gz files (compressed)
    
## search queries

    | metasearch host=*<pre_filter_str>*  | search host="<host_name>"

## operational queries

    # see all visible hosts
    | metasearch host=* | stats values(source) by host
    
