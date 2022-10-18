properties([parameters([text('BOT_IMAGE_NAME')])])

pipeline{

    agent any

    stages{

        stage ("Deploy"){
            step{
                sh """
                echo "stage 1 deploy"
                """
            }

            step{
                sh """
                echo "stage 2 deploy"
                """
            }
        }
    }
}