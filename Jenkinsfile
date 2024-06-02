pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Use Git step to clone the repository
                git credentialsId: 'your-credentials-id', url: 'https://github.com/Tannvi/WorldOfGames.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker build -t my-docker-image .'
                    } else {
                        bat 'docker build -t my-docker-image .'
                    }
                }
            }
        }

        stage('Run Application (Test)') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'nohup ./run_my_app.sh &'
                    } else {
                        bat 'start /B run_my_app.bat'
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                if (isUnix()) {
                    sh 'docker-compose down'
                } else {
                    bat 'docker-compose down'
                }
            }
        }
    }
}
