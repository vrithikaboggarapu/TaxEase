pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                // Pull code from your GitHub repo
                git branch: 'main', url: 'https://github.com/vrithikaboggarapu/TaxEase.git'
            }
        }

        stage('Set up Python') {
            steps {
                // Verify Python version
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install all required Python packages
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                // Run your Flask app (make sure app.py is in your repo root)
                sh 'python3 app.py &'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Build failed ❌'
        }
        success {
            echo 'Build succeeded ✅'
        }
    }
}
