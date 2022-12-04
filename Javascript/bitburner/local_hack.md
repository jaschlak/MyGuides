# Local Hack

    This is a local script to be distributed out to all servers you have root access to and run
    
## Script

    export async function main(ns) 
    {
        while(true)
        {
            await ns.grow(ns.getHostname());
            await ns.weaken(ns.getHostname());
            await ns.hack(ns.getHostname());
        }
    }