pipeline {
    agent any

    stages {
        stage('Unittest') {
            steps {
                sh """
                pip3 install pytest==7.1.3
                pip3 install unittest2~=1.1.0
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