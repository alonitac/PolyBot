pipeline {
    agent any

    environment {
        REGISTRY_URL ="352708296901.dkr.ecr.eu-north-1.amazonaws.com"
        IMAGE_TAG = "0.0.$BUILD_NUMBER"
        IMAGE_NAME = "amip-bot"
    }


    stages {
        stage('Build') {
            steps {
                sh '''
                aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                docker build -t $IMAGE_NAME .
                    docker tag $IMAGE_NAME $REGISTRY_URL/$IMAGE_NAME:IMAGE_TAG
                docker push $REGISTRY_URL/$IMAGE_NAME:IMAGE_TAG
                '''
            }
            post{
            always {
                sh '''
                   docker image prune --filter "label=app=bot"
                '''
            }
            }
        }

        stage('Stage II') {
            steps {
                sh 'echo "stage II Run Lula Run yes"'
            }
        }
        stage('Stage III ...') {
            steps {
                sh 'echo echo "stage III..."'
            }
        }
    }
}