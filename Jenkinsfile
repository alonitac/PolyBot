pipeline {
    agent {
        docker {
            label 'general'
            image '352708296901.dkr.ecr.us-east-1.amazonaws.com/shay-jenkins-agent:1'
            args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    options {
        buildDiscarder(logRotator(daysToKeepStr: '30'))
        disableConcurrentBuilds()
        timestamps()
    }

    environment {

        REGISTRY_URL = "352708296901.dkr.ecr.ap-northeast-1.amazonaws.com"
        IMAGE_TAG = "0.0.${BUILD_NUMBER}"
        IMAGE_NAME = "shay_polybot_ecr"

    }
    stages {

        stage('Build Bot app') {
            options {
                timeout(time: 10, unit: 'MINUTES')
            }
            steps {
                sh """
                aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                    docker build -t $IMAGE_NAME:$IMAGE_TAG .
                    docker tag $IMAGE_NAME:$IMAGE_TAG $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                    docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                """
//                 withCredentials([string(credentialsId: 'SNYK_TOKEN', variable: 'SNYK_TOKEN')]) {
//                     sh """
//                         snyk ignore --id=SNYK-DEBIAN10-EXPAT-3061092
//                         snyk container test  $IMAGE_NAME:$IMAGE_TAG  --severity-threshold=high --file=Dockerfile
//                     """
//                 }
            }

            post{
                always{
                    sh 'docker image prune -a -f --filter "until=30m"'
                }
            }
        }

        stage('Trigger Deploy') {
            steps {
                build job: 'BotDeploy', wait: false, parameters: [
                    string(name: 'BOT_IMAGE_NAME', value: "${REGISTRY_URL}/${IMAGE_NAME}:${IMAGE_TAG}")
                    ]
            }
        }

        stage('Stage III ...') {
            steps {
                sh 'echo echo "stage2..."'
            }
        }
    }
}
