#include "Assignment2.h"

int main( int argc, char **argv )
{
    char *fileName;
    char** array;
    int x, y, numLines;
    LinkedList* list;
    /*taking in command line parameter and assigning them to variables, if no parameter passed, throw error*/
    if ( argc < 2 )
    {
        printf( "Please enter a filename!\n" );
        exit( 0 );
    }
    fileName = argv[1];
    /*counts number of lines in the file*/
    numLines = lineCount( fileName );
    /*assigning memory to the array that will house the data from the file*/
    array = ( char ** )malloc( numLines*sizeof( char * ) );
    for ( x = 0; x < numLines; x++ )
    {
        array[x]= ( char * )malloc( MAX_LINE_LENGTH*sizeof( char ) );
    } 
    /*putting the text from the chosen file into an arrray*/
    array = readFile( array, fileName );
    /*create a linked list that will be used to store data of matched brackets*/
    list = createLinkedList();
    /*calls findBrackets, which does the bulk of the work of finding the brackets*/
    findBrackets( array, numLines, list );
    /*frees the linked list to ensure no memory leaks are present*/
    freeLinkedList( list );
    /*frees the array, one row at a time*/
    for ( y = 0; y < numLines; y++ )
    {
        free( array[y] );
    }
    /*frees the array pointer*/
    free( array );
    return 0;
}

/*PURPOSE OF FUNCTION: Finds all brackets in row, and prints it accordingly, up until a certain line number, which allows a pointer ('^') to be used in between the text file*/
void printBeforeColoured( char** array, int lineNum, int row )
{
    int i, j, y, bracket, bracket1, flag;
    flag = 0;
    /*for each line in the file/array*/
    for ( i = 0; i < lineNum+1; i++ )
    {
        /*for each character in a given line*/
        for ( j = 0; j < strlen( array[i] ); j++ )
        {
            /*if the current line of the text file is less than the line number specified when calling the function*/
            if ( i < lineNum )
            {   
                    /*if a certain character = a given bracket type*/
                    if ( array[i][j] == '<' || array[i][j] == '>' )
                    {
                        /*highlight that character*/
                        changeColourKnown( hGreen );
                        printf( "%c", array[i][j] );
                        /*reset the text to its original colour*/
                        changeColourKnown( reset );
                    }
                    else if ( array[i][j] == '{' || array[i][j] == '}' )
                    {
                        changeColourKnown( hCyan );
                        printf( "%c", array[i][j] );
                        changeColourKnown( reset );
                    }
                    else if ( array[i][j] == '(' || array[i][j] == ')' )
                    {
                        changeColourKnown(hRed);
                        printf("%c", array[i][j]);
                        changeColourKnown(reset);
                    }
                    else if ( array[i][j] == '[' || array[i][j] == ']' )
                    {
                        changeColourKnown( hYellow );
                        printf( "%c", array[i][j] );
                        changeColourKnown( reset );
                    }
                /*if the certain character is not any type of bracket*/
                else
                {
                    /*print them in white*/
                    changeColourKnown( reset );
                    printf( "%c", array[i][j] );
                }
                /*flag onjly = 1 once the first line has been printed, to ensure that there is no newline before the text*/
                flag = 1;
            }
        }
        if ( flag == 1 )
        {
            printf( "\n" );
            flag = 0;
        }
    }
    /*checks current line for a bracket, and if found saves its location in the line in a variable, bracket1*/
    for ( i = 0; i < lineNum+1; i++ )
    {
        for ( j = 0; j < strlen( array[i] ); j++ )
        {
            if ( array[i][j] == '>' || array[i][j] == ']' || array[i][j] == '}' || array[i][j] == ')' )
            {
                bracket1 = j;
            }
        }
    }
    /*checks current line for a bracket, and if found saves its location in the line in a variable, bracket*/
    for ( i = 0; i < lineNum+1; i++ )
    {
        for ( j = 0; j < strlen( array[i] ); j++ )
        {
            if ( array[i][j] == '<' || array[i][j] == '[' || array[i][j] == '{' || array[i][j] == '(' )
            {
                bracket = j;
            }
        }
    }
    /*for all characters in the given line of the text file*/
    for ( y = 0; y < strlen( array[lineNum] ); y++ )
    {
        /*if the row specified when calling the function is greater than the index of the bracket, i.e. the pointer has reached the cloed bracket for that line*/
        if ( row >= bracket1 )
        {
            /*if it is a closed bracket do the following*/
            if ( y == bracket1 )
            {
                if ( array[lineNum][bracket1] == '>' )
                {
                    /*change the colour of the chosen bracket, and reset after printing that character in the different colour*/
                    changeColourKnown(hGreen);
                    printf( "%c", array[lineNum][bracket1] );
                    changeColourKnown( reset );
                }
                if ( array[lineNum][bracket1] == '}' )
                {
                    changeColourKnown( hCyan );
                    printf( "%c", array[lineNum][bracket1] );
                    changeColourKnown( reset );
                }
                if ( array[lineNum][bracket1] == ')' )
                {
                    changeColourKnown( hRed );
                    printf( "%c", array[lineNum][bracket1]);
                    changeColourKnown( reset );
                }
                if ( array[lineNum][bracket1] == ']' )
                {
                    changeColourKnown( hYellow );
                    printf( "%c", array[lineNum][bracket1] );
                    changeColourKnown( reset );
                }
            }
            /*if it is an open bracket do the following*/
            else if ( y == bracket )
            {
                if ( array[lineNum][bracket] == '<' )
                {
                    /*change the colour of the chosen bracket, and reset after printing that character in the different colour*/
                    changeColourKnown( hGreen );
                    printf( "%c", array[lineNum][bracket] );
                    changeColourKnown( reset );
                }
                if ( array[lineNum][bracket] == '{' )
                {
                    changeColourKnown( hCyan );
                    printf( "%c", array[lineNum][bracket] );
                    changeColourKnown( reset );
                }
                if ( array[lineNum][bracket] == '(' )
                {
                    changeColourKnown( hRed );
                    printf( "%c", array[lineNum][bracket] );
                    changeColourKnown( reset );
                }
                if ( array[lineNum][bracket] == '[' )
                {
                    changeColourKnown( hYellow );
                    printf( "%c", array[lineNum][bracket] );
                    changeColourKnown( reset );
                }
            }
            /*if the character is not an open or closed bracket, print in white*/
            else
            {
                changeColourKnown( reset );
                printf( "%c", array[lineNum][y] );
            }                
        }
        /*if we have reached the open bracket, but not yet reached the closed bracket*/
        else if ( row >= bracket && row < bracket1 )
        {
            if ( y == bracket )
            {
                if ( array[lineNum][bracket] == '<' )
                {
                    /*change the colour of only the open bracket but not the closed bracket, and then reset after printing that bracket*/
                    changeColourKnown( onlyBlue );
                    printf( "%c", array[lineNum][bracket] );
                    changeColourKnown( reset );
                }
                if ( array[lineNum][bracket] == '{' )
                {
                    changeColourKnown( onlyBlue );
                    printf( "%c", array[lineNum][bracket] );
                    changeColourKnown(reset);
                }
                if ( array[lineNum][bracket] == '(' )
                {
                    changeColourKnown( onlyBlue );
                    printf( "%c", array[lineNum][bracket] );
                    changeColourKnown( reset );
                }
                if ( array[lineNum][bracket] == '[' )
                {
                    changeColourKnown( onlyBlue );
                    printf( "%c", array[lineNum][bracket] );
                    changeColourKnown( reset );
                }
            }
            /*if the character is not an open bracket, print in white*/
            else
            {
                changeColourKnown( reset );
                printf( "%c", array[lineNum][y] );
            }
        }
        /*if we have not yet reached an open bracket print in white*/
        else
        {
            changeColourKnown( reset );
            printf( "%c", array[lineNum][y] );
        }
    }        
    printf( "\n" );
}

