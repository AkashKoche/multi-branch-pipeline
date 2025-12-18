pipeline {
    agent any {
    
        stages {
            stage('Checkout') {
                steps {
                    sh "git url: https://github.com/AkashKoche/multi-branch-pipeline.git"
                }
                stage('Deploy') {
                    steps {
                        sh 'python3 tests/test_app.py'
                    }
                }
                stage('Deploy') {
                    steps {
                        sh 'echo "Deploying to production..."'
                    }
                }
            }
        }
    }
}
