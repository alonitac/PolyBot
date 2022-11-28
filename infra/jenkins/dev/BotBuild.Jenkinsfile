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
    IMAGE_NAME = "yf-bot-ecr"
    IMAGE_TAG = "0.0.$BUILD_NUMBER"
    WS = "/home/ec2-user/workspace/dev/botBuild/"
    ECR_REGISTRY = "public.ecr.aws/r7m7o9d4"
    TEAM_EMAIL = 'yuval.fid@gmail.com'

    }

    stages {
        stage('Build') {
            steps {
                // from jenkins demo build
                sh 'echo building...'
                sh '''
                aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ECR_REGISTRY
                docker build -t $IMAGE_NAME:$IMAGE_TAG . -f services/bot/Dockerfile


                '''
            }
        }

    stage('tag and push') {
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
            echo 'i have finished the job successfully'
            docker image prune -a -f --filter "until=24"
            '''
            }
        }
   }


        stage('Trigger Deploy ') {
            steps {
                build job: 'botDeploy', wait: false, parameters: [
                    string(name: 'BOT_IMAGE_NAME', value: "${ECR_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}")
                ]
            }
        }
    }
}