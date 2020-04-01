from conans import ConanFile, CMake

class LibA(ConanFile):
    name = "libA"
    version = "1.0"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    generators = "cmake"

    scm = {"type": "git",
           "url": "https://github.com/conan-ci-cd-training/libA.git",
           "revision": "auto"}

    def build(self):
        print("|-----------------------------------------|")
        print("|-------------   BUILDING   --------------|")
        print("|---------------   libA   ----------------|")
        print("|-----------------------------------------|")        
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("LICENSE", dst="licenses")

    def package_info(self):
        self.cpp_info.libs = ["libA",]
