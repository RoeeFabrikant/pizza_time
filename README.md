# Pizza Time web application

<p align="center"><img alt="kind" src="https://media.giphy.com/media/h7Nr5t3chWq1HpvfxB/giphy.gif" width="300px" /></p>

Pizza Time is a Python Flask web application that will help you to order your favorite pizza!

# Architecture:

### Please find the architecture diagram [here](./files/Pizza_time_arch.png)

# Installation and usage

## Run locally:

Prerequisites:
- Python
- Install the required python packages using the command:
`pip install -r requirements.txt`

How to run:
- Clone the repository
- Run the command: `flask run`

The application will expose port `8080` on your local machine.

Usage:

To place new pizza order send http POST request to the application:

```
curl -X POST -d "pizza_type=napolitana&size=fammily&amount=3" http://localhost:8080/order
```

## Run with Kind:

kind is a tool for running local Kubernetes clusters using Docker container "nodes".

Prerequisites:
- Docker ([install guide](https://docs.docker.com/get-docker/))
- Kind ([install guide](https://kind.sigs.k8s.io/docs/user/quick-start/#installation))

How to run:
- Clone the repository
- Run the following kubectl command to create the kubernetes cluster and application pods:

```
kubectl apply -f ./k8s/kind_cluster.yaml
```

```
kubectl apply -f ./k8s/pizza_time_k8s.yaml
```

The application will expose port `30646` on your local machine.

Usage:

To place new pizza order send http POST request to the application:

```
curl -X POST -d "pizza_type=napolitana&size=fammily&amount=3" http://localhost:30646/order
```

To check the application health:
```
curl http://localhost:30646/health
```

To ping the application:
```
curl http://localhost:30646/ping
```

# Docker Image
The application has a ready Docker image you can use:

[roeef/pizza_time](https://hub.docker.com/r/roeef/pizza_time)

# Tests

You can test Pizza time application using pytest:
- Clone the repository
- From the main folder run the `pytest` command

# Contributions

Contributions are welcomed. Please use the below as a guideline
for your input.

1. Fork the repository
2. Document your planned change
3. Write your test
4. Test your changes using pytest
5. Submit a pull request 
6. Assign a reviewer
7. Sit back and wait for your awesome code to be merged

## License and Authors

### Authors

- [Roee Fabrikant](roee73@gmail.com)