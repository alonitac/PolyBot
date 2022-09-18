pipeline {
    agent any

    stages {
        stage('Build') {
            environment {
                REGISTRY_URL = "352708296901.dkr.ecr.eu-north-1.amazonaws.com"
                IMAGE_NAME = "alonit-bot:0.0.$BUILD_NUMBER"
            }
            steps {
                sh '''
                aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                docker build -t $IMAGE_NAME .
                docker tag $IMAGE_NAME $REGISTRY_URL/$IMAGE_NAME
                docker push $REGISTRY_URL/$IMAGE_NAME
                '''
            }
            post {
                always {
                    sh '''
                        docker rmi $REGISTRY_URL/$IMAGE_NAME
                        docker rmi $IMAGE_NAME

                    '''
                }
            }
        }
        stage('Stage II') {
            steps {
                sh 'echo "stage II done"'
            }
        }
        stage('Stage III ...') {
            steps {
                sh 'echo echo "stage III..."'
            }
        }
    }
}