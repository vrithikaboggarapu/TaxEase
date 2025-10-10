pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vrithikaboggarapu/TaxEase.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }

        stage('Run') {
            steps {
                sh 'mvn spring-boot:run'
            }
        }
    }
}
