# PhysiCell_Studio: compile a PhysiCell model using CMake.

On Windows:
* install Visual Studio 2019 and the MS C++ compiler.
* install latest CMake

Do something like the following:
```
mkdir build
cd build
cmake .. -G "Visual Studio 16 2019"
cmake --build . --config Release
cd Release
mkdir output
cp -R ..\..\config .
.\mymodel
```

