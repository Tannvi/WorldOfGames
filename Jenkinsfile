pipeline {
    agent any

    environment {
        USER_NAME = 'Tannvi'
        GAME_CHOICE = '2'
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

        stage('Build and Run Docker Compose') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker-compose up --build -d'
                    } else {
                        bat 'docker-compose up --build -d'
                    }
                }
            }
        }

        stage('Wait for Application to Start') {
            steps {
                script {
                    // Delay to allow app startup (adjust if needed)
                    sleep 400
                }
            }
        }

        stage('Check Application Status') {
            steps {
                script {
                    def appRunning = false
                    def retryCount = 0
                    def maxRetries = 10

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
                            sh "docker-compose logs"
                        } else {
                            bat "docker-compose logs"
                        }
                        error 'Application failed to start within the timeout period'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def workspaceDir = pwd()
                    def testScriptPath = "${workspaceDir}/tests/e2e.py"

                    // Check if e2e.py exists before attempting to run it
                    if (fileExists(testScriptPath)) {
                        // Install required Python packages
                        if (isUnix()) {
                            sh 'pip install -r requirements.txt'
                        } else {
                            bat "\"C:\\Users\\91741\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe\" install -r requirements.txt"
                        }

                        // Run tests
                        if (isUnix()) {
                            sh "python ${testScriptPath} http://localhost:5000"
                        } else {
                            bat "\"C:\\Users\\91741\\AppData\\Local\\Programs\\Python\\Python312\\python.exe\" ${testScriptPath} http://localhost:5000"
                        }
                    } else {
                        error "e2e.py not found in workspace/tests directory."
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

    post {
        always {
            script {
                // Ensure that Docker containers are brought down after the job
                if (isUnix()) {
                    sh 'docker-compose down'
                } else {
                    bat 'docker-compose down'
                }
            }
        }
    }
}
