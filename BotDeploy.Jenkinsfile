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
        stage('Ansible Bot Deploy') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'bot-machine', usernameVariable: 'ssh_user', keyFileVariable: 'privatekey')]) {
                    sh '''
                    export ANSIBLE_HOST_KEY_CHECKING=False
                    /var/lib/jenkins/.local/bin/ansible-playbook botDeploy.yaml --extra-vars "bot_image=$BOT_IMAGE" --user=${ssh_user} -i hosts --private-key ${privatekey}

                    '''
                }
            }
        }
    }
}