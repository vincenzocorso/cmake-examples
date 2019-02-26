# General settings
cmake_minimum_required(VERSION 2.8)

# Project settings
project(library)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -std=c11")
include_directories(include)
file(GLOB SOURCES "src/*.c")
file(GLOB TESTS "test/*.c")
file(GLOB HEADERS "include/*.h")

# Library
add_library(${PROJECT_NAME} STATIC ${SOURCES})
set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER "${HEADERS}")
if(UNIX)
	install(TARGETS ${PROJECT_NAME}
		ARCHIVE	DESTINATION lib
		LIBRARY DESTINATION lib
		PUBLIC_HEADER DESTINATION include)
endif(UNIX)

# Tests
add_executable(library_test ${TESTS})
set_target_properties(library_test PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/test")
target_link_libraries(library_test ${PROJECT_NAME})

enable_testing()
add_test(NAME library_test COMMAND library_test WORKING_DIRECTORY ${UNIT_TEST_BIN_OUTPUT_DIR})
