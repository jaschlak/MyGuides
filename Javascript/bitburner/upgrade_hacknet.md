# Upgrade Hacknet

    This is to upgrade the hacknets whenever money is available
    
## upgrade_hacknet.md Script

    export async function upgradeNodeLevel(ns, node)
    {
        if (ns.hacknet.getLevelUpgradeCost(node) <= ns.getServerMoneyAvailable('home'))
        {
            ns.hacknet.upgradeLevel(node);
        }
    }

    export async function purchaseNewNode(ns, node)
    {
        if (ns.hacknet.getPurchaseNodeCost() <= ns.getServerMoneyAvailable('home'))
        {
            ns.hacknet.purchaseNode();
        }
    }

    export async function upgradeNodeRam(ns, node)
    {
        if (ns.hacknet.getRamUpgradeCost(node) <= ns.getServerMoneyAvailable('home'))
        {
            ns.hacknet.upgradeRam(node);
        }
    }

    export async function upgradeNodeCore(ns, node)
    {
        if (ns.hacknet.getCoreUpgradeCost(node) <= ns.getServerMoneyAvailable('home'))
        {
            ns.hacknet.upgradeCore(node);
        }
    }

    export async function main(ns) 
    {
        //ns.tprint(ns.hacknet.numNodes());
        while (true)
        {
            for (var i=0; i<await ns.hacknet.numNodes(); i++)
            {
                //var nodeName = ns.hacknet.getNodeStats(i)['name'];

                // await ns.hacknet.upgradeLevel(i);
                // upgrade level
                await upgradeNodeLevel(ns,i);

                // upgrade ram
                await upgradeNodeRam(ns,i);

                // upgrade cores
                await upgradeNodeCore(ns,i);

                // purchase node
                await purchaseNewNode(ns,i);

            }
            await ns.sleep(1000);
        }
    }