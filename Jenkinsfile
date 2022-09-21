pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '50'))
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
                docker build -t $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG .
                docker push 352708296901.dkr.ecr.eu-north-1.amazonaws.com/alonit-bot:0.0.$BUILD_NUMBER
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
//     post{
//         always {
//             script {
//              currentBuild.description = ("Branch : ${JOB.branch}\n GitCommiter : ${JOB.commitAuthor}\nGitLastMassage: ${JOB.lastCommitMassage}")
//             }
//         }
//     }
}