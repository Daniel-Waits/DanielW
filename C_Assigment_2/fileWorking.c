#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char** argv)
{
    char* fileNames;
    fileNames = argv[1];
    printf("%s", fileNames);
    return 0;
}
