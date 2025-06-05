# Set the compiler
CXX := g++

# Compiler flags (you can modify as needed)
CXXFLAGS := -Wall -O2

# Source files in the pipeline folder
SRC := $(wildcard pipeline_src/*.cpp)
SRC_DIR := pipeline_src
BIN_DIR := pipeline_bin

# Executable names (same as source files but without .exe extension)
EXE := $(patsubst $(SRC_DIR)/%.cpp,$(BIN_DIR)/%,$(SRC))

# Default target
all: $(BIN_DIR) $(EXE)

# Create the binary directory if it doesn't exist
$(BIN_DIR):
	mkdir -p $(BIN_DIR)

# Rule for compiling each source file into an executable
$(BIN_DIR)/%: $(SRC_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

# Clean rule to remove the compiled executables
clean:
	rm -f $(BIN_DIR)/*