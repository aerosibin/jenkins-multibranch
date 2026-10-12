
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
        buildDiscarder(logRotator(
            numToKeepStr: '20'
        ))
    }

    environment {
        APP_NAME = 'jenkins-multibranch-demo'
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm

                script {
                    echo "Building branch: ${env.BRANCH_NAME}"
                    echo "Build number: ${env.BUILD_NUMBER}"
                }
            }
        }

        stage('Environment Setup') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv .venv
                    .venv/bin/python -m pip --version
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                sh '''
                    mkdir -p reports

                    .venv/bin/python -m unittest \
                        discover \
                        -s . \
                        -p "test_*.py" \
                        -v 2>&1 | tee reports/test-results.txt
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
                sh '''
                    mkdir -p dist

                    tar --exclude=.git \
                        --exclude=.venv \
                        --exclude=dist \
                        -czf "dist/${APP_NAME}-${BUILD_NUMBER}.tar.gz" \
                        app.py test_app.py requirements.txt
                '''

                archiveArtifacts(
                    artifacts: 'dist/*.tar.gz',
                    fingerprint: true
                )
            }
        }

        stage('Feature Branch Validation') {
            when {
                expression {
                    env.BRANCH_NAME != 'main'
                }
            }
            steps {
                echo "Feature branch ${env.BRANCH_NAME} passed CI validation."
                echo "Deployment is skipped for non-main branches."
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                echo 'Main branch validated.'
                echo 'Production deployment stage is ready.'
                echo 'Configure your deployment command here.'
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
