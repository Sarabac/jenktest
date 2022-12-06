pipeline {
    agent any
    triggers { pollSCM('* * * * *') }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Sarabac/jenktest.git'
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
    }
}
