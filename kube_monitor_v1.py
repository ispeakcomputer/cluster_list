#!/usr/bin/python 

import json
import subprocess

context=[]

with open('lab_cluster.txt', 'r' ) as f:
    for linenewline in f:
        line = linenewline[:-1] 
	context.append(line)
		        
for c in context:
    kubecontext="kubectl config use-context" + " " + c
    process = subprocess.Popen(kubecontext.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
					    
    kubenodes="kubectl get nodes"
    process = subprocess.Popen(kubenodes.split(), stdout=subprocess.PIPE)
    nodeoutput, error = process.communicate()
							    
							        
    print(output)
    print("{code}\n" + nodeoutput + "{code}")

