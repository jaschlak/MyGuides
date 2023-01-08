# Recursive Hack

	This uses recursion to propogate accross the network and hack the nodes that we have access.
	Future: run local_hack.js from home directory on all nodes with root access
	
## recursive_hack.js

    export async function openPorts(ns, hostName)
    {
        var srvAttr = await ns.getServer(hostName);

        if (srvAttr['openPortCount'] <= srvAttr['numOpenPortsRequired'])

        if (ns.fileExists('bruteSSH.exe','home')) 
        {
            await ns.brutessh(hostName);
        };

        if (ns.fileExists('FTPcrack.exe','home')) 
        {
            await await ns.ftpcrack(hostName);
        };

        if (ns.fileExists('relaySMTP.exe','home')) 
        {
            await ns.relaysmtp(hostName);
        };
        if (ns.fileExists('HTTPWorm.exe','home')) 
        {
            await ns.httpworm(hostName);
        };
        if (ns.fileExists('SQLinjection.exe','home')) 
        {
            await ns.sqlinject(hostName);
        };
    }

    function canHackServer(ns, hostName)
    {
        var serverAttr = ns.getServer(hostName);
        // if hacking level large enough and ports open
        if (ns.getServerSecurityLevel(hostName) <= ns.getHackingLevel())
        {
            if(serverAttr['numOpenPortsRequired'] <= serverAttr['openPortCount'])
            {
                return true;
            } else
            {
                openPorts(ns,hostName);
            }
        }
        else
        {
            return false;
        }
    }

    export async function doGrow(ns, hostName)
    {
        if (await ns.getServerMoneyAvailable(hostName) < await ns.getServerMaxMoney(hostName))
        {
            await ns.grow(hostName);
        } 
    }

    export async function doWeaken(ns, hostName)
    {
        if (await ns.getServerSecurityLevel(hostName) > await ns.getServerMinSecurityLevel(hostName))
        {
            await ns.weaken(hostName);
        }
    }



    export async function scanServer(ns,processList,processedList) {

        //filtering specified nodes
        while (processedList.includes(processList[0]))
        {
            processList.shift();
        }

        // scan current node and add to list to process
        var newScan = ns.scan(processList[0])
        processList = processList.concat(newScan);

        //filtering specified nodes (in case process servers crept in)
        while (processedList.includes(processList[0]))
        {
            //ns.tprint('True stuff right here');
            processList.shift();
        }

        if (processList.length > 0) {

            // print node and list to process
            /*
            ns.tprint(processList[0]);
            ns.tprint(processList);
            ns.tprint(processedList);
            ns.tprint('');
            */

            // start process //

            var hostName = processList[0];

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
                if (canHackServer(ns,hostName))
                {
                    await ns.nuke(hostName);
                }
            }

            // end process //

            //ns.tprint('attempting to push');
            processedList.push(processList.shift()); 

            // call function again
            await scanServer(ns,processList,processedList);
        }
    }

    /** @param {NS} ns */
    export async function main(ns) 
    {
        ns.disableLog('scan');
        ns.disableLog('getServerMoneyAvailable');
        ns.disableLog('getServerMaxMoney');
        ns.disableLog('grow');
        ns.disableLog('getServerSecurityLevel');
        ns.disableLog('getServerMinSecurityLevel');
        ns.disableLog('weaken');
        ns.disableLog('getServerNumPortsRequired');
        
        while(true)
        {
            var processList = await ns.scan('home');
            processList = ['iron-gym'];
            var processedList = ['home','ps_node1','ps_node2','ps_node3','ps_node4','CSEC','undefined'];
            await scanServer(ns,processList,processedList);
            //ns.sleep(1000);
        }
    }