    pipeline {
        agent {
            docker {
                // TODO build & push your Jenkins agent image, place the URL here
                image '352708296901.dkr.ecr.eu-north-1.amazonaws.com/jankins-agent-amip'
                args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
            }
        }

            environment {
                REGISTRY_URL ="352708296901.dkr.ecr.eu-north-1.amazonaws.com"
                IMAGE_TAG = "0.0.$BUILD_NUMBER"
                IMAGE_NAME = "amip-ecr-bot-dev1"
            }

                stages {
                    stage ('botbuild') {
                    steps {
                    sh '''
                    aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                    docker build -t $IMAGE_NAME .
                    docker tag $IMAGE_NAME $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                    docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                    '''
                    }
                post{
                always {
                    sh '''
                       docker image prune -f --filter "label=app=bot"

                    '''
                    }
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
        }
    }
