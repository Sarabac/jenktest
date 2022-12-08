pipeline {
    agent any
    triggers { pollSCM('* * * * *') }
    stages {
        stage('create report dir') {
            steps {
                sh "mkdir -p /var/reports/$BRANCH_NAME"
                sh "docker volume create jenkins_test_reports_$BRANCH_NAME"
            }
        }
        stage('build docker') {
            steps {
                sh 'docker build . -f ./Dockerfile -t lucas/test-calculator '
            }
        }
        stage('run unit test') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'docker run --rm -p 8090:8090 -v jenkins_test_reports_$BRANCH_NAME:/usr/src/build/reports lucas/test-calculator gradle test'
                }
            }
        }

        stage('run code coverage') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'docker run --rm -p 8090:8090 -v jenkins_test_reports_$BRANCH_NAME:/usr/src/build/reports lucas/test-calculator gradle test jacocoTestReport'
                }
            }
        }

        stage('run style check') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'docker run --rm -p 8090:8090 -v jenkins_test_reports_$BRANCH_NAME:/usr/src/build/reports lucas/test-calculator gradle checkstyleMain'
                }
            }
        }

        stage('publish test reports') {
            steps {
                sh 'docker container run --rm -it -v jenkins_test_reports_$BRANCH_NAME:/from -v jenkins_docker_jenkins-test-report:/to alpine ash -c "cd /from ; cp -av . /to/$BRANCH_NAME"'
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

        post {
            always {
                sh "docker volume rm jenkins_test_reports_$BRANCH_NAME"
                sh 'docker image rm lucas/test-calculator'
            }
        }
}
