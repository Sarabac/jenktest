pipeline {
    agent any
    triggers { pollSCM('* * * * *') }
    stages {
        stage('create report dir') {
            steps {
                sh "mkdir /var/reports/$BRANCH_NAME"
            }
        }
        stage('build docker') {
            steps {
                sh 'docker build . -f ./Dockerfile -t lucas/test-calculator '
            }
        }
        stage('run unit test') {
            steps {
                sh 'docker run --rm -p 8090:8090 -v jenkins_docker_jenkins-test-report/$BRANCH_NAME:/usr/src/build/reports lucas/test-calculator gradle test'
            }
        }

        stage('run code coverage') {
            steps {
                sh 'docker run --rm -p 8090:8090 -v jenkins_docker_jenkins-test-report/$BRANCH_NAME:/usr/src/build/reports lucas/test-calculator gradle test jacocoTestReport'
            }
        }

        stage('run style check') {
            steps {
                sh 'docker run --rm -p 8090:8090 -v jenkins_docker_jenkins-test-report/$BRANCH_NAME:/usr/src/build/reports lucas/test-calculator gradle checkstyleMain'
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

    
        post{
            always{
                sh 'docker image rm lucas/test-calculator'
            }
        }
}
