pipeline {
    agent any

    enviroment {
        REGISTRY_URL= "352708296901.dkr.ecr.eu-west-2.amazonaws.com"
        IMAGE_TAG = "0.0.$BUILD_NUMBER"
        IMAGE_NAME = schiff-repo
    }

    stages {
        stage('ECHOING') {
            steps {
                sh 'echo building...'

        }

//         stage('Build Bot app') {
//             steps {
//                     sh '''
//             aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin $REGISTRY_URL
//             docker build -t $IMAGE_NAME .
//             docker tag $IMAGE_NAME $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
//             docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
//             '''
//             }
//         }

//     }
// }