/*PURPOSE OF FUNCTION: Print all lines after the line chosen when calling the function, to allow space for the pointer ('^') in between*/
void printAfter( char** array, int lineNum, int numLines )
{
    int i, j;
    j = lineNum-1;
    /*for all lines after the one chosen when calling the function, print each line with a newline in between*/
    for ( i = j; i < numLines; i++ )
    {
        printf( "%s", array[i] );
        printf( "\n" );
    }
}

/*PURPOSE OF FUNCTION: Reads the file, chosen by the command line parameter, and returns its length*/
int lineCount( char* fileName )
{
    FILE *file;
    char c;
    int count;
    /*open the file in read only mode*/
    file = fopen( fileName, "r" );
    /*print error message if file cannot be opened*/
    if ( file == NULL )
    {
        printf( "Cannot open file!\n" );
        exit( 0 );
    }
    c = fgetc( file );
    /*for each new line in the file, increment the count by one*/
    for ( c = getc( file ); c != EOF; c = getc( file ) )
    {
        if ( c == '\n' )
        {
            count = count + 1;
        }
    }
    /*return the count to be assigned to other variables as the length of the text file*/
    return count;
}

/*PURPOSE OF FUNCTION: Prints the chosen phrase ('^' pointer) and increment it according to the indentNum passed to it. Works inside a for loop*/
void printIndented( int indentNum, char* phrase )
{
    /*prints the phrase, with a certain indent*/
    printf( "\r%*s%s", indentNum, "", phrase );
}

