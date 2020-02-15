def docker_runs = [:]  // [id] = [docker_image, profile]

docker_runs["conanio-gcc8"] = ["conanio/gcc8", "linux_gcc_8_x86_64"]
docker_runs["conanio-gcc7"] = ["conanio/gcc7", "linux_gcc_7_x86_64"]

ArrayList line_split(String text) {
  return text.split('\\r?\\n').findAll{it.size() > 0} as ArrayList
}

def organization = "conan-ci-cd-training"
def user_channel = "mycompany/stable"
def config_url = "https://github.com/conan-ci-cd-training/settings.git"

def projects = line_split(readTrusted('dependent-projects.txt')).collect { "${it}@${user_channel}" } // TODO: Get list dynamically

String reference_revision = null
String repository = null
String sha1 = null

def get_stages(id, docker_image, profile, user_channel, config_url) {
  return {
    stage(id) {
      node {
          docker.image(docker_image).inside("--net=host") {
          def scmVars = checkout scm
          def repository = scmVars.GIT_URL.tokenize('/')[3].split("\\.")[0]
          withEnv(["CONAN_USER_HOME=${env.WORKSPACE}/conan_cache"]) {
            def remoteName = "conan-develop"
            def lockfile = "${id}.lock"
            try {
              echo("running ${docker_image}")
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

def stages = [:]
docker_runs.each { id, values ->
    stages[id] = get_stages(id, values[0], values[1], user_channel, config_url)
}

pipeline {
  agent none
  stage("Build + upload") {
    steps {
      script {
        docker_runs = withEnv(["CONAN_HOOK_ERROR_LEVEL=40"]) {
          //parallel stages
        }
      }
    }
  }

  stage("Retrieve and publish build info") {
    agent any
    steps {
      script {
        echo("Retrieve and publish build info")
      }
    }
    post {
      always {
        deleteDir()
      }
    }
  }

  stage("Trigger dependents jobs") {
    agent any
    steps {
      script {
        echo("Trigger dependents jobs")
      }
    }
    post {
      always {
        deleteDir()
      }
    }
  }
}
