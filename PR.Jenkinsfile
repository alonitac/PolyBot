pipeline {
    agent any

    environment {
        REGISTRY_URL = "352708296901.dkr.ecr.eu-north-1.amazonaws.com"
        IMAGE_TAG = "0.0.$BUILD_NUMBER"
        IMAGE_NAME = "alonit-bot"
    }

    stages {
        stage('Unittest') {
            steps {
                sh '''
                pip install -r requirements.txt
                python3 -m pytest --junitxml results.xml tests
                '''
            }

        }
        stage('Functional Test') {
            steps {
                echo 'testing...'
            }
        }
    }
}