/*PURPOSE OF FUNCTION: Reads a .txt or .c file and stores ints contents in a 2D array*/
char** readFile( char** array, char *fileName )
{
    FILE *file;
    int i;
    i = 0;
    /*open the file in read only mode*/
    file = fopen( fileName, "rb" );
    /*throw error if file cannot be opened*/
    if ( file == NULL )
    {
        printf( "could not open file: %s", fileName );
    }
    /*read through the file, using fgets to store the characters in the file inside of an array*/
    while ( fgets( array[i], MAX_LINE_LENGTH, file ) )
    {
        array[i][strlen( array[i] ) - 1] = '\0';
        i++; 
    }  
    /*close the file to avoid errors*/
    fclose( file );
    /*returns the array back to a variable*/
    return array;
}

/*PURPOSE OF FUNCTION: Checks items in list, if both open and closed brackets are found, remove both of them from the list. If Incorrect bracket appears, throw error to user*/
void checkList( char bracket, char** array, LinkedList* list, int count, int numLines, int x )
{
    char* startBracket;
    /*use peekStart to find the top item in the list*/
    startBracket = peekStart( list );
    /*if the bracket given to the function and the top bracket are a match ('<' and '>') then remove the beracket from the list to show its' pair has been found*/
    if ( strcmp( startBracket, "(" ) == 0 && bracket == ')' )
    {
        removeStart( list );
    }
    if ( strcmp( startBracket, "<" ) == 0 && bracket == '>' )
    {
        removeStart( list );
    }
    if ( strcmp( startBracket, "{" ) == 0 && bracket == '}' )
    {
        removeStart( list );
    }
    if ( strcmp( startBracket, "[" ) == 0 && bracket == ']' )
    {
        removeStart( list );
    }
    else
    {
        /*if the brackets are not a match, print an error, with the expected bracket*/
        if ( strcmp( startBracket, "(" ) == 0 && bracket != ')' )
        {
            changeColourKnown( hRed );
            printIndented( x, "')' expected" );
            changeColourKnown( reset );
            printf( "\n" );
            printAfter( array, count, numLines) ;
            #ifdef STACK
            printLinkedList( list, list->head );
            #endif
            exit( 0 );
        }
        if ( strcmp( startBracket, "<" ) == 0 && bracket != '>' )
        {
            changeColourKnown( hRed );
            printIndented( x, "'>' expected" );
            changeColourKnown( reset );
            printf( "\n" );
            printAfter( array, count, numLines );
            #ifdef STACK
            printLinkedList( list, list->head );
            #endif
            exit( 0 );
        }
        if ( strcmp( startBracket, "{" ) == 0 && bracket != '}' )
        {
            changeColourKnown( hRed );
            printIndented( x, "'}' expected" );
            changeColourKnown( reset );
            printf( "\n" );
            printAfter( array, count, numLines );
            #ifdef STACK
            printLinkedList( list, list->head );
            #endif
            exit( 0 );
        }
        if ( strcmp( startBracket, "[" ) == 0 && bracket != ']' )
        {
            changeColourKnown( hRed );
            printIndented( x, "']' expected" );
            changeColourKnown( reset );
            printf( "\n" );
            printAfter( array, count, numLines );
            #ifdef STACK
            printLinkedList( list, list->head );
            #endif
            exit( 0 );
        }
    }
}

