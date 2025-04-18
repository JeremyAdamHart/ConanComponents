cmake_minimum_required(VERSION 3.20)

project(waldoProj VERSION 0.0.1)

IF (WIN32)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}" "/DWIN32_LEAN_AND_MEAN /DNOSERVICE /DNOMCX /DNOIME /DNOMINMAX /permissive- /volatile:iso /Zc:preprocessor /Zc:__cplusplus /Zc:externConstexpr /Zc:throwingNew /EHsc" PARENT_SCOPE)
ENDIF()

# add_compile_definitions(USE_GL_4_2)

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON CACHE INTERNAL "") # works

cmake_minimum_required(VERSION 3.20)

add_library(waldo source/waldo.cpp
)
add_library(waldo::waldo ALIAS waldo)

target_sources(waldo PUBLIC FILE_SET waldo_headers TYPE HEADERS BASE_DIRS ./include/ FILES ./include/waldo.hpp)

target_include_directories(waldo PUBLIC ./include/)


# Packages
find_package(qux REQUIRED)
# find_package(glfw3 REQUIRED)
# find_package(glad REQUIRED)
# find_package(glm REQUIRED)

target_link_libraries(waldo PUBLIC qux::quxa qux::quxb)

install(TARGETS waldo FILE_SET waldo_headers)

# add_subdirectory(core)
# add_subdirectory(exts)

# install(TARGETS jorl_core jorl_exts)
# add_subdirectory(examples)
# add_subdirectory(vr)