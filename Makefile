CXX = g++
CXXFLAGS = -std=c++17 -Wall

# Rule to compile a .cpp file and create an executable with the same base name
# This rule matches any .cpp file and creates an executable without the .cpp extension
%.cpp:
	$(CXX) $(CXXFLAGS) $< -o $(@:.cpp=)

# Clean rule to remove generated executables
clean:
	rm -f *.out *.exe *.out