/*PURPOSE OF FUNCTION: Finds brackets in the array, and if open bracket, adds it to a list. If not throws an error to the user*/
void findBrackets( char** array, int numLines, LinkedList* list )
{
    int j, k, x;
    char* lastBracket;
    k = 2;
    /*loops through the array, by coplumn and then row*/
    for ( j = 0; j < numLines; j++ )
    {
        for ( x = 0; x < strlen( array[j] ); x++ )
        {
            /*uses newSleep to refresh and clear the screen, allowing us to print different data and a moving cursor*/
            newSleep( 0.15 );
            system( "clear" );
            /*prints the before code, which at first will be just the first line of code*/
            printBeforeColoured( array, j, x );
            /*prints a cursor, which moves from left to right every cycle of the loop*/
            printIndented( x, "^" );
            printf( "\n" );
            /*if current (next due to system(clear)) bracket is an open bracklet, add that bracket to the list*/
            if ( array[j][x+1] == '<' )
            {
                insertStart( list, "<" );
            }
            /*if current bracket is a closed bracketn without any item in the list, meaning it is incorrectly placed*/
            if ( array[j][x] == '>' )
            {
                if ( list->head == NULL )
                {
                    /*print error message in red, along with resetting the colour and porinting the rest of the file after*/
                    changeColourKnown( hRed );
                    printIndented( x+1, "'<' expected before this" );
                    changeColourKnown( reset );
                    printf( "\n" );
                    printAfter( array, k, numLines );
                    #ifdef STACK
                    printLinkedList( list, list->head );
                    #endif
                    exit( 0 );
                }
                /*check the list for that pair using checkList, which will remove its' pair from the list if correct*/
                else
                {
                    checkList( '>', array, list, k, numLines, x );
                }
            }
            if ( array[j][x+1] == '(' )
            {
                insertStart( list, "(" );
            }
            if ( array[j][x] == ')' )
            {
                if ( list->head == NULL )
                {
                    changeColourKnown( hRed );
                    printIndented( x+1, "'(' expected before this" );
                    changeColourKnown( reset );
                    printf( "\n" );
                    printAfter( array, k, numLines );
                    #ifdef STACK
                    printLinkedList( list, list->head );
                    #endif
                    exit( 0 );
                }
                else
                {
                    checkList( ')', array, list, k, numLines, x );
                }
            }
            if ( array[j][x+1] == '{' )
            {
                insertStart( list, "{" );
            }
            if ( array[j][x+1] == '}' )
            {
                if ( list->head == NULL )
                {
                    changeColourKnown( hRed );
                    printIndented( x+1, "'{' expected before this" );
                    changeColourKnown( reset );
                    printf( "\n" );
                    printAfter( array, k, numLines );
                    #ifdef STACK
                    printLinkedList( list, list->head );
                    #endif
                    exit( 0 );
                }
                else
                {
                    checkList( '}', array, list, k, numLines, x );
                }
            }
            if ( array[j][x+1] == '[' )
            {
                insertStart( list, "[" );
            }
            if ( array[j][x] == ']' )
            {
                if ( list->head == NULL )
                {
                    changeColourKnown( hRed );
                    printIndented( x+1, "'[' expected before this" );
                    changeColourKnown( reset );
                    printf( "\n" );
                    printAfter( array, k, numLines );
                    #ifdef STACK
                    printLinkedList( list, list->head );
                    #endif
                    exit( 0 );
                }
                else
                {
                    checkList( ']', array, list, k, numLines, x );
                }
            }
            printAfter( array, k, numLines );
            #ifdef STACK
            printLinkedList( list, list->head );
            #endif
            if ( j == numLines - 1 )
            {
            }
            /*checks first character on the next line to see if it is a bracket*/
            else if ( array[j][x+1] == '\0'  )
            {
                if ( array[j+1][0] == '<' )
                {
                    insertStart( list, "<" );
                }
                if ( array[j+1][0] == '>' )
                {
                    checkList( '>', array, list, k, numLines, x );
                }
                if ( array[j+1][0] == '(' )
                {
                    insertStart( list, "(" );
                }
                if ( array[j+1][0] == ')' )
                {
                    checkList( ')', array, list, k, numLines, x );
                }
                if ( array[j+1][0] == '{' )
                {
                    insertStart( list, "{" );
                }
                if ( array[j+1][0] == '}' )
                {
                    checkList( '}', array, list, k, numLines, x );
                }
                if ( array[j+1][0] == '[' )
                {
                    insertStart( list, "[" );
                }
                if ( array[j+1][0] == ']' )
                {
                    checkList( ']', array, list, k, numLines, x );
                }
            }
        }
        k++;
    }
    /*checks, if the list is empty at the end of the file, which bracket should be present*/
    if ( list->head != NULL )
    {
        lastBracket = peekStart( list );
        if ( strcmp( lastBracket, "{" ) == 0 )
        {
            printf( "^\n" );
            changeColourKnown( hRed );
            printf( "'}' expected before End of Code\n" );
            changeColourKnown( reset );
        }
        if ( strcmp( lastBracket, "(" ) == 0 )
        {
            printf( "^\n" );
            changeColourKnown( hRed );
            printf( "')' expected before End of Code\n" );
            changeColourKnown( reset );
        }
        if ( strcmp( lastBracket, "[" ) == 0 )
        {
            printf( "^\n" );
            changeColourKnown( hRed );
            printf( "']' expected before End of Code\n" );
            changeColourKnown( reset );
        }
        if ( strcmp( lastBracket, "<" ) == 0 )
        {
            printf( "^\n" );
            changeColourKnown( hRed );
            printf( "'>' expected before End of Code\n" );
            changeColourKnown( reset );
        }
    }
    else
    {
        /*prints success message if there is no bracket missing at the end*/
        changeColourKnown( onlyGreen );
        printf( "All Good!\n" );
        changeColourKnown( reset );
    }
}
