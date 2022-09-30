pipeline {
    agent any

    environment {
        REGISTRY_URL ="352708296901.dkr.ecr.eu-north-1.amazonaws.com/amip-bot"
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
                docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
            post{
            always {
                sh '''
                   docker image prune -f --filter "label=app=bot"
                '''
                }
            }

        }
        stage('Trigger Deploy') {
            steps {
                build job: 'BotDeploy', wait: false, parameters: [
                    string(name: 'BOT_IMAGE_NAME', value: "${REGISTRY_URL}/${IMAGE_NAME}:${IMAGE_TAG}")
                ]
           }
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