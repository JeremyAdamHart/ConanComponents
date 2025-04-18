from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class Recipe(ConanFile):
    name = "bar"
    version = "0.0.1"

    exports_sources = "include/*", "source/*", "CMakePresets.json", "CMakeLists.txt"
    generators = "CMakeToolchain", "CMakeDeps"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def layout(self):
        cmake_layout(self)

    # def generate(self):
    #     tc = CMakeToolchain(self)
    #     tc.generate()
    #     deps = CMakeDeps

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def requirements(self):
        self.requires("foo/0.0.1", transitive_headers=True, transitive_libs=True)
        # self.requires("glfw/3.4", transitive_headers=True, transitive_libs=True)
        # self.requires("freetype/2.13.3", transitive_headers=True, transitive_libs=True)
        # self.requires("glad/0.1.36", transitive_headers=True, transitive_libs=True)
        # self.requires("glm/1.0.1", transitive_headers=True, transitive_libs=True)
        # self.requires("stb/cci.20240531", transitive_headers=True, transitive_libs=True)
        # self.requires("tinyply/2.3.4", transitive_headers=True, transitive_libs=True)
        # self.requires("openvr/1.16.8", transitive_headers=True, transitive_libs=True)

    def package_info(self):
        pass
        # self.cpp_info.components["core"].libs = ["jorl_core"]
        # self.cpp_info.components["exts"].libs = ["jorl_exts"]
        # self.cpp_info.components["exts"].requires = ["core"]
        # self.