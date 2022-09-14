pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                    aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 352708296901.dkr.ecr.eu-central-1.amazonaws.com
                    docker build -t shlomigd:0.0.$BUILD_TAG .
                    docker tag shlomigd:0.0.$BUILD_TAG 352708296901.dkr.ecr.eu-central-1.amazonaws.com/shlomigd:0.0.$BUILD_TAG
                    docker push 352708296901.dkr.ecr.eu-central-1.amazonaws.com/shlomigd:latest
            }
        }
        stage('Test') {
            steps {
                //
            }
        }
        stage('Deploy') {
            steps {
                //
            }
        }
    }
}