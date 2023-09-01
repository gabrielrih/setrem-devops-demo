# setrem-devops-demo
DevOps demo activity

# Index
- [Dependencies](#dependencies)
- [How to start the web site](#how-to-start-the-web-site)
- [How to run tests](#how-to-run-tests)
- [How to change web tests on cypress](#how-to-change-web-tests-on-cypress)
- [Deploying on K8S](#deploying-on-k8s)
- [Documentation](#documentation)

## Dependecies
To use this repository we must have install [docker](https://docs.docker.com/get-docker/) and [cypress](https://docs.cypress.io/guides/overview/why-cypress). Please, install it according to your OS.


## How to start the web site

Starting the web site:
```sh
cd docker
docker compose up --build -d
```

To open it:

[http://localhost:5000](http://localhost:5000)


## How to run tests

### Unit tests

Press F1, _Tasks: Run task_ and then _Run unit tests_.

### Integration and web tests

> First of all, we must install cypress on Linux or WSL.

To install it on the current repo:
```sh
npm install cypress --save-dev
```

> More information for installing it on [Windows](https://www.browserstack.com/guide/how-to-install-cypress-for-windows).

Press F1, _Tasks: Run task_ and then _Run integration tests_.

## How to change web tests on cypress

To start cypress to create on modify tests:
```sh
./node-modules/.bin/cypress open
```

Now we can create your tests.

## Deploying on K8S

Make sure you are on the current context:
```sh
kubectl config current-context
```

Then you can apply the resources on K8S using this command:
```sh
kubectl apply -f ./k8s/resources.yml
```

To verify if it's working you can run a get command to see the services and the pods.
```sh
kubectl get deployments
kubectl get services
```

Finally, we can undo the deploy:
```sh
kubectl delete -f ./k8s/resources.yml
```

## Documentation

Extra tools:
- [Codecov](https://app.codecov.io)
- [SonarCloud](https://sonarcloud.io)
- [Docker hub](https://hub.docker.com/repository/docker/gabrielrih/devops-demo-app)

Cypress docs:
- [Testing your app](https://docs.cypress.io/guides/end-to-end-testing/testing-your-app)
- [cypress new window](https://testersdock.com/cypress-new-window/)
- [Navigation](https://example.cypress.io/commands/navigation)
- [get command](https://docs.cypress.io/api/commands/get)