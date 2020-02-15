ArrayList line_split(String text) {
  return text.split('\\r?\\n').findAll{it.size() > 0} as ArrayList
}

def organization = "conan-ci-cd-training"
def user_channel = "mycompany/stable"
def config_url = "https://github.com/conan-ci-cd-training/settings.git"
def projects = line_split(readTrusted('dependent-projects.txt')).collect { "${it}@${user_channel}" } // TODO: Get list dynamically

def docker_runs = [:] 
docker_runs["conanio-gcc8"] = ["conanio/gcc8", "conanio-gcc8"]	
//docker_runs["conanio-gcc7"] = ["conanio/gcc7", "conanio-gcc7"]

def get_stages(id, docker_image, profile, user_channel, config_url) {
    return {
        stage(id) {
            node {
                docker.image(docker_image).inside("--net=host") {
                    def scmVars = checkout scm
                    def repository = scmVars.GIT_URL.tokenize('/')[3].split("\\.")[0]
                    withEnv(["CONAN_USER_HOME=${env.WORKSPACE}/conan_cache"]) {
                        try {
                            stage("Configure Conan") {
                                sh "conan --version"
                                sh "conan config install ${config_url}"
                                sh "conan remote add artifactory-develop http://${env.ARTIFACTORY_URL}/artifactory/api/conan/conan-develop"
                                withCredentials([usernamePassword(credentialsId: 'artifactory-credentials', usernameVariable: 'ARTIFACTORY_USER', passwordVariable: 'ARTIFACTORY_PASSWORD')]) {
                                    sh "conan user -p ${ARTIFACTORY_PASSWORD} -r artifactory-develop ${ARTIFACTORY_USER}"
                                }
                            }
                            stage("Create package") {
                                sh "conan create . ${user_channel} --profile conanio-gcc8"
                                sh "conan upload '*' --all -r artifactory-develop --confirm  --force"
                            }
                            stage("Get dependencies and create app") {
                            }
                            stage("Calculate full reference") {
                            }
                            stage("Upload packages") {
                            }
                            stage("Create build info") {
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
}

pipeline {
    agent none
    stages {
        stage('Build') {
            steps {
                script {
                    docker_runs = withEnv(["CONAN_HOOK_ERROR_LEVEL=40"]) {
                        parallel docker_runs.collectEntries { id, values ->
                          def (docker_image, profile) = values
                            ["${id}": get_stages(id, docker_image, profile, user_channel, config_url)]
                        }
                    }
                }
            }
        }        
        // stage('Something') {
        //     steps {
        //         script {
        //             //docker.image("conanio/gcc8").inside("--net=host") {
        //             //}
        //         }
        //     }
        // }
    }
}