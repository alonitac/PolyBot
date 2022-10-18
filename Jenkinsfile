pipeline {
    agent any

    environment {

        REGISTRY_URL = "352708296901.dkr.ecr.us-east-1.amazonaws.com"
        IMAGE_TAG = "0.0.${BUILD_NUMBER}"
        IMAGE_NAME = "shaypolybotecr"

    }
    stages {
        stage('Build Bot app') {
            steps {
                sh """
                    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${REGISTRY_URL}
                    docker build -t ${IMAGE_NAME} .
                    docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${REGISTRY_URL}/${IMAGE_NAME}:${IMAGE_TAG}
                    docker push ${REGISTRY_URL}/${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }
        stage('Stage II') {
            steps {
                sh 'echo "stage II..."'
            }
        }
        stage('Stage III ...') {
            steps {
                sh 'echo echo "stage III..."'
            }
        }
    }
}
