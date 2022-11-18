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
    IMAGE_NAME = "YF_jenkinsBot"
    IMAGE_TAG = "0.0.$BUILD_NUMBER"
    WORKSPACE = "/var/lib/jenkins/workspace/BotBuild/services"
    ECR_REGISTRY = "352708296901.dkr.ecr.eu-central-1.amazonaws.com/yf-bot-reg"
    TEAM_EMAIL = 'yuval.fid@gmail.com' // email address example

    }

    stages {
        stage('Build') {
            steps {
                // from jenkins demo build
                sh '''
                aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin $ECR_REGISTRY
                cd /home/ec2-user/workspace/dev/botBuild/services/bot/
                docker build -t $IMAGE_NAME:$IMAGE_TAG .

                '''
            }
        }
    // used snyk container test from - https://docs.snyk.io/snyk-cli/cli-reference and https://docs.snyk.io/snyk-cli/commands/container-test
    stage('Snyx Check') {
    steps {
            withCredentials([string(credentialsId: '', variable: '')]) {
                sh 'snyk container test $IMAGE_NAME:$IMAGE_TAG --severity-threshold=high --file=/home/ec2-user/workspace/dev/botBuild/services/bot/Dockerfile'
            }
        }
    }

    stage('Continue_Build_Repost_Status') {
        steps {
            sh'''
            docker tag $IMAGE_NAME:$IMAGE_TAG $REGISTRY/$IMAGE_NAME:$IMAGE_TAG
            docker push $ECR_REGISTRY/$IMAGE_NAME:$IMAGE_TAG
            '''
        }
        // post used from docker docs - https://docs.docker.com/engine/reference/commandline/image_prune/
        //The following removes images created more than 1 week ago for any case, and sends a mail status notification
        post {
            always {
            sh '''
            echo 'One way or another, I have finished'
            docker image prune -a --filter "until=168h"
            '''
            }
         success {
            echo 'I succeeded!'
        }

        failure {
            echo 'I failed :('
            mail to: '$TEAM_EMAIL',
                 subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                 body: "Something is wrong with ${env.BUILD_URL}"
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