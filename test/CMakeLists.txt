cmake_minimum_required(VERSION 3.20)

project(testProj VERSION 0.0.1)

IF (WIN32)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}" "/DWIN32_LEAN_AND_MEAN /DNOSERVICE /DNOMCX /DNOIME /DNOMINMAX /permissive- /volatile:iso /Zc:preprocessor /Zc:__cplusplus /Zc:externConstexpr /Zc:throwingNew /EHsc" PARENT_SCOPE)
ENDIF()

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON CACHE INTERNAL "") # works

cmake_minimum_required(VERSION 3.20)

add_executable(test main.cpp)

# Packages
find_package(bar REQUIRED)
# find_package(foo REQUIRED)
target_link_libraries(test PUBLIC bar::bara bar::barb) # foo::foo )
