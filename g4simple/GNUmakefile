# Example modifications to the Makefile
BINDIR := /nas/longleaf/home/kbhimani/ornl_sims/g4simple/install2/bin
LIBDIR := /nas/longleaf/home/kbhimani/ornl_sims/g4simple/install2/lib
TMPDIR := /nas/longleaf/home/kbhimani/ornl_sims/g4simple/install2/tmp

ifneq ("$(wildcard $(G4INCLUDE)/g4hdf5.hh)","")
  CPPFLAGS += -DGEANT4_USE_HDF5
endif
G4TARGET := g4simple
include $(G4INSTALL)/config/binmake.gmk
