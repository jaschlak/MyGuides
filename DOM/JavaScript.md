# Random JavaScript References

    This can be used as a collection point for commands. When it grows to big my intention is to clean this out and properly categorize them
    
## Call the first "button" from html and add/remove/toggle a class to it in order to make it invisible:

    
    document.querySelector("button").classList.add("invisible");
    document.querySelector("button").classList.remove("invisible");
    document.querySelector("button").classList.toggle("invisible");
    
#### Note: the following need to exist for this to work

    CSS:
    
    Creates the invisible style
    .invisible{
      visibility: hidden;
    }

    HTML:
    
    Links the javascipt and css files to html
    <script src="index.js" charset="utf-8"></script>
    <link rel="stylesheet" href="styles.css">