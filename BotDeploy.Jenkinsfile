pipeline {
    agent any
    environment{
        REGISTRY_URL = "352708296901.dkr.ecr.eu-central-1.amazonaws.com"
        IMAGE_TAG = "0.0.$BUILD_NUMBER"
        IMAGE_NAME = "shlomigd"
    }
    stages {
        stage('Deploy') {
            steps {
            sh '''
                    aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                    docker build -t   $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG .
                    docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                    '''
            }
        }
    }
}