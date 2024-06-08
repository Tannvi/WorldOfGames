pipeline {
    agent any

   environment {
        USER_NAME = 'Tannvi'
        GAME_CHOICE = '1'
        DIFFICULTY_LEVEL = '1'
        MEMORY_GAME_USER_LIST = '1,2,3'
        USER_GUESS = '1'
        POSTGRES_PASSWORD = 'yourpassword'
    }

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

                    // Check if application is running
                    def maxRetries = 20
                    def retryCount = 0
                    def appRunning = false

                    while (retryCount < maxRetries) {
                        if (isUnix()) {
                            appRunning = sh(script: "curl -s -o /dev/null -w '%{http_code}' http://localhost:5000", returnStatus: true) == 200
                        } else {
                            appRunning = bat(script: "curl -s -o NUL -w %%{http_code} http://localhost:5000", returnStatus: true) == 200
                        }
                        if (appRunning) {
                            echo 'Application is running'
                            break
                        } else {
                            echo 'Waiting for application to start...'
                            sleep 5
                            retryCount++
                        }
                    }

                    if (!appRunning) {
                        echo 'Fetching Docker container logs...'
                        if (isUnix()) {
                            sh "docker logs $containerName"
                        } else {
                            bat "docker logs $containerName"
                        }
                        error 'Application failed to start within the timeout period'
                    }

                    // Check if e2e.py exists before attempting to run it
                    if (fileExists("${workspaceDir}/e2e.py")) {
                        // Install required Python packages
                        if (isUnix()) {
                            sh 'pip install -r requirements.txt'
                        } else {
                            bat "\"C:\\Users\\91741\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe\" install -r requirements.txt"
                        }

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
                        sh 'docker login -u tannvi -p Balentine@19'
                        sh 'docker push tannvi/getting-started'
                    } else {
                        // Handle failure (e.g., send notification)
                        echo 'Tests failed. Image not pushed to Docker Hub.'
                    }
                }
            }
        }
    }
}
