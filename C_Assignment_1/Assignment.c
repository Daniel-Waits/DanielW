#include "Assignment.h"
#include "Colour.h"

int stringCompare( char str1[], char str2[] );
char* replacePhrase(char* strPhrase, char* strToReplace, char* strReplaceWith );
void printIndented( int indentNum, char* phrase1 );
int search( char[], char[] );
void outputColour( char* phrase, char* strReplaceWith, char* colourChosen, int colourType ); 
/* [FOR COLOURTYPE] underline = 0, highlight = 1*/

int main( int argc, char** argv )
{
    char* strPhrase;
    char* strToReplace;
    char* strReplaceWith;
    char* colourOne;
    char* colourTwo;
    char* replacedPhrase;
    int timer, length, location, position;
    /*taking in command line parameters and assigning them to variables*/
    strPhrase = argv[1];
    strToReplace = argv[2];
    strReplaceWith = argv[3];
    colourOne = argv[4];
    colourTwo = argv[5];
    replacedPhrase = replacePhrase( strPhrase, strToReplace, strReplaceWith );
    /*find length of the replaced phrase*/
    length = strlen( replacedPhrase );
    system( "clear" );
    printf( "replace: %s -> %s\n\n", strToReplace, strReplaceWith );
    printf( "%s\n", strPhrase );
    /*finds the location of the word in the sentence and stores it in a variable*/
    location = search( strPhrase, strToReplace );
    if( location == -1 )
    {
        printf( "\nNot Found!" );
    }
    else
        position = ( location );
    /*starts timer of length of the new phrase, in order to create visual interface*/
    for( timer = 0; timer <=length-1; timer++ )
    {
        changeColour( colourOne );
        /*prints no match for all lengths less than length of the replaced phrase*/
        if ( timer <= length )
        {
            changeColourKnown( onlyRed );
            printIndented( timer, "^no match" );
            fflush( stdout );
            /*add one second to allow user interface to sweep the screen*/
            sleep( 1 );
        }
        /*if the end of the phrase has been reached*/
        if ( timer == length-1 )
        {
            changeColourKnown( onlyCyan );
            printIndented( timer, "^END     " );
            fflush( stdout );
            /*add one second to allow user interface to sweep the screen*/
            sleep( 1 );
        }
        /*if ^ reaches the chosen word*/
        if( timer == position-1 )
        {  
            /*clear screen in order to print new phrase to screen*/
            system( "clear" );
            /*resetting colour*/
            changeColourKnown( reset );
            printf( "replace: %s -> %s\n\n", strToReplace, strReplaceWith );
            /*change the colour to the colour chosen in the command line*/
            changeColour( colourTwo );
            /*print the phrase with the chosen word as highlighted*/
            outputColour( replacedPhrase, strReplaceWith, colourTwo, highlight );
            printf( "%s\n", replacedPhrase );
            timer = timer + 1;
            changeColourKnown( onlyGreen );
            /*update ^ to say replaced when word is replaced*/
            printIndented( timer, "^replaced" );
            free( replacedPhrase );
            fflush( stdout );
            sleep( 1 );
            timer = timer + strlen( strReplaceWith )-1;
        }
    }    
    /*final clear of screen to allow final phrases to be printed*/
    system( "clear" );
    replacedPhrase = replacePhrase( strPhrase, strToReplace, strReplaceWith );
    /*printing final phrase with underlined chosen word*/
    outputColour( strPhrase, strToReplace, colourOne, underline );
    printf( "%s\n", strPhrase );
    /*prionting final phrase with underlined chosen word*/
    outputColour( replacedPhrase, strReplaceWith, colourTwo, underline );
    printf( "%s\n", replacedPhrase );
    /*setting index from makefile input, to print the index of the chosen word to the user*/
    #ifdef INDEX
    printf("Index = %d\n", location);
    #endif
    /*freeing malloc'd char*/
    free( replacedPhrase );
    /*reset colour*/
    changeColourKnown( reset );
    return( 0 );
}

