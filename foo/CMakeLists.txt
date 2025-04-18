cmake_minimum_required(VERSION 3.20)

project(fooProj VERSION 0.0.1)

IF (WIN32)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}" "/DWIN32_LEAN_AND_MEAN /DNOSERVICE /DNOMCX /DNOIME /DNOMINMAX /permissive- /volatile:iso /Zc:preprocessor /Zc:__cplusplus /Zc:externConstexpr /Zc:throwingNew /EHsc" PARENT_SCOPE)
ENDIF()

# add_compile_definitions(USE_GL_4_2)

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON CACHE INTERNAL "") # works

cmake_minimum_required(VERSION 3.20)

add_library(foo source/foo.cpp
)
add_library(foo::foo ALIAS foo)

target_sources(foo PUBLIC FILE_SET foo_headers TYPE HEADERS BASE_DIRS ./include/ FILES ./include/foo.hpp)

target_include_directories(foo PUBLIC ./include/)


# Packages
# find_package(glfw3 REQUIRED)
# find_package(glad REQUIRED)
# find_package(glm REQUIRED)

# target_link_libraries(jorl_core PUBLIC glfw)
# target_link_libraries(jorl_core PUBLIC glm::glm)
# target_link_libraries(jorl_core PUBLIC glad::glad)

# install(TARGETS jorl_core FILE_SET jorl_core_headers)

# install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/ DESTINATION "")

install(TARGETS foo FILE_SET foo_headers)

# add_subdirectory(core)
# add_subdirectory(exts)

# install(TARGETS jorl_core jorl_exts)
# add_subdirectory(examples)
# add_subdirectory(vr)