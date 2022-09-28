pipeline {
    agent any

    stages {
        stage('Build Bot app') {
            steps {
                sh """
                    aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 352708296901.dkr.ecr.ap-northeast-1.amazonaws.com
                    docker build -t shay_polybot_ecr .
                    docker tag shay_polybot_ecr:${BUILD_NUMBER} 352708296901.dkr.ecr.ap-northeast-1.amazonaws.com/shay_polybot_ecr:latest
                    docker push 352708296901.dkr.ecr.ap-northeast-1.amazonaws.com/shay_polybot_ecr:${BUILD_NUMBER}
                """
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
