pipeline {
    agent any

    environment {

        REGISTRY_URL = "352708296901.dkr.ecr.ap-northeast-1.amazonaws.com"
        IMAGE_TAG = "0.0.${BUILD_NUMBER}"
        IMAGE_NAME = "shay_polybot_ecr"

    }
    stages {
        stage('Build Bot app') {
            steps {
                sh """
                aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                    docker build -t $IMAGE_NAME:$IMAGE_TAG .
                    docker tag $IMAGE_NAME:$IMAGE_TAG $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                    docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
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
    post{
    always{
    sh """

    docker image prune -a -f

    """
    }
    }
}
