#ifndef ASSIGNMENT2_H
#define ASSIGNMENT2_H

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include "newSleep.h"
#include "linkedList.h"
#include "Colour.h"

#define MAX_LINE_LENGTH 256

#define reset "\033[0m"

#define hBlack "\033[40m"
#define hRed "\033[41m"
#define hGreen "\033[42m"
#define hYellow "\033[43m"
#define hBlue "\033[44m"
#define hPurple "\033[45m"
#define hCyan "\033[46m"
#define hWhite "\033[47m"

#define onlyBlack "\033[0;30m"
#define onlyRed "\033[0;31m"
#define onlyGreen "\033[0;32m"
#define onlyYellow "\033[0;33m"
#define onlyBlue "\033[0;34m"
#define onlyMagenta "\033[0;35m"
#define onlyCyan "\033[0;36m"
#define onlyWhite "\033[0;37m"

int lineCount( char* fileName );
void printBeforeColoured( char** array, int lineNum, int row );
void printAfter( char** array, int lineNum, int numLines );
char** readFile( char** array, char *fileName );
void findBrackets( char** array, int numLines, LinkedList* list );
void checkList( char bracket, char** array, LinkedList* list, int count, int numLines, int x );

#endif
