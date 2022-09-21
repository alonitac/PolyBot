pipeline {
    agent {
        docker {
            image '352708296901.dkr.ecr.eu-north-1.amazonaws.com/alonit-jenkins-agent:1'
            args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    options {
        buildDiscarder(logRotator(daysToKeepStr: '30'))
        disableConcurrentBuilds()
        timestamps()
    }

    environment {
        REGISTRY_URL = "352708296901.dkr.ecr.eu-north-1.amazonaws.com"
        IMAGE_TAG = "0.0.$BUILD_NUMBER"
        IMAGE_NAME = "alonit-bot"
    }

    stages {
        stage('Build') {
            options {
                timeout(time: 10, unit: 'MINUTES')
            }

            steps {
                sh '''
                aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''

                withCredentials([string(credentialsId: 'snyk', variable: 'SNYK_TOKEN')]) {
                    sh '''
                    snyk container test $IMAGE_NAME:$IMAGE_TAG --severity-threshold=high --file=Dockerfile
                    '''
                }

                sh '''
                docker tag $IMAGE_NAME:$IMAGE_TAG $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
            post {
                always {
                    sh '''
                    docker image prune -f --filter "until=240h"
                    '''
                }
            }
        }

        stage('Trigger Deploy') {
            steps {
                build job: 'BotDeploy', wait: false, parameters: [
                    string(name: 'BOT_IMAGE_NAME', value: "352708296901.dkr.ecr.eu-north-1.amazonaws.com/alonit-bot:0.0.${BUILD_NUMBER}")
                ]
            }
        }
    }
}