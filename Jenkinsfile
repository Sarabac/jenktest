pipeline {
    agent any
    triggers { pollSCM('* * * * *') }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Sarabac/jenktest.git',
                branch: 'master'
            }
        }
        stage('Compile') {
                steps {
                    sh './gradlew compileJava'
                }
        }
        stage('unit test') {
            steps {
                sh './gradlew test'
            }
        }
        stage('code coverage') {
            steps {
                sh './gradlew test jacocoTestReport'
            }
        }
    }
}
