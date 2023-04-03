pipeline {
  agent any
  
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
        build job: 'CronAWSPythonScanner'
      }
    }
  }
}