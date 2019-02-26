# General settings
cmake_minimum_required(VERSION 2.6)

# Project settings
project(main)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -std=c11")
include_directories(include)
file(GLOB SOURCES "src/*.c")

# Build
add_executable(${PROJECT_NAME} ${SOURCES})
