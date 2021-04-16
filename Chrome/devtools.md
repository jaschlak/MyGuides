# DevTools

	Help on DevTools searches
	
## Console

### Find element by xpath, print all items

	$x('//*[@class="<class name>"]/<extended path>').forEach(function(el){console.log(el.<attribute to be printed>)})
	$x('//*[@class="form-horizontal"][2]/div/div/select/option').forEach(function(el){console.log(el.value)})