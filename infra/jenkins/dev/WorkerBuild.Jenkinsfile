pipeline {
    agent {
        docker {
            label 'general'
            image '352708296901.dkr.ecr.us-east-1.amazonaws.com/shay-polybot-jenkins-agent:1'
            args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    // TODO dev worker build stage
}