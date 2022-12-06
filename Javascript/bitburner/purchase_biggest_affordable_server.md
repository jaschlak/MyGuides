# Purchase Biggest Affordable Server

	Identify the most expensive server you can purchase (ram) and buy it
	
## purchase_biggest_affordable_server.js 

	export async function main(ns) 
	{
		var n_power = 0;
		var ram_base = 2;

		var money_available = await ns.getServerMoneyAvailable('home');

		var purch_ram = 0;
		var purch_cost = 0;

		// cycle through ram possibilities and find the max you can afford
		for (var n=0; n<20; n++)
		{
			var ram_value = Math.pow(ram_base,n);
			var server_cost = await ns.getPurchasedServerCost(ram_value);

			if (server_cost < home_available)
			{
				purch_ram = ram_value;
				purch_cost = server_cost;
			} else
			{break;}
		}

		var numPurchasedServers = await ns.getPurchasedServers().length + 1;
		var purchaseHostName = 'ps_node' + numPurchasedServers;
		
		ns.tprint('purchasing server ' + purchaseHostName + ' with ram ' + purch_ram + ' for ' + purch_cost);
		await ns.purchaseServer(purchaseHostName,purch_ram);

	}