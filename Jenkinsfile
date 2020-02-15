pipeline {
    agent { docker { image 'conanio/gcc8' } }
    stages {
        stage('Build') {
            steps {
                sh '''
                    conan --version
                '''
            }
        }
    }
}