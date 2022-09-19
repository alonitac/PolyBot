pipeline {
    agent any

    stages {
        stage('Install Ansible') {
            stage {
               sh 'python3 -m pip install ansible'
               sh '/var/lib/jenkins/.local/bin/ansible-galaxy collection install community.general'
            }
        }
    }
}