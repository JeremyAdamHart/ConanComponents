#include <baz.hpp>

#include <bar.hpp>
#include <foo.hpp>
#include <iostream>

void baz(){
    foo();
    bar();
    std::cout << "baz" << std::endl;
}