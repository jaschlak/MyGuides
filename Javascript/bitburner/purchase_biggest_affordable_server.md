# Purchase Biggest Affordable Server

	Identify the most expensive server you can purchase (ram) and buy it
	
## purchase_biggest_affordable_server.js 

	var n_power = 0;
	ram_base = 2;

	var home_available = getServerMoneyAvailable("home");

	var purch_ram = 0;
	var purch_cost = 0;
	for (n=0; n<=20; n++)
	{
		var ram_value = Math.pow(ram_base,n)
		var server_cost = getPurchasedServerCost(ram_value);
		
		if (server_cost < home_available)
		{
			purch_ram = ram_value;
			purch_cost = server_cost;
		}
	}

	var numPurchasedServers = getPurchasedServers().length +1;

	var purchase_hostname = 'ps_node' + numPurchasedServers;

	tprint('purchasing server ' + purchase_hostname + ' with ram ' + purch_ram + ' for ' + purch_cost);
	purchaseServer(purchase_hostname,purch_ram)
