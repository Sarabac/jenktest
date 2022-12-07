pipeline {
    agent any
    triggers { pollSCM('* * * * *') }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Sarabac/jenktest.git'
            }
        }

        stage('create test volume'){
            steps {
                sh 'docker volume create calculator-test-result'
            }
        }
        stage("build docker") {
            steps {
                sh 'docker build . -f ./Dockerfile -t lucas/test-calculator '
            }
        }

        stage("run test") {
            steps {
                sh 'docker run -it -p 8090:8090 -v calculator-test-result:/usr/src lucas/test-calculator'
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
