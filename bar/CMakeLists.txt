cmake_minimum_required(VERSION 3.20)

project(barProj VERSION 0.0.1)

IF (WIN32)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}" "/DWIN32_LEAN_AND_MEAN /DNOSERVICE /DNOMCX /DNOIME /DNOMINMAX /permissive- /volatile:iso /Zc:preprocessor /Zc:__cplusplus /Zc:externConstexpr /Zc:throwingNew /EHsc" PARENT_SCOPE)
ENDIF()

# add_compile_definitions(USE_GL_4_2)

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON CACHE INTERNAL "") # works

cmake_minimum_required(VERSION 3.20)

# barA --------------------
add_library(bara bara/source/bara.cpp)
add_library(bar::a ALIAS bara)

target_sources(bara PUBLIC FILE_SET bara_headers TYPE HEADERS BASE_DIRS ./bara/include/ FILES ./bara/include/bara.hpp)

target_include_directories(bara PUBLIC ./bara/include/)

# Packages
find_package(foo REQUIRED)
target_link_libraries(bara PUBLIC foo::foo)

# barA --------------------
add_library(barb barb/source/barb.cpp)
add_library(bar::b ALIAS barb)

target_sources(barb PUBLIC FILE_SET bara_headers TYPE HEADERS BASE_DIRS ./barb/include/ FILES ./barb/include/barb.hpp)

target_include_directories(barb PUBLIC ./barb/include/)

# Packages
find_package(foo REQUIRED)
target_link_libraries(barb PUBLIC foo::foo)

# -------------------------
install(TARGETS bara barb FILE_SET bara_headers FILE_SET barb_headers)

# add_subdirectory(core)
# add_subdirectory(exts)

# install(TARGETS jorl_core jorl_exts)
# add_subdirectory(examples)
# add_subdirectory(vr)