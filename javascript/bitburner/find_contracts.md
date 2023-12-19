
# Find Contracts
    
    This script is used to find what servers have contract files (or cycle servers and find condition)
    
## Code

    /** @param {NS} ns */
    export async function main(ns) {

        
        var toscan_list = [];
        var server_json = JSON.parse('{}');
        var hostName = 'home';

        var scanned_list = [hostName,'ps_node1','ps_node2','unknown','darkweb'];

        var current_scan_list = await ns.scan(hostName)
        server_json[hostName] = current_scan_list;

        
        toscan_list = toscan_list.concat(current_scan_list)

        var i = 0
        while (toscan_list.length>0)
        {

            hostName = toscan_list[0];

            var check_file_list = ns.ls(hostName,'.*\.cct');

            if (check_file_list.length > 0)
            {
                ns.tprint('host: ' + hostName);
                ns.tprint('local file list is: ' + check_file_list);
            }

            // if hostname in scanned list, remove and continue loop
            if (scanned_list.includes(hostName))
            {
                // removing hostname from toscan list
                toscan_list = toscan_list.filter(function(value,index,array){return value != hostName});
                continue;
            } else
            {
                //ns.tprint(hostName);
                current_scan_list = await ns.scan(hostName);
                toscan_list = toscan_list.concat(current_scan_list);

                // removing hostname from toscan list
                toscan_list = toscan_list.filter(function(value,index,array){return value != hostName});
                scanned_list.push(hostName);
            }

            // handle inf loop
            i++;
            if (i > 1000)
                {ns.tprint('ending inf loop');
                break
            };

        }

        //ns.tprint('ended while loop');

    }