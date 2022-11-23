pipeline {
    agent {
        docker {
            // TODO build & push your Jenkins agent image, place the URL here
            image '352708296901.dkr.ecr.eu-central-1.amazonaws.com/yf-bot-reg:latest'
            args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    // options used from jenkins docs - https://www.jenkins.io/doc/book/pipeline/syntax/
    options {
    buildDiscarder(logRotator(daysToKeepStr: '30'))
    disableConcurrentBuilds()
    timestamps()

    }
    // env and image vars
    environment {
    IMAGE_NAME = "yfbot"
    IMAGE_TAG = "0.0.$BUILD_NUMBER"
    WS = "/home/ec2-user/workspace/dev/botBuild/"
    ECR_REGISTRY = "352708296901.dkr.ecr.eu-central-1.amazonaws.com"
    TEAM_EMAIL = 'yuval.fid@gmail.com'

    }

    stages {
        stage('Build') {
            steps {
                // from jenkins demo build
                sh 'echo building...'
                sh '''
                aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin $ECR_REGISTRY
                docker build -t $IMAGE_NAME:$IMAGE_TAG . -f services/bot/Dockerfile

                '''
            }
        }

    stage('Build_part_2') {
        steps {
            sh'''
            docker tag $IMAGE_NAME:$IMAGE_TAG $ECR_REGISTRY/$IMAGE_NAME:$IMAGE_TAG
            docker push $ECR_REGISTRY/$IMAGE_NAME:$IMAGE_TAG
            '''
        }
        // post used from docker docs - https://docs.docker.com/engine/reference/commandline/image_prune/
        //The following removes images created more than 1 week ago for any case.
        post {
            always {
            sh '''
            echo 'One way or another, I have finished'
            docker image prune -a --filter "until=168" -y
            '''
            }
        }
   }


        stage('Trigger Deploy') {
            steps {
                build job: 'botDeploy', wait: false, parameters: [
                    string(name: 'BOT_IMAGE_NAME', value: "${ECR_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}")
                ]
            }
        }
    }
}