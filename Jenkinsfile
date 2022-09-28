pipeline {
    agent {
    docker {
        image '352708296901.dkr.ecr.eu-central-1.amazonaws.com/shlomigd-jenkins-agent:1'
        args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment{
        REGISTRY_URL = "352708296901.dkr.ecr.eu-central-1.amazonaws.com"
        IMAGE_TAG = "0.0.$BUILD_NUMBER"
        IMAGE_NAME = "shlomigd"
    }
    options {
        buildDiscarder(logRotator(daysToKeepStr: '30'))
        disableConcurrentBuilds()
        timestamps()
    }
    stages {
        stage('Build') {
            options {
               timeout(time: 10, unit: 'MINUTES')
            }
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