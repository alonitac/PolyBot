pipeline {
    agent any

    stages {
        stage('Unittest') {
            when { changeRequest() }
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