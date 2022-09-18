pipeline {
    agent any

    stages {
        stage("Generate Ansible Inventory") {
            steps {
                sh 'aws ec2 describe-instances --region eu-north-1 --filters "Name=tag:App,Values=AlonitBot"  --query "Reservations[].Instances[]" > hosts.json'
                sh 'python3 prepare_ansible_inv.py'
            }
        }
        stage('Bot Deploy') {
            steps {
                withCredentials([file(credentialsId: 'bot-machine', variable: 'my-private-key')]) {
                    writeFile file: 'private.pem', text: readFile(my_private_key)

                    sh '''
                    ansible-playbook botDeploy.yaml --extra-vars "bot_image=$BOT_IMAGE" -i hosts --private-key private.pem

                    ls
                    '''
                }
            }
        }
    }
}