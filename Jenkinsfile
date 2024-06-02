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
                    docker run(
                        // Mount current directory as /app and a dummy Scores.txt
                        "-v ${pwd()}:/app",
                        "-v ${pwd()}/Scores.txt:/app/Scores.txt",
                        "-d",  // Run in detached mode
                        "-p 5000:5000",  // Map container port 8777 to host port 8777
                        "--name $containerName",
                        "my-docker-image"  // Use the built image
                    )

                    // Delay to allow app startup (adjust if needed)
                    sleep 5

                    // Run tests (assuming e2e.py is in the workspace)
                    sh 'python e2e.py http://localhost:5000'

                    // Stop the container
                    sh "docker stop $containerName"
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
