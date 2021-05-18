# akita-k8s-example

An example that illustrates how to run akita as a sidecar to an exiting application in order to be able to automatically infer API specifications without touching your application's code :)

## What are you getting?

This example is comprised of two APIs (services) that collaborate to deliver todo list type application.

The `todo-service`, stores the todo list items in Redis, and exposes the following endpoints:

- GET /todos - returns a list of todos
- POST /todos - creates a new todo. Expected body is an application/json with the following structure `{"name": "foo", "description": "bar"}`
- DELETE /todos/{id} - deletes a specific item from the list

This service also sends internal requests to the `statistics-service`, which exposes the following endpoints:

- GET /stats - returns the current number of added and deleted todos
- POST /stats - increments the added todo items counter
- DELETE /stats - increments the removed todo items counter

This example is a bit contrived, but it is designed to showcase how Akita can help you not only infer APIs but also understand the outgoing calls from a service.

## Getting started

### Setup akita

You can find detailed instructions specific for this example in this [post](https://www.akitasoftware.com/blog-posts/deep-dive-learning-about-your-api-behavior-on-k8s).

If you want to go solo, please make sure you have Akita setup, as you will need to provide the API Key ID and Secret as well as a service (see documentation [here](https://docs.akita.software/docs/get-started-with-superlearn))

### Running in Kubernetes

The example already provides ready-to-use docker images for the services, so you can jump right to running the example.

#### Running just the services:

You can run the services without Akita with the following steps:

- Setup a Kubernetes cluster (you can use something like microk8s or minikube to run a cluster locally)
- Run `kubectl apply -f service.yaml`
- View the exposed port for the created service by running `kubectl get services`
- Use curl, postman or any other tool to send requests to `http://localhost:30123/todos`

#### Running Akita as a sidecar to the todo-service:

Create a new Kubernetes secret to hold the Akita credentials:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: akita-secrets
type: Opaque
data:
  api-key-id: # REPLACE WITH YOUR API KEY ID BASE 64 ENCODED
  api-key-secret: # REPLACE WITH YOUR API KEY SECRET BASE 64 ENCODED
```

Remember that the credentials are base64 encoded.

Save it on a file named: `akita-secrets.yaml` and run `kubectl apply -f akita-secrets.yaml`

Run `kubectl apply -f service-with-akita.yaml` Note that the default service name being used is `k8s-integration`, so please ensure you have an Akita service with that name.

### Troubleshooting:

- On microk8s you may have to enable DNS by running `microk8s enable dns` this may be required if your pod is not able to connect to the Internet
