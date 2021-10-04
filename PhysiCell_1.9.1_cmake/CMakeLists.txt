cmake_minimum_required (VERSION 3.10)

# put before COMPILER so we can subsitute compiler on command line.
project (mymodel)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

FIND_PACKAGE (OpenMP)
if (OPENMP_FOUND)
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()

#OPTION(BUILD_SHARED_LIBS "Build shared libraries" ON)

# rf. https://cmake.org/cmake/help/v3.0/variable/CMAKE_VERSION.html
set (PhysiCell_VERSION_MAJOR 1)
set (PhysiCell_VERSION_MINOR 9)
set (PhysiCell_VERSION_PATCH 1)

# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/PhysiCellConfig.h.in"
  "${PROJECT_BINARY_DIR}/PhysiCellConfig.h"
  )

# add the binary tree to the search path for include files
# so that we will find PhysiCellConfig.h
include_directories ("${PROJECT_BINARY_DIR}")

include_directories ("${PROJECT_SOURCE_DIR}/BioFVM")
add_subdirectory (BioFVM)
include_directories ("${PROJECT_SOURCE_DIR}/core")
add_subdirectory (core)
include_directories ("${PROJECT_SOURCE_DIR}/modules")
add_subdirectory (modules)
include_directories ("${PROJECT_SOURCE_DIR}/custom_modules")
add_subdirectory (custom_modules)

#set (EXTRA_LIBS ${EXTRA_LIBS} BioFVMFunctions CoreFunctions ModulesFunctions CustomModulesFunctions)
#set (EXTRA_LIBS ${EXTRA_LIBS} CustomModulesFunctions BioFVMFunctions CoreFunctions ModulesFunctions )

file(GLOB SOURCES
    BioFVM/*.h
    BioFVM/*.cpp
    core/*.h
    core/*.cpp
    modules/*.h
    modules/*.cpp
    custom_modules/*.h
    custom_modules/*.cpp
)

# add the executable
#add_executable (PhysiCell main.cpp)
#target_link_libraries (PhysiCell  ${EXTRA_LIBS})
add_executable(mymodel main.cpp ${SOURCES})
