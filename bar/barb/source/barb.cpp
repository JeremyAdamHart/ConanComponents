#include <barb.hpp>

#include <foo.hpp>
#include <iostream>

void barb(){
    foo();
    std::cout << "barb" << std::endl;
}