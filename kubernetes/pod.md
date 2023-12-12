# Kubernetes Pod

    Pods
    
## Get Pod Commands

    kubectl get pod                                                                     # get all pod details in default namespace
    kubectl get pod -n <namespace>                                                      # get all pods within namespace
    kubectl wait --for=condition=Ready pods --all -n <namespace> --timeout=180s         # wait 180 seconds for all pods in namespace to become available    