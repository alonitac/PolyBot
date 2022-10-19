properties([parameters([text('BOT_IMAGE_NAME')])])

pipeline {
    agent any

    stages{

        stage("Install Ansible") {
            steps {
                sh 'python3 -m pip install ansible'
                sh '/var/lib/jenkins/.local/bin/ansible-galaxy collection install community.general'
            }
        }
    }
}