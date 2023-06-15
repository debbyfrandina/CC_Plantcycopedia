# PlantCycopedia API

The PlantCycopedia API is an application developed by Debby Frandina and Vito Ahmad Husein for the Bangkit Capstone Project. It serves as an interface for plant detection using a machine learning algorithm. The API allows users to classify and identify various plant species based on input images.

## Prerequisites

Before running the PlantCycopedia API, ensure you have the following prerequisites installed on your system:

- [Docker](https://www.docker.com/) - For containerization and deployment
- [Google Cloud SDK](https://cloud.google.com/sdk) - For interacting with Google Cloud Platform services

## Running the Application

To run the PlantCycopedia API, follow the steps below:

1. Clone the repository:

```shell
$ git clone https://github.com/debbyfrandina/CC_Plantcycopedia.git
$ cd CC_Plantcycopedia
```

2. Build the Docker image:

```shell
$ docker build -t plantcycopedia-api .
```

3. Run the Docker container:

```shell
$ docker run -p 8080:8080 plantcycopedia-api
```

4. Access the API locally:

Open your web browser and visit `http://localhost:8080`. The API endpoints will be available for use.

## Deployment on Google Cloud Run

To deploy the PlantCycopedia API on Google Cloud Run, perform the following steps:

1. Log in to your Google Cloud account:

```shell
$ gcloud auth login
```

2. Set the default project:

```shell
$ gcloud config set project <your_project_id>
```

3. Enable the Cloud Run and Container Registry services:

```shell
$ gcloud services enable run.googleapis.com containerregistry.googleapis.com
```

4. Build and tag the Docker image:

```shell
$ docker build -t gcr.io/<your_project_id>/plantcycopedia-api .
```

5. Push the Docker image to Google Container Registry:

```shell
$ docker push gcr.io/<your_project_id>/plantcycopedia-api
```

6. Deploy the application on Cloud Run:

```shell
$ gcloud run deploy --image gcr.io/<your_project_id>/plantcycopedia-api --platform managed
```

7. Follow the prompts to configure the deployment options.

8. Once the deployment is complete, you will receive a URL where the PlantCycopedia API is accessible.

## Acknowledgements

The PlantCycopedia API is created by Debby Frandina and Vito Ahmad Husein as part of the Bangkit Capstone Project.

For any inquiries or issues related to the API, please reach out to the developers.

GitHub repository: [CC_Plantcycopedia](https://github.com/debbyfrandina/CC_Plantcycopedia)
