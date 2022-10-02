pipeline {
    agent any
    stages {
        stage ('PR testing') {
//                 failFast true
//                 parallel {
                    stage('Unittest') {
                        steps {
                            sh '''
                            pip3 install -r requirements.txt
                            python3 -m pytest --junitxml results.xml tests
                            '''
                        }
                        post {
                            always {
                                junit allowEmptyResults: true, testResults: 'results.xml'
                            }
                        }
                    }
                    stage('Static code linting') {
                        steps {
                           sh 'python3 -m pylint -f parseable --reports=no *.py'
                        }
                        post {
                            always {
                                sh 'cat pylint.log'
                                recordIssues healthy: 1, tools: [pyLint(name: 'report name', pattern: '**/pylint.log')], unhealthy: 2
                            }
                        }
                    }
//                 }
        }

    }
}