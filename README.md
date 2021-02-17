# FastAPI with Opencensus
Purpose : to find a web framwork for building APIs with python that can have all the utilities we need.

## This is a Proof of Concept task, to acheive:
1. Serving a Machine learning model with FastAPI
2. FastAPI Asynchronize function
3. FastAPI integrate with openCensus
4. Having observability of the fastAPI web api in azure Application Insight via opencensus

## topic
### Dataset
- Iris dataset multiclass classification prediction
### Attribute Information:
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
### Model outcome
1. output class:
-- Iris Setosa [0]
-- Iris Versicolour [1]
-- Iris Virginica [2]
## Machine learning type
- Random Forest classifier

## How to use?
- ### In local host (Without docker)
 1. Install all the modules in `requirements.txt` using `pip install -y XXXX`
 2. In the terminal input `python main.py`, then the model API is start running.
 3. Make a request:
 -- 1. click the url ` http://0.0.0.0:8080`, then add `/docs` to enter the openapi swagger, then go the the `/predict` tab and click `Try it out`.
 -- 2. Open another terminal, input `python request.py`. The `request.py` has 2 steps, first, post corresponding json data to the correct url, then request for final output of API to print out as json format.
- ### In local host (with Docker)
1. Follow the `DockerRun.txt` to build and run a docker image contains the API framework.
2. Then follow the same procedure above to make a request.
- ### In web-app
1. In terminal, login using `az acr login --name RAPContainerRegistry`, login name and password can be found on [Azure Portal](https://portal.azure.com/#@GrowNZ4All.onmicrosoft.com/resource/subscriptions/1deb8e42-a405-40d3-bbf2-7624a843e2b4/resourceGroups/rg_rock_dry/providers/Microsoft.ContainerRegistry/registries/RAPContainerRegistry/accessKey)
2. Follow the `DockerRun.txt` to build the docker.
3. Tag the docker image name with following format `docker tag nameOfDockerImage rapcontainerregistry.azurecr.io/fastapi:1.0.6`, `fastapi:1.0.6` means  repository name `fastapi`, tags `1.0.6`, so you can setup any repository name and version you want.
4. use `docker push rapcontainerregistry.azurecr.io/fastapi:1.0.6` to push the image to the RAPContainerRegistry, now you should able to see it in `Repositories` tab.
5. Deploy the specific tags to web app.
6. Go to that web server to start the web app by clicking the URL.
7. Request using `python request_url.py` with correct set up of url.

### Connect to Azure Application Insights
1. Go into the `main.py`, change the `Instrumentation Key` to the corresponding Instrumentation key for your Apllication Insights.
2. Then after you have restart your web app, every time you make a request or a Failed request, you should able to see it in the Application Insights overview or Failures tab.
3. In this case middleware only tracks the tracing of the web app activity, if you need track both log and metrics, here is the setup [MS Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor/app/opencensus-python)

### Alternative request
- Now you can request the model prediction by upload `csv` file using `request_file.py` 
