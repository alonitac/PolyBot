pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'echo building...'
                sh 'echo what am i doing?'
            }
        }

        stage('Build Bot app') {
   steps {
       sh '''
            echo "build image"
            aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 352708296901.dkr.ecr.eu-west-2.amazonaws.com

            docker build -t schiff-repo:1 .

            docker tag schiff-repo:1 352708296901.dkr.ecr.eu-west-2.amazonaws.com/schiff-repo:1


            docker push 352708296901.dkr.ecr.eu-west-2.amazonaws.com/schiff-repo:1
       '''
            }
        }
        stage('Stage II') {
            steps {
                sh 'echo "stage II..."'
            }
        }
        stage('Stage III ...') {
            steps {
                sh 'echo echo "stage III..."'
            }
        }
    }
}
