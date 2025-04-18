from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class Recipe(ConanFile):
    name = "baz"
    version = "0.0.1"

    exports_sources = "include/*", "source/*", "CMakePresets.json", "CMakeLists.txt"
    generators = "CMakeToolchain", "CMakeDeps"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def requirements(self):
        self.requires("bar/0.0.1", transitive_headers=True, transitive_libs=True)

    def package_info(self):
        pass
