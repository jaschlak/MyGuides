# CMD Commands for scrapy

    Commands for Scrapy from the command prompt
    
## benchmark how well scrapy works on your machine

    scrapy bench
    
## fetch contents of website

    scrapy fetch --nolog <insert site url>
    
## see scrapy settings you have changed

    scrapy settings
    
## see scrapy version

    scrapy version
    
## view contents of website

    scrapy view <insert site url>
    
## see scrapy components before crawling without python IDE

    scrapy shell <insert site url>
    
## options from the shell

    crawler
    item
    request
    response
    response.status
    response.url
    response.body
    response.css('<insert css section>')
    response.css('title')                   # returns selecter
    response.css('title').extract()         # dump all contents
    response.css('title::text').extract()   # dump only text
    response.css('.author')                 # selects only author classes from the page
    response.css('.author').extract()       # get all authors on page
    type(response('.author'))               # show type
    
    response.css('.author').extract()[0]    # extract first item
    response.css('.author'.extract_first()  # extract first item
    response.css('.author::text').extract() # extract all text of authors    
    
    settings
    settings.get('BOT_NAME')
    spider
    fetch('<website url>')
    from pprint import pprint               # you can import other python libraries
    pprint(response.headers)                # see headers from the site
    view(response)
    shelp()                                 #shows commands available from shell
    exit()
    
# parse contents of downloaded file:

    scrapy shell file:///<filepath>
    
## specify hierarchy between classes

    response.css('.quote > .text').extract()
    
## select all links on website

    response.css('a::attr(href)').extract()
    
## xpath

    response.xpath('/html/head/title').extract()
    response.xpath('//title').extract()
    response.xpath('//*[@id="maincontent"]/div[2]/span/section[2]/div/div/div[1]').extract()            # coppied from element inspection in chrome
    response.xpath('//*[@id="maincontent"]/div[2]/span/section[2]/div/div/div[1]/text()').extract()     # text only
    response.xpath("//span[@class='text']").extract()                                                   # select only elements with a text class
    response.xpath("//span[@class='text']/text()").extract()                                            # select the text from those elements
    
## shell regex

    scrapy shell https://www.axosbank.com/
    response.xpath("//*[contains(text(), 'friend')]/text()")                                            # selects any section that has the text "friend", * indicated we were interested in all tags
    response.xpath("//*[contains(text(), 'friend')]/text()").extract()                                  # same but full text
    response.xpath(".text:contains(text(), 'friend')::text").extract()                                  # same but only quotes that contain friend
    
## combine normal selection with regex

    response.css('.author::text').re('A[a-z]*\s\w+')                                                    # extracts authors and then regexes for filtered results
    respone.xpath("//*[@class='author'][starts-with(text(), 'A')]/text()").extract()                    # filters for all authors that start with A
    
    