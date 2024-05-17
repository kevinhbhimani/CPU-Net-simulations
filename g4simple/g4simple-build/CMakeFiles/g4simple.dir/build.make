# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/anaconda3/lib/python3.11/site-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /opt/anaconda3/lib/python3.11/site-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /nas/longleaf/home/kbhimani/ornl_sims/g4simple

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /nas/longleaf/home/kbhimani/ornl_sims/g4simple/g4simple-build

# Include any dependencies generated for this target.
include CMakeFiles/g4simple.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/g4simple.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/g4simple.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/g4simple.dir/flags.make

CMakeFiles/g4simple.dir/g4simple.cc.o: CMakeFiles/g4simple.dir/flags.make
CMakeFiles/g4simple.dir/g4simple.cc.o: /nas/longleaf/home/kbhimani/ornl_sims/g4simple/g4simple.cc
CMakeFiles/g4simple.dir/g4simple.cc.o: CMakeFiles/g4simple.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/nas/longleaf/home/kbhimani/ornl_sims/g4simple/g4simple-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/g4simple.dir/g4simple.cc.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/g4simple.dir/g4simple.cc.o -MF CMakeFiles/g4simple.dir/g4simple.cc.o.d -o CMakeFiles/g4simple.dir/g4simple.cc.o -c /nas/longleaf/home/kbhimani/ornl_sims/g4simple/g4simple.cc

CMakeFiles/g4simple.dir/g4simple.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/g4simple.dir/g4simple.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /nas/longleaf/home/kbhimani/ornl_sims/g4simple/g4simple.cc > CMakeFiles/g4simple.dir/g4simple.cc.i

CMakeFiles/g4simple.dir/g4simple.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/g4simple.dir/g4simple.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /nas/longleaf/home/kbhimani/ornl_sims/g4simple/g4simple.cc -o CMakeFiles/g4simple.dir/g4simple.cc.s

# Object files for target g4simple
g4simple_OBJECTS = \
"CMakeFiles/g4simple.dir/g4simple.cc.o"

# External object files for target g4simple
g4simple_EXTERNAL_OBJECTS =

g4simple: CMakeFiles/g4simple.dir/g4simple.cc.o
g4simple: CMakeFiles/g4simple.dir/build.make
g4simple: /usr/local/lib/libG4Tree.so
g4simple: /usr/local/lib/libG4GMocren.so
g4simple: /usr/local/lib/libG4visHepRep.so
g4simple: /usr/local/lib/libG4RayTracer.so
g4simple: /usr/local/lib/libG4VRML.so
g4simple: /usr/local/lib/libG4OpenGL.so
g4simple: /usr/local/lib/libG4gl2ps.so
g4simple: /usr/local/lib/libG4interfaces.so
g4simple: /usr/local/lib/libG4persistency.so
g4simple: /usr/local/lib/libG4error_propagation.so
g4simple: /usr/local/lib/libG4readout.so
g4simple: /usr/local/lib/libG4physicslists.so
g4simple: /usr/local/lib/libG4parmodels.so
g4simple: /usr/local/lib/libG4FR.so
g4simple: /usr/local/lib/libG4vis_management.so
g4simple: /usr/local/lib/libG4modeling.so
g4simple: /usr/lib/x86_64-linux-gnu/libXm.so
g4simple: /usr/lib/x86_64-linux-gnu/libSM.so
g4simple: /usr/lib/x86_64-linux-gnu/libICE.so
g4simple: /usr/lib/x86_64-linux-gnu/libX11.so
g4simple: /usr/lib/x86_64-linux-gnu/libXext.so
g4simple: /usr/lib/x86_64-linux-gnu/libXt.so
g4simple: /usr/lib/x86_64-linux-gnu/libXmu.so
g4simple: /usr/lib/x86_64-linux-gnu/libGL.so
g4simple: /usr/lib/x86_64-linux-gnu/libGLU.so
g4simple: /opt/anaconda3/lib/libQt5OpenGL.so.5.15.2
g4simple: /opt/anaconda3/lib/libQt5PrintSupport.so.5.15.2
g4simple: /opt/anaconda3/lib/libQt5Widgets.so.5.15.2
g4simple: /opt/anaconda3/lib/libQt5Gui.so.5.15.2
g4simple: /opt/anaconda3/lib/libQt5Core.so.5.15.2
g4simple: /usr/lib/x86_64-linux-gnu/libxerces-c.so
g4simple: /usr/local/lib/libG4run.so
g4simple: /usr/local/lib/libG4event.so
g4simple: /usr/local/lib/libG4tracking.so
g4simple: /usr/local/lib/libG4processes.so
g4simple: /usr/local/lib/libG4analysis.so
g4simple: /usr/local/lib/libhdf5.so
g4simple: /usr/lib/x86_64-linux-gnu/libpthread.a
g4simple: /usr/lib/x86_64-linux-gnu/libdl.a
g4simple: /usr/lib/x86_64-linux-gnu/libm.so
g4simple: /usr/lib/x86_64-linux-gnu/libfreetype.so
g4simple: /usr/lib/x86_64-linux-gnu/libz.so
g4simple: /usr/lib/x86_64-linux-gnu/libexpat.so
g4simple: /usr/local/lib/libG4digits_hits.so
g4simple: /usr/local/lib/libG4track.so
g4simple: /usr/local/lib/libG4particles.so
g4simple: /usr/local/lib/libG4geometry.so
g4simple: /usr/local/lib/libG4materials.so
g4simple: /usr/local/lib/libG4graphics_reps.so
g4simple: /usr/local/lib/libG4intercoms.so
g4simple: /usr/local/lib/libG4global.so
g4simple: /usr/local/lib/libCLHEP-2.4.1.0.so
g4simple: CMakeFiles/g4simple.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/nas/longleaf/home/kbhimani/ornl_sims/g4simple/g4simple-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable g4simple"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/g4simple.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/g4simple.dir/build: g4simple
.PHONY : CMakeFiles/g4simple.dir/build

CMakeFiles/g4simple.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/g4simple.dir/cmake_clean.cmake
.PHONY : CMakeFiles/g4simple.dir/clean

CMakeFiles/g4simple.dir/depend:
	cd /nas/longleaf/home/kbhimani/ornl_sims/g4simple/g4simple-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /nas/longleaf/home/kbhimani/ornl_sims/g4simple /nas/longleaf/home/kbhimani/ornl_sims/g4simple /nas/longleaf/home/kbhimani/ornl_sims/g4simple/g4simple-build /nas/longleaf/home/kbhimani/ornl_sims/g4simple/g4simple-build /nas/longleaf/home/kbhimani/ornl_sims/g4simple/g4simple-build/CMakeFiles/g4simple.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/g4simple.dir/depend

