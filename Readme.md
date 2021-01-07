 # Load balancing Sample

 #### How to use :
 - To launch the APP, just open a terminal, go inside the unzipped folder, at the same level with docker-compose.yml, and execute : docker-compose up
 - This will spin up the dockerised architecture. After that, you need to open a browser and tape : http://localhost:8080
 - It will redirect 60% traffic to app1 and 40% traffic to app2.
 - To quit, you can just CTRL + C in the terminal and it will stop the application and destroy the created containers.

https://towardsdatascience.com/sample-load-balancing-solution-with-docker-and-nginx-cf1ffc60e644
https://docs.docker.com/compose/gettingstarted/

Flask Session - https://www.youtube.com/watch?v=lvKjQhQ8Fwk

#### Gateway Network

```
docker network inspect bridge
```

Gateway network IP 172.17.0.1

This explains the nginx load balancing configuration

https://docs.docker.com/network/network-tutorial-standalone/#use-the-default-bridge-network