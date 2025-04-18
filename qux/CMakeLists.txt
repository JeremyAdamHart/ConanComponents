cmake_minimum_required(VERSION 3.20)

project(quxProj VERSION 0.0.1)

IF (WIN32)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}" "/DWIN32_LEAN_AND_MEAN /DNOSERVICE /DNOMCX /DNOIME /DNOMINMAX /permissive- /volatile:iso /Zc:preprocessor /Zc:__cplusplus /Zc:externConstexpr /Zc:throwingNew /EHsc" PARENT_SCOPE)
ENDIF()

# add_compile_definitions(USE_GL_4_2)

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON CACHE INTERNAL "") # works

cmake_minimum_required(VERSION 3.20)

# QUXA --------------------
add_library(quxa quxa/source/quxa.cpp)
add_library(qux::a ALIAS quxa)

target_sources(quxa PUBLIC FILE_SET quxa_headers TYPE HEADERS BASE_DIRS ./quxa/include/ FILES ./quxa/include/quxa.hpp)

target_include_directories(quxa PUBLIC ./quxa/include/)

# Packages
find_package(foo REQUIRED)
target_link_libraries(quxa PUBLIC foo::foo)

# QUXA --------------------
add_library(quxb quxb/source/quxb.cpp)
add_library(qux::b ALIAS quxb)

target_sources(quxb PUBLIC FILE_SET quxa_headers TYPE HEADERS BASE_DIRS ./quxb/include/ FILES ./quxb/include/quxb.hpp)

target_include_directories(quxb PUBLIC ./quxb/include/)

# Packages
find_package(foo REQUIRED)
target_link_libraries(quxb PUBLIC foo::foo)

# -------------------------
install(TARGETS quxa quxb FILE_SET quxa_headers FILE_SET quxb_headers)

# add_subdirectory(core)
# add_subdirectory(exts)

# install(TARGETS jorl_core jorl_exts)
# add_subdirectory(examples)
# add_subdirectory(vr)