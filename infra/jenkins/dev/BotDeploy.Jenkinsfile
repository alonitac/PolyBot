pipeline {
    agent {
        docker {
            // TODO build & push your Jenkins agent image, place the URL here
            image '<jenkins-agent-image>'
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
                    string(credentialsId: 'telegram-bot-token', variable: 'TELEGRAM_TOKEN'),
                    file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')
                ]) {
                    sh '''
                    K8S_CONFIGS=infra/k8s

                    # replace placeholders in YAML k8s files
                    bash common/replaceInFile.sh $K8S_CONFIGS/bot.yaml APP_ENV $APP_ENV
                    bash common/replaceInFile.sh $K8S_CONFIGS/bot.yaml BOT_IMAGE $BOT_IMAGE_NAME
                    bash common/replaceInFile.sh $K8S_CONFIGS/bot.yaml TELEGRAM_TOKEN $(echo $TELEGRAM_TOKEN | base64)

                    # apply the configurations to k8s cluster
                    kubectl apply --kubeconfig ${KUBECONFIG} -f $K8S_CONFIGS/bot.yaml
                    '''
                }
            }
        }
    }
}