pipeline {
  agent any
  options {
    buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '5')
  }
  stages {
    stage('Git Clone') {
      steps {
        cleanWs()
        git branch: 'main', url: 'https://github.com/ascended4/awspythonscanner.git'
      }
    }
    
    stage('Docker Build') {
      steps {
        sh 'docker build -t awspythonscanner:v$BUILD_NUMBER -t awspythonscanner:latest .'
      }
    }

    stage('Invoke Deploy') {
      steps {
        build wait: false, job: 'CronAWSPythonScanner'
      }
    }
  }
}