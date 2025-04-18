#include <bar.hpp>

#include <foo.hpp>
#include <iostream>

void bar(){
    foo();
    std::cout << "bar" << std::endl;
}