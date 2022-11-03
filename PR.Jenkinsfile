pipeline {
    agent any

    stages {
        stage('Unittest') {
            steps {
                sh """
                pip install pytest==7.1.3
                python3 -m pytest --junitxml results.xml tests
                """
            }

            post {
                always {
                    junit allowEmptyResults: true, testResults: 'results.xml'
                }
            }
        }
        stage('Functional test') {
            steps {
                echo "functional testing "
            }
        }
    }
}