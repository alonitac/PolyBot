pipeline {
    agent any

    stages {
        stage('Build') {
            environment {
                REGISTRY_URL = "352708296901.dkr.ecr.eu-north-1.amazonaws.com"
                IMAGE_TAG = "0.0.$BUILD_NUMBER"
                IMAGE_NAME = "alonit-bot"
            }
            steps {
                sh '''
                aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                docker build -t $IMAGE_NAME .
                docker tag $IMAGE_NAME $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
        stage('Trigger Deploy') {
            steps {
                script {
                    env.IMAGE = "${REGISTRY_URL}"
                }
                build job: "BotDeploy", wait: false, parameters: [
                    string(name: 'image', value: "${env.IMAGE}")
                ]
            }
        }
        stage('Stage III ...') {
            steps {
                sh 'echo echo "stage III..."'
            }
        }
    }
}