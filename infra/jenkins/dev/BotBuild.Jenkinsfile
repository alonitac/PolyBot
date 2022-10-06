pipeline {
    agent {
        docker {
            image '<jenkins-agent-image>'
            args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                echo "building..."
                '''
            }
        }

        stage('Trigger Deploy') {
            steps {
                build job: 'BotDeploy', wait: false, parameters: [
                    string(name: 'BOT_IMAGE_NAME', value: "<image-name>")
                ]
            }
        }
    }
}