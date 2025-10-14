pipeline {

    agent none   // 👈 No global agent — each stage defines where it runs

    stages {

        stage('Checkout - Controller') {
            agent { label 'master' }   // 👈 Runs on Jenkins Controller
            steps {
                echo '📥 Checking out source code on controller...'
                git branch: 'main', url: 'https://github.com/vrithikaboggarapu/TaxEase.git'

                // Stash the workspace so agent can use it later
                stash includes: '**', name: 'source_code'
            }
        }

        stage('Set up Python - Agent') {
            agent { label 'win_agent' }   // 👈 Runs on Windows Agent
            steps {
                echo '🐍 Checking Python version on agent...'
                // Unstash the source code from controller
                unstash 'source_code'
                bat 'python --version'
            }
        }

        stage('Install Dependencies - Agent') {
            agent { label 'win_agent' }
            steps {
                echo '📦 Installing dependencies on agent...'
                unstash 'source_code'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App - Agent') {
            agent { label 'win_agent' }
            steps {
                echo '🚀 Running Flask app on agent...'
                unstash 'source_code'
                bat 'start python app.py'
            }
        }
    }

    post {
        always {
            echo '📋 Pipeline execution finished (Controller + Agent).'
        }
        failure {
            echo '❌ Build failed.'
        }
        success {
            echo '✅ Build succeeded.'
        }
    }
}
