pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/leszko/calculator.git',
                branch: 'main'
            }
            stage('First Stage') {
                steps {
                    echo 'Step 1. Hello World'
                }
            }
        }
    }
}
