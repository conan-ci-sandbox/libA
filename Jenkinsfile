pipeline {
    agent { docker { image 'conanio/gcc8' } }
    stages {
        stage('build') {
            steps {
                sh 'conan --version'
            }
        }
    }
}