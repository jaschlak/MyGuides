# Kubernetes General Commands

    Quick documentation during AWS gameday (may already have a guide but was not sticking out)
    Tutorial followed: https://build-14d24a4.eksworkshop.com/docs/introduction/getting-started/first
    
## Get Commands

    kubectl get nodes                                                                           # node details (lookup id) in default namespace
    kubectl get pods                                                                            # pod details in default namespace
    kubectl get namespaces                                                                      # namespace details
    kubectl get svc -n <namespace>                                                              # details on services in namespace
    kubectl logs -n catalog <type>/<namespace>                                                  # get logs for type of yaml/namespace
    
    kubectl -n <namespace> exec -it <type>/<namespace> -- curl <url route> | jq .               # execute curl command inside (pretty print json)
    
## Apply Commands
    
    kubectl apply <yaml file path>
    kubectl apply -k <directory with all yamls>
    
    kubectl scale -n <namespace> --replicas <number to scale to (int)> <type>/<namespace>       # scale to number of nodes for type/namespace    