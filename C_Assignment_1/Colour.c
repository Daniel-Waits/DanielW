#include "Assignment.h"
#include "Colour.h"

int stringCompare( char str1[], char str2[] );
void changeColour( char* colour )
{
        if ( stringCompare( colour, "black" ) == 1 )
        {
            printf( "%s", black );
        }
        if ( stringCompare( colour, "red" ) == 1 )
        {
            printf( "%s", red );
        }
        if ( stringCompare( colour, "green" ) == 1 )
        {
            printf( "%s", green );
        }
        if ( stringCompare( colour, "yellow" ) == 1 )
        {
            printf( "%s", yellow );
        }
        if ( stringCompare( colour, "blue" ) == 1 )
        {
            printf( "%s", blue );
        }
        if ( stringCompare( colour, "cyan" ) == 1 )
        {
            printf( "%s", cyan );
        }
        if ( stringCompare( colour, "purple" ) == 1 )
        {
            printf( "%s", purple );
        }
        if ( stringCompare( colour, "white" ) == 1 )
        {
            printf( "%s", white );
        }
}

void changeColourHighlight( char* colour )
{
        if ( stringCompare( colour, "black" ) == 1 )
        {
            printf( "%s", hBlack );
        }
        if ( stringCompare( colour, "red" ) == 1 )
        {
            printf( "%s", hRed );
        }
        if ( stringCompare( colour, "green" ) == 1 )
        {
            printf( "%s", hGreen );
        }
        if ( stringCompare( colour, "yellow" ) == 1 )
        {
            printf( "%s", hYellow );
        }
        if ( stringCompare( colour, "blue" ) == 1 )
        {
            printf( "%s", hBlue );
        }
        if ( stringCompare( colour, "purple" ) == 1 )
        {
            printf( "%s", hPurple );
        }
        if ( stringCompare( colour, "cyan" ) == 1 )
        {
            printf( "%s", hCyan );
        }
        if ( stringCompare( colour, "white" ) == 1 )
        {
            printf( "%s", hWhite );
        }
}

void changeColourKnown( char* colour )
{
    printf( "%s", colour );
}
