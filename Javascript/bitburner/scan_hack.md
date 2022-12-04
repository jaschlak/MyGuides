# Scan hack

    This is to be run from the home server or purchased servers.
    
    Cycle through all scanable servers and gain access and hack (if no extra ports needed)
    
## Script

    function canHackServer(ns, hostName)
    {
        if (ns.getServerSecurityLevel(hostName) <= ns.getServerSecurityLevel("home"))
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    export async function doGrow(ns, hostName)
    {
        if (ns.getServerMoneyAvailable(hostName) < ns.getServerMaxMoney(hostName))
        {
            await ns.grow(hostName);
        } 
    }

    export async function doWeaken(ns, hostName)
    {
        if (ns.getServerSecurityLevel(hostName) > ns.getServerMinSecurityLevel(hostName))
        {
            await ns.weaken(hostName);
        }
    }

    export async function main(ns) 
    {
        var hostNames = await ns.scan();

        for (var i=0; i<hostNames.length; i++)
        {
            var hostName = hostNames[i];
            
            if (await ns.hasRootAccess(hostName))
            {
                
                // grow
                await doGrow(ns, hostName);

                // weaken
                await doWeaken(ns, hostName);

                // hack
                await ns.hack(hostName);

            } else
            {
                if (canHackServer)
                {
                    // ports open
                    if (await ns.getServerNumPortsRequired(hostName) == 0)
                    {
                        await ns.nuke(hostName);
                    }
                }
            }
        }
    }