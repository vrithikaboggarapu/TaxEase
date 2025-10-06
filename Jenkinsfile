pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                bat """
                if exist out rmdir /s /q out
                mkdir out
                echo Installing dependencies...
                python -m venv venv
                .\\venv\\Scripts\\pip install -r requirements.txt
                """
            }
        }
        stage('Run') {
            steps {
                bat """
                echo Running TaxEase application...
                .\\venv\\Scripts\\python app.py
                echo Build_OK > artifact.txt
                """
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'artifact.txt, out/**'
        }
    }
}
