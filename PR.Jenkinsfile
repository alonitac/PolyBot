pipeline {
    agent any

    stages {
        stage('Unittest') {
            steps {
                sh '''
                pip3 install -r requirements.txt
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