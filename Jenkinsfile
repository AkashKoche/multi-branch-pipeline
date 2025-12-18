pipeline {
    agent any {
    
        stages {
            stage('Checkout') {
                steps {
                    sh "git url: https://github.com/AkashKoche/multi-branch-pipeline.git"
                }
                stage('Build') {
                    steps {
                        sh 'echo "Building (test skipped)..."'
                        sh 'python3 -m py_compile src/app.py'
                    }
                }
                stage('Deploy') {
                    steps {
                        sh 'echo "Deploying without tests!"'
                    }
                }
            }
        }
    }
}
