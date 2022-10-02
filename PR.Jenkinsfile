pipeline {
    agent any

    stages {
        stage('Unittest') {
            steps {
                sh '''
                python3 -m pytest --junitxml results.xml tests
                '''
            }
        }
        stage('Functional test') {
            steps {
                echo "testing"
            }
        }
    }
}