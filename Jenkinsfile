pipeline {
    agent any
    environment{
        REGISTRY_URL = "352708296901.dkr.ecr.eu-central-1.amazonaws.com"
        IMAGE_TAG = "0.0.$BUILD_NUMBER"
        IMAGE_NAME = "shlomigd"
    }
    stages {
        stage('Build') {
            steps {
            sh '''
                    aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                    docker build -t   $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG .
                    docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                    '''
            }
        }
        stage('Trigger Deploy') {
            steps {
                build job: 'BotDeploy', wait: false, parameters: [
                    string(name: 'BOT_IMAGE_NAME', value: "$REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG")
                ]
            }
    }
        }
         }