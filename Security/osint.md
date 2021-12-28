# OSInt

    Sites,links, and tools for osint

## People lookup

    webmii.com                              # lookup first and last name, nickname:optional
    whois.net                               # lookup dns name 

## Dorking (needs it's own section)

    http://www.googleguide.com/advanced_operators_reference.html
    
    intext:<param>                          # filter by something in text
    site:<param>                            # filter by domain
    site:-.com                              # filter out all .com results
    inurl:<param>                           # filter by url contains
    allinurl: <word1> <word2>               # filter to detect multiple works in url
    filetype:<param>                        # filter by filtetype
    cache:<website url>                     # display cached version of website
    info:<website url>                      # search info about url
    link:<website url>                      # find sites that have your link in it
    intitle:<param>                         # find word in title
    allintitle: <word1> <word2>             # filter multiple words in title
    
    
## External Resources

### All-In-One Guides
    https://github.com/F3dai/OSINT-Resources                                                                                            # all sorts of tools
    https://cdn.discordapp.com/attachments/607679536741613599/920213433700458536/Complete_List_of_OSINT_Web_Resources_Light_ohshint.pdf # pdf of all sorts of tools (looks like a lot of content)
    https://cdn.discordapp.com/attachments/607679536741613599/918375440765313055/1_Complete_Bookmarks_Organized_8-12-2021_ohshint.html  # someones volunteer bookmarks
    https://github.com/OhShINT/ohshint.gitbook.io/tree/main/Lists_of_OSINT_Web_Resources                                                # another repo of tools
    
### Language Translators

    https://www.deepl.com/en/translator
    https://translate.yandex.com/
    https://translation2.paralink.com/

### Social Media

    http://sleepingtime.org/                                                                                                            # sleep time of people on twitter
    https://twitch-tools.rootonline.de/channel_previews.php                                                                             # twitch lookup
    https://rhematt.github.io/Snap-Scraper/                                                                                             # find snapchat story content by geolocation
    
### Dox Tools (information consolidation)

    https://pdfmapmaker.com/                                                                                                            # simple map maker
    https://rateourcops.org/                                                                                                            # police rating (20211228 little info)
    https://infosecsherpa.medium.com/investigating-charities-c3950eb6dc7                                                                # lookup charities before donating
    https://www.mobilephonemuseum.com/catalogue/                                                                                        # old phone model lookup
    https://github.com/sharsil/mailcat                                                                                                  # repo for finding emails of users by nickname
    https://github.com/smicallef/spiderfoot?ref=d                                                                                       # map client attack surface
    https://dataportals.org/search                                                                                                      # free GIS data lookup (usually from governments)
    https://geohack.toolforge.org/                                                                                                      # maps/weather/flight/maritime/fitnessdevice data by lat/long
    https://animal.toolpie.com/                                                                                                         # detect animal by pic
    https://logo.toolpie.com/                                                                                                           # detect logo by pic
    https://plant.toolpie.com/                                                                                                          # detect plant by pic
    https://colorize.toolpie.com/                                                                                                       # turn black and white image to color
    https://age.toolpie.com/                                                                                                            # detect age by faceshot
    https://facecomparison.toolpie.com/                                                                                                 # compare faces by faceshot
    https://landmark.toolpie.com/                                                                                                       # detect landmark by image
    https://webmii.com/                                                                                                                 # ML lookup by first and last name (optional:keywords)
    
### Scam Recon

    https://scamsearch.io/                                                                                                              # scam database
    
### Tips and Tricks

    https://freedom.press/training/locking-down-signal/                                                                                 # article on how to lockdown signal
    
### Informational Articles

    https://cdn.discordapp.com/attachments/607679536741613599/916907561641467995/Art-17-We-Know-Where-You-Are.pdf                       # Cell tower tracking
    https://osintcurio.us/2021/11/29/staying-up-to-date-with-osint-content/                                                             # simple osint guide
    https://sector035.nl/articles/chronolocation-of-media                                                                               # exif -> chronological events    
    
### Informational Videos

    https://youtube.com/watch?v=eis1F10H0KI                                                                                             # bypass Instragram Selfie Verification
    
### Tips and Tricks (written)

    bypass Instagram login dialog box
    1) locate in dev tools <body> tag
        a) remove "overflow:hidden;"
    2) locate <div clas"RnEpo Yx5HN" role="presentation">
        a) delete element