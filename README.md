# list_every_kubernetes_cluster
Simple script to list every single cluster and there nodes in my kuberctl configuration

# Cluster List - Get Nodes Output For Multiple Clusters for Kubernetes.  

Currently switching between clusters or "context" and outputs "kubectl get nodes" results.

In the current working state the script output looks like this. 

``` 
working on contextalbqurqurque-01
Switched to context "albqurqurque-01".

NAME            STATUS    ROLES     AGE       VERSION
22.43.175.131   Ready     <none>    1y        v1.2.6
22.43.175.132   Ready     <none>    1y        v1.2.6
22.43.175.133   Ready     <none>    1y        v1.2.6
22.43.175.134   Ready     <none>    1y        v1.2.6

working on context anvil
Switched to context "anvil".

NAME             STATUS    ROLES     AGE       VERSION
234.30.183.132   Ready     <none>    216d      v1.6.4+coreos.0
```



