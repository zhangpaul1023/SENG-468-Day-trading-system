# Deployment

Spin-up service.
```sh
# Ensure the machine is running in Swarm mode.
docker swarm init

# Create registry service.
docker service create --name registry --publish published=5000,target=5000 registry:2

# Push stack to registry.
docker-compose push

# Deploy stack to Swarm.
docker stack deploy --compose-file docker-compose.yaml transaction_service

# Check stack status.
docker service ls
```

Take down service.
```sh
docker stack rm transaction_service
docker service rm registry
docker swarm leave --force
```