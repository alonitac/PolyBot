pipeline {
    agent {
        docker {
            label 'polybot_cicd_general'
            image '352708296901.dkr.ecr.us-east-1.amazonaws.com/shay-polybot-jenkins-agent:2'
            args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    options {
        buildDiscarder(logRotator(daysToKeepStr: '30'))
        disableConcurrentBuilds()
        timestamps()
    }

    environment {

        REGISTRY_URL = "352708296901.dkr.ecr.us-east-1.amazonaws.com"
        IMAGE_TAG = "0.0.${BUILD_NUMBER}"
        IMAGE_NAME = "shay-polybot-cicd-worker"

    }
    stages {

        stage('Worker Bot app') {
            options {
                timeout(time: 10, unit: 'MINUTES')
            }
            steps {
                sh """
                aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                    docker build -t $IMAGE_NAME:$IMAGE_TAG -f services/worker/Dockerfile .
                    docker tag $IMAGE_NAME:$IMAGE_TAG $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                    docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                """
            }
        }


//         stage('Trigger Deploy') {
//             steps {
//                 build job: 'workerDeploy', wait: false, parameters: [
//                     string(name: 'WORKER_IMAGE_NAME', value: "${REGISTRY_URL}/${IMAGE_NAME}:${IMAGE_TAG}")
//                 ]
//             }
//         }
    }
}