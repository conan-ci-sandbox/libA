ArrayList line_split(String text) {
  return text.split('\\r?\\n').findAll{it.size() > 0} as ArrayList
}

def organization = "conan-ci-cd-training"
def user_channel = "mycompany/stable"
def config_url = "https://github.com/conan-ci-cd-training/settings.git"
def projects = line_split(readTrusted('dependent-projects.txt')).collect { "${it}@${user_channel}" } // TODO: Get list dynamically

pipeline {
    agent { docker { image 'conanio/gcc8' } }
    stages {
        stage('Build') {
            steps {
                script {
                    try {
                        def scmVars = checkout scm
                        def repository = scmVars.GIT_URL.tokenize('/')[3].split("\\.")[0]
                        withEnv(["CONAN_USER_HOME=${env.WORKSPACE}/conan_cache"]) {
                                sh '''
                                    conan --version
                                    conan config install ${config_url}".toString()
                                    pwd
                                    conan create . mycompany/stable --profile conanio-gcc8
                                    conan search
                                '''
                        }
                    }
                   finally {
                        deleteDir()
                    }
                }
            }
        }
    }
}