
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }

    environment {
        APP_NAME = 'jenkins-multibranch-demo'
        PYTHON = 'python'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Building branch: ${env.BRANCH_NAME}"
                echo "Build number: ${env.BUILD_NUMBER}"
            }
        }

        stage('Environment Setup') {
            steps {
                bat '''
                    python --version
                    python -m venv .venv
                    .venv\\Scripts\\python.exe --version
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                bat '''
                    if not exist reports mkdir reports

                    .venv\\Scripts\\python.exe -m unittest discover -s . -p "test_*.py" -v > reports\\test-results.txt 2>&1

                    set TEST_EXIT_CODE=%ERRORLEVEL%
                    type reports\\test-results.txt
                    exit /b %TEST_EXIT_CODE%
                '''
            }
            post {
                always {
                    archiveArtifacts(
                        artifacts: 'reports/test-results.txt',
                        allowEmptyArchive: true
                    )
                }
            }
        }

        stage('Build') {
            steps {
                bat '''
                    if not exist dist mkdir dist

                    tar --exclude=.git --exclude=.venv --exclude=dist -czf "dist/%APP_NAME%-%BUILD_NUMBER%.tar.gz" app.py test_app.py requirements.txt

                    if errorlevel 1 exit /b 1
                '''

                archiveArtifacts(
                    artifacts: 'dist/*.tar.gz',
                    fingerprint: true
                )
            }
        }

        stage('Feature Branch Validation') {
            when {
                not {
                    branch 'main'
                }
            }
            steps {
                echo "Feature branch ${env.BRANCH_NAME} passed CI validation."
                echo 'Production deployment skipped.'
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                echo 'Main branch passed CI validation.'
                echo 'Add your actual production deployment command here.'
            }
        }
    }

    post {
        success {
            echo "SUCCESS: ${env.BRANCH_NAME}"
        }
        failure {
            echo "FAILURE: ${env.BRANCH_NAME}"
        }
        always {
            echo "Pipeline finished for ${env.BRANCH_NAME}"
        }
    }
}
