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
                    def containerName = 'myt-docker-image-test'
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

                    // Run tests (assuming e2e.py is in the workspace)
                    if (isUnix()) {
                        sh 'python e2e.py http://localhost:5000'
                    } else {
                        bat '"C:\Users\91741\AppData\Local\Programs\Python\Python312\python.exe" e2e.py http://localhost:5000'
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
                        if (isUnix()) {
                            sh 'docker login -u tannvi -p Tannvisingh@19'
                            sh 'docker push tannvi/my-docker-image'
                        } else {
                            bat 'docker login -u tannvi -p Tannvisingh@19'
                            bat 'docker push tannvi/my-docker-image'
                        }
                    } else {
                        // Handle failure (e.g., send notification)
                        echo 'Tests failed. Image not pushed to Docker Hub.'
                    }
                }
            }
        }
    }
}
