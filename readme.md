This repository contains Python scripts for AWS Automation. Scripts which are tested and were approved to use in production will be tagged with a comment in start of each script....

Config Settings:
\# ` tiller -listen=localhost:8080`  --> Set this if tiller running on localhost
\# `export HELM_HOST=:8080`
\# `export TF_LOG=TRACE`  --> For terraform Debug log
\# `export TF_LOG_PATH=./terraform.log`  --> To set terraform Logfile path
Create a Cluster Role Binding:
\# ` kubectl create clusterrolebinding cluster-system-anonymous --clusterrole=cluster-admin --user=system:anonymous `

Get your jenkins 'admin' user password by running:
```
   # printf $(kubectl get secret --namespace default <secret_name> -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode);echo 
  ```
Get your jenkins URL by running:
```
# export SERVICE_IP=$(kubectl get svc --namespace default krishna-jenkins --template "{{ range (index .status.loadBalancer.ingress 0) }}{{ . }}{{ end }}") `
# echo http://$SERVICE_IP:8080/login
```
