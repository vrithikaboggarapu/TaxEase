pipeline {

    agent none   // 👈 No global agent — each stage defines its own

    stages {

        stage('Checkout - Controller') {
            agent { label 'built-in' }   // 👈 Runs on Jenkins Controller (built-in node)
            steps {
                echo '📥 Checking out code on Controller (built-in node)...'
                git branch: 'main', url: 'https://github.com/vrithikaboggarapu/TaxEase.git'

                // Save workspace for next stages on agent
                stash includes: '**', name: 'source_code'
            }
        }

        stage('Set up Python - Agent') {
            agent { label 'win_agent' }   // 👈 Runs on Windows Agent node
            steps {
                echo '🐍 Checking Python on Windows Agent...'
                unstash 'source_code'
                bat 'python --version'
            }
        }

        stage('Install Dependencies - Agent') {
            agent { label 'win_agent' }
            steps {
                echo '📦 Installing dependencies on Windows Agent...'
                unstash 'source_code'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App - Agent') {
            agent { label 'win_agent' }
            steps {
                echo '🚀 Running Flask App on Windows Agent...'
                unstash 'source_code'
                bat 'start python app.py'
            }
        }
    }

    post {
        always {
            echo '📋 Pipeline finished (Controller + Agent setup).'
        }
        failure {
            echo '❌ Build failed.'
        }
        success {
            echo '✅ Build succeeded.'
        }
    }
}
