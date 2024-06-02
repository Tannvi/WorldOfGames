pipeline {
    agent any  // Run on any available agent

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/Tannvi/WorldOfGames'  // Replace with your details
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t score service:latest .'  // Build the image with tag "score service:latest"
            }
        }

        stage('Run Application (Test)') {
            steps {
                script {
                    def containerName = 'score service-test'
                    docker run(
                        // Mount current directory as /app and a dummy Scores.txt
                        "-v ${pwd()}:/app",
                        "-v ${pwd()}/Scores.txt:/app/Scores.txt",
                        "-d",  // Run in detached mode
                        "-p 5000:5000",  // Map container port 8777 to host port 8777
                        "--name $containerName",
                        "score service:latest"  // Use the built image
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
                        sh 'docker push tannvi/scoreservice:latest'
                    } else {
                        // Handle failure (e.g., send notification)
                        echo 'Tests failed. Image not pushed to Docker Hub.'
                    }
                }
            }
        }
    }
}
