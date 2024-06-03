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
                    def containerName = 'my-docker-image-test'
                    def workspaceDir = pwd()

                    def args = [
                        "-v \"${workspaceDir}:/app\"",
                        "-v \"${workspaceDir}/Scores.txt:/app/Scores.txt\"",
                        "-d",
                        "-p 5000:5000",
                        "--name $containerName",
                        "my-docker-image"
                    ]

                    def argsString = args.join(' ')

                    if (isUnix()) {
                        sh "docker run ${argsString}"
                    } else {
                        bat "docker run ${argsString}"
                    }

                    // Delay to allow app startup (adjust if needed)
                    sleep 5

                    // Check if e2e.py exists before attempting to run it
                    if (fileExists("${workspaceDir}/e2e.py")) {
                        // Run tests
                        if (isUnix()) {
                            sh "python e2e.py http://localhost:5000"
                        } else {
                            bat "\"C:\\Users\\91741\\AppData\\Local\\Programs\\Python\\Python312\\python.exe\" e2e.py http://localhost:5000"
                        }
                    } else {
                        error "e2e.py not found in workspace."
                    }

                    // Stop the container
                    if (isUnix()) {
                        sh "docker stop $containerName"
                    } else {
                        bat "docker stop $containerName"
                    }
                }
            }
        }

        stage('Finalize (Optional)') {
            steps {
                script {
                    // Get build result (success/failure) from previous stage
                    def testResult = currentBuild.result

                    if (testResult == 'SUCCESS') {
                        // Push image to Docker Hub (replace with your details)
                        sh 'docker login -u tannvi -p Tannvisingh@19'
                        sh 'docker push tannvi/my-docker-image'
                    } else {
                        // Handle failure (e.g., send notification)
                        echo 'Tests failed. Image not pushed to Docker Hub.'
                    }
                }
            }
        }
    }
}

