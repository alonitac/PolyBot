pipeline {
    agent any

    environment {
        REGISTRY_URL= "352708296901.dkr.ecr.eu-west-2.amazonaws.com"
        IMAGE_TAG = "0.0.$BUILD_NUMBER"
        IMAGE_NAME = "schiff-repo"
    }

    stages {
        stage('ECHOING') {
            steps {
                sh 'echo building...'

        }
    }
    

        stage('Build Bot app') {
            steps {
                    sh '''
            aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin $REGISTRY_URL
            docker build -t $IMAGE_NAME .
            docker tag $IMAGE_NAME $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
            docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
            '''
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
