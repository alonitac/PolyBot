pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                printenv
                '''
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