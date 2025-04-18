from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class Recipe(ConanFile):
    name = "bar"
    version = "0.0.1"

    exports_sources = "bara/include/*", "bara/source/*", "barb/include/*", "barb/source/*", "CMakePresets.json", "CMakeLists.txt"
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

    def package_info(self):
        self.cpp_info.components["bara"].libs = ["bara"]
        self.cpp_info.components["bara"].requires = ["foo::foo"]
        self.cpp_info.components["barb"].libs = ["barb"]
        self.cpp_info.components["bara"].requires = ["foo::foo"]

        self.cpp_info.libs = ["bara", "barb"]
        # self.cpp_info.components["exts"].requires = ["core"]
        # self.