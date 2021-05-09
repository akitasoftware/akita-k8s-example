# akita-k8s-example

An example that illustrates how to run akita as a sidecar to an exiting application in order to be able to automatically generate API specifications without touching your application's code :)

## What you are getting

This example is comprised of a simple todo list application written in python. The application exposes three endpoints:

- GET /todos - returns a list of todos
- POST /todos - creates a new todo. Expected body is an application/json with the following structure `{"name": "foo", "description": "bar"}`
- DELETE /todos/{id} - deletes a specific item from the list

## Getting started

### Setup akita

TODO

### Running the Kubernetes service

1 - Setup a Kubernetes cluster (you can use something like microk8s or minikube to run a cluster locally)
2 - Run `kubectl apply -f service.yaml`
3 - View the exposed port for the created service by running `kubectl get services`
4 - Use curl, postman or any other tool to send requests to `http://localhost:{exposed-port}/todos`

### Running locally

### Troubleshooting:

- On microk8s you may have to enable DNS by running `microk8s enable dns` this may be required if your pod is not able to connect to the Internet

## TODO:

- Remove the secrets from the service.yaml
