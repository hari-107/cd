pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/hari-107/ci-cd-example.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    ./venv/bin/pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t flask-cicd:latest .
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop flask-cicd || true
                    docker rm flask-cicd || true

                    docker run -d \
                        --name flask-cicd \
                        -p 5000:5000 \
                        flask-cicd:latest
                '''
            }
        }
    }

    post {
        success {
            echo '🚀 Deployment successful!'
        }

        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
