cmake_minimum_required (VERSION 3.10)

add_library(BioFVMFunctions BioFVM_MultiCellDS.cpp BioFVM_microenvironment.cpp BioFVM_agent_container.cpp BioFVM_solvers.cpp BioFVM_basic_agent.cpp BioFVM_utilities.cpp BioFVM_matlab.cpp BioFVM_vector.cpp BioFVM_mesh.cpp pugixml.cpp)
