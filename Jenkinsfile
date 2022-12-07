pipeline {
    agent any
    triggers { pollSCM('* * * * *') }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Sarabac/jenktest.git'
            }
        }
        stage('build docker') {
            steps {
                sh 'docker build . -f ./Dockerfile -t lucas/test-calculator '
            }
        }

        stage('run test') {
            steps {
                sh 'docker run -p 8090:8090 -v /var/jenkins_home/reports:/usr/src/build/reports/jacoco/test/html lucas/test-calculator gradle test'
            }
        }
/*
        stage('unit test') {
            steps {
                sh './gradlew test'
            }
        }
        stage('code coverage') {
            steps {
                sh './gradlew test jacocoTestReport'
                publishHTML(target: [
                    reportDir: 'build/reports/jacoco/test/html',
                    reportFiles: 'index.html',
                    reportName: 'JaCoCo Report'
                ])
            }
        }
        stage('check style') {
            steps {
                sh './gradlew checkstyleMain'
                publishHTML(target: [
                    reportDir: 'build/reports/checkstyle',
                    reportFiles: 'main.html',
                    reportName: 'style check'
                ])
            }
        }
        */
    }
}
