pipeline {
    agent any

    stages {
        stage("Generate Ansible Inventory") {
            steps {
                sh 'aws ec2 describe-instances --region eu-north-1 --filters "Name=tag:App,Values=AlonitBot"  --query "Reservations[].Instances[]" > hosts.json'
                sh 'python3 prepare_ansible_inv.py'
                sh '''
                echo "Inventory generated"
                cat hosts
                '''
            }
        }
        stage('Bot Deploy') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'bot-machine', usernameVariable: 'ssh_user', keyFileVariable: 'privatekey')]) {
                    sh '''
                    cp ${privatekey} tmp.pem
                    cat temp.pem
                    ansible-playbook botDeploy.yaml --extra-vars "bot_image=$BOT_IMAGE" --user=${ssh_user} -i hosts --private-key tmp.pem
                    '''
                }
            }
        }
    }
}