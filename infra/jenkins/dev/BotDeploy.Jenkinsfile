pipeline {
    agent {
        docker {
            image '352708296901.dkr.ecr.eu-north-1.amazonaws.com/alonit-jenkins-agent:latest'
            args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        APP_ENV = "dev"
    }

    parameters {
        string(name: 'BOT_IMAGE_NAME')
    }

    stages {
        stage('Bot Deploy') {
            steps {
                withCredentials([
                    string(credentialsId: 'telegram-bot-token', variable: 'TELEGRAM_TOKEN')
                    file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')
                ]) {
                    sh '''
                    # replace registry url and image name placeholders in yaml
                    sed -i "s/{{APP_ENV}}/$APP_ENV/g" k8s/bot.yaml
                    sed -i "s/{{BOT_IMAGE}}/$BOT_IMAGE_NAME/g" k8s/bot.yaml
                    sed -i "s/{{TELEGRAM_TOKEN}}/$TELEGRAM_TOKEN/g" k8s/bot.yaml

                    # apply the configurations to k8s cluster
                    kubectl apply --kubeconfig ${KUBECONFIG} -f k8s/bot.yaml
                    '''
                }
            }
        }
    }
}