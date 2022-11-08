pipeline {
    agent {
        docker {
            // TODO build & push your Jenkins agent image, place the URL here
            image '352708296901.dkr.ecr.us-east-1.amazonaws.com/shay-polybot-jenkins-agent:1'
            args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    options {
        buildDiscarder(logRotator(daysToKeepStr: '30'))
        disableConcurrentBuilds()
        timestamps()
    }

    environment {

        REGISTRY_URL = "352708296901.dkr.ecr.us-east-1.amazonaws.com/shay-polybot-cicd"
        IMAGE_TAG = "0.0.${BUILD_NUMBER}"
        IMAGE_NAME = "shay-polybot-cicd"

    }
    stages {

        stage('Build Bot app') {
            options {
                timeout(time: 10, unit: 'MINUTES')
            }
            steps {
                sh """
                aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                    docker build -t $IMAGE_NAME:$IMAGE_TAG .
                    docker tag $IMAGE_NAME:$IMAGE_TAG $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                    docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                """
            }
        }

        stage('Trigger Deploy') {
            steps {
                build job: 'BotDeploy', wait: false, parameters: [
                    string(name: 'BOT_IMAGE_NAME', value: "<image-name>")
                ]
            }
        }
    }
}