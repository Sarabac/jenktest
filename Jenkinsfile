pipeline {
    agent any
    triggers { pollSCM('* * * * *') }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Sarabac/jenktest.git',
                branch: 'main'
            }
        }
        stage('First Stage') {
                steps {
                    echo 'Step 1. Hello World'
                    echo 'Step 2 in Stage 1: Whatsup'
                }
        }
        stage('Second Stage') {
            steps {
                echo 'Step 3 in Stage 2: Good'
            }
        }
    }
}
