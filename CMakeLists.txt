cmake_minimum_required(VERSION 3.0.2)
project(conan-ci-cd-training)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(SOURCES src/libA.cpp)
file(GLOB HEADERS include/libA/*)

add_library(libA ${SOURCES} ${HEADERS})

target_include_directories(
    libA PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include/>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)

install(TARGETS libA
        RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}/bin
        LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
        ARCHIVE DESTINATION ${CMAKE_INSTALL_PREFIX}/lib)
install(FILES ${HEADERS}
        DESTINATION ${CMAKE_INSTALL_PREFIX}/include/libA
        PERMISSIONS OWNER_WRITE OWNER_READ GROUP_READ WORLD_READ)
