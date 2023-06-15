# PlantCycopedia API

## Project Description

PlantCycopedia API is an application developed for the Bangkit Capstone Project. It utilizes machine learning algorithms to enable plant detection and classification. The API serves as an interface for users to upload plant images and receive information about the detected plant species.

This project was created by Debby Frandina and Vito Ahmad Husein as part of the Bangkit Capstone Project, demonstrating their skills and knowledge gained throughout the program.

## Features

- Plant detection and classification based on uploaded images.
- Provides information about the detected plant species.

## Technologies Used

- Machine Learning (ML) algorithms
- Express.js
- Docker
- Google Cloud Run
- Google Cloud SDK

## Getting Started

### Prerequisites

Before running the PlantCycopedia API, ensure you have the following prerequisites installed on your system:

- Docker
- Google Cloud SDK

### Installation and Setup

1. Clone the repository:

```shell
$ git clone https://github.com/debbyfrandina/CC_Plantcycopedia.git
$ cd CC_Plantcycopedia
```

2. Build the Docker image:

```shell
$ docker build -t plantcycopedia-api .
```

### Running the Application

To run the PlantCycopedia API locally, follow these steps:

1. Run the Docker container:

```shell
$ docker run -p 8080:8080 plantcycopedia-api
```

2. Access the API locally:

Open your web browser and visit `http://localhost:8080`. The API endpoints will be available for use.

### Deployment on Google Cloud Run

To deploy the PlantCycopedia API on Google Cloud Run, follow these steps:

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

## Contributing

Contributions to the PlantCycopedia API project are welcome. If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request on the GitHub repository.

## License

The PlantCycopedia API project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or further information, please contact the project developers:

- Debby Frandina: [Email](mailto:debbyfrandina@debbyfrandina.com)
- Vito Ahmad Husein: [Email](mailto:vitoahmadhusein@gmail.com)

GitHub repository: [CC_Plantcycopedia](https://github.com/debbyfrandina/CC_Plantcycopedia)
