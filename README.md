# Cluster List - Get Nodes Output For Multiple Clusters for Kubernetes.  

Simple script to list every single cluster and their nodes in my kuberctl configuration

In the current working state the script output looks like this below. 

This is used for getting an overview of all the clusters I might be looking after.

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

### Installation and running

1. You will need to setup kubectl with the clusters you want to get 'kubectl get nodes' output for. Find you more on doing this at link -> [Install Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
2. You will need to add the cluster names you want this script to run over to the lab_clusters.txt file.
3. Run the script with the below command

```
python3 kube_monitor_v1.py
```




