# WhatApp Messenger Container for Kubernetes Cluster
Whatsapp Messenger that can be deployed in a Kubernetes cluster. This is tested on GKE

It accepts phone number and message as query parameters and sends the whatsapp message to the specified mobile number without having to add it as a contact on the phone. Attachments and Bulk Messaging are not yet handled but they can be handled as developed [here](https://github.com/kgsatish/whatsapp-direct-bulk/).

Refer to requirements.txt for the dependencies.
 
## Installation

To create selenium-chrome image in Google artifact registry
```
docker pull selenium/standalone-chrome
docker tag selenium/standalone-chrome <region>-docker.pkg.dev/<project-id>/<repository>/selenium-chrome
docker push <region>-docker.pkg.dev/<project-id>/<repository>/selenium-chrome
```
To create whatsapp messenger image in Google artifact registry
```
docker build . --tag whatsapp:latest
docker image tag whatsapp <region>-docker.pkg.dev/<project-id>/<repository>/whatsapp
docker push <region>-docker.pkg.dev/<project-id>/<repository>/whatsapp
```

After the images are created, deploy them in GKE into 'whatsapp-cluster' and create a workload 'whatsapp' following the steps mentioned [here](https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app).
1. Deploy both the images as two containers in the same pod (using 'Workloads' deploy in 'Kubernetes engine' navigation link in the Google console)
2. Expose 4444:4444, 7900:7900 and 8080:8080 ports. 4444 is the Selenium Grid port where the WebDriver calls are made and 7900 is the noVNC port to see what is happening inside the selenium-chrome container. 8080 port is the WhatsApp Messenger port invoked using http://\<external ip\>:8080

## Usage
Get the external ip from clusters->whatsapp-cluster->overview and then, invoke http://\<external ip\>:8080 in the browser. Login to http://\<external ip\>:7900 with 'secret' as the password. You will see the whatsapp login screen with QR code displayed. Scan the QR code using whatsapp -> linked devices from your mobile to login.  

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Reach me on satishkg@yahoo.com for any queries

## Roadmap
Enable for images. Video, audio, document attachments yet to be implemented. Enable for bulk messaging. Also, tested only against Indian mobile numbers. International numbers yet to be tested. You are welcome to chip in if interested.

## License
[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