/*PURPOSE OF FUNCTION: To take in the phrase, word to replace, and word being replaced, and returns the phrase with these words swapped*/
/*Code adapted from - 'https://stackoverflow.com/questions/27160073/replacing-words-inside-string-in-c'*/
char* replacePhrase( char* strPhrase, char* strToReplace, char* strReplaceWith )
{
    char* replacedPhrase;
    char* toReplacePtr;
    /*allocating memory to the replaced phrase*/
    replacedPhrase = ( char* ) calloc( strlen( strPhrase )-strlen( strToReplace )+strlen( strReplaceWith )+1 , sizeof(char*));
    toReplacePtr = replacedPhrase;
    *replacedPhrase = 0;
    /*while the phrase still has characters in it*/
    while( *strPhrase )
    {
        if( !strncmp( strPhrase, strToReplace, strlen( strToReplace ) ) )
        {
            /*concatenate the word being replaced with the new phrase pointer*/
            strcat( toReplacePtr, strReplaceWith );
            strPhrase += strlen( strToReplace );
            toReplacePtr += strlen( strReplaceWith );
        }
        else
        {
            /*copy the phrase pointer to point to replaced phrase pointer*/
            *toReplacePtr = *strPhrase;
            toReplacePtr++;
            strPhrase++;
        }
    }
    *toReplacePtr = 0;
    return replacedPhrase;
}

/*PURPOSE OF FUNCTION: To take in an integer, being the number of spaces to insert before a chosen phrase*/
void printIndented( int indentNum, char* phrase1 )
{
    /*replaces every new print, adds spaces before phrase*/
    printf( "\r%*s%s", indentNum, "", phrase1 );
}

/*PURPOSE OF FUNCTION: Finds index of word inside a phrase*/
/*Code adapted from - 'http://www.c4learn.com/c-programs/c-program-to-find-substring-of-string.html'*/
int search( char strPhrase[], char str[] ) 
{
    int i, j, firstOccurance;
    i = 0;
    j = 0;
    /*while the phrase has not reached a null terminator - end of string*/
    while ( strPhrase[i] != '\0' ) 
    {
        /*if word isnt yet found and isnt end of string*/
        while ( strPhrase[i] != str[0] && strPhrase[i] != '\0' )
        {
            /*cycle through string*/
            i++;
        }
        /*word isnt found - end of string*/
        if ( strPhrase[i] == '\0' )
        {
            printf("-1");
        }
        firstOccurance = i;
            /*if first letter of word is found and not end of string*/
            while ( strPhrase[i] == str[j] && strPhrase[i] != '\0' && str[j] != '\0' ) 
            {
                /*cycle through string and word*/
                i++;
                j++;
            }
        /*word not found - end of string*/
        if ( strPhrase[i] == '\0' )
        {
            printf("-1");
        }
        /*if word ends - word found*/
        if ( str[j] == '\0' )
        {
            /*return index of the word in string*/
            return firstOccurance;
        }
 
        i = firstOccurance + 1;
        j = 0;
    }
    return 0;
}

/*PURPOSE OF FUNCTION: To compare two strings - returns 1 if same, 0 if not same*/
int stringCompare( char* str1, char* str2 )  
{
    int boolean;
    int i = 0;
    int flag = 0;
    /*while strings do not equal the null terminator - arent finished*/
    while( str1[i] != '\0' && str2[i] != '\0' ) 
    {
        if( str2[i] != str2[i] ) 
        {
            /*flag showing not same*/
            flag = 1;
        }
        /*cycles through characters in strings until they match (or dont match)*/
        i++;
    }
    /*if flag = 0 (not not same), and words are ended (null terminator)*/
    if( flag == 0 && str1[i] == '\0' && str2[i] == '\0' )
        /*boolean = 1 meaning words are the same*/
        boolean = 1;
    else
        boolean = 0;
    return boolean;
}

/*PURPOSE OF FUNCTION: To split the string on " " (space) taking each separate word and putting each in a separate variable. If that word = the chosen word, change the colour of only that word and print all.*/
void outputColour( char* phrase, char* strReplaceWith, char* colourChosen, int colourType )
{
    char* strRef[256];
    int i;
    int count = 0;

    /*split string on spaces*/
    strRef[0] = strtok( phrase, " " );
    for( i = 1; i<256; i++ )
    {
        /*for every word, put in different variable inside array of strRef*/
        strRef[i] = strtok( NULL, " " );
    }
    for( i = 0; i<256; i++ )
    {
        /*gets count for finding how many words are in the string*/
        if ( strRef[i] == NULL )
        {
            
        }
        else
        {
             count = i+1;
        }
    }
    for( i = 0; i<count; i++ )
    {
        /*prints the chosen word in chosen colour, and other words in normal colour*/
        if( ( stringCompare( strRef[i], strReplaceWith ) == 1 ) ) 
        {
            if( colourType == underline )
            {
                changeColour( colourChosen );
                printf( "%s", strRef[i] );
                changeColourKnown( reset );
                printf( " " );
            
            }
            else
            {
                changeColourHighlight( colourChosen );
                printf( "%s", strRef[i] );
                changeColourKnown( reset );
                printf( " " );
            }
        }
        else
        {
            changeColourKnown( reset );
            printf( "%s ", strRef[i] );
        }
    }
    printf( "\r" );
}
