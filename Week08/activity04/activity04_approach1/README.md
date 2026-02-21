## Assignment
Week 8 - Activity 4: Docker _ multi-container  (deadline by next week). 
Run a project (either a Car Rental System or a CV Analysis project) using a multi-container architecture (by next week).  
Help link: https://docs.docker.com/get-started/docker-concepts/running-containers/multi-container-applications/

### Second approach
Just for demonstration purpose, this approach uses two Dockerfile 

### Running the application
First: build the two images 
`docker build -t cars-db ./db`
`docker build -t cars-cli ./cli`

Second: create the network
`docker network create cars-network`

Third: create the volume
`docker volume create cars-data`

Finally, run the application
```
docker run --rm -it \
  --name cli \
  --network cars-network \
  -v cars-data:/data \
  -v $(pwd)/cli:/app \
  -v $(pwd)/db:/db \
  cars-cli
```
