properties([parameters([text('BOT_IMAGE_NAME')])])

pipeline{

    agent any

    stages{

        stage ("Deploy"){
            steps{
                sh """
                echo "stage 1 deploy"
                """
            }

            steps{
                sh """
                echo "stage 2 deploy"
                """
            }
        }
    }
}