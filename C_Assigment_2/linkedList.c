#include"linkedList.h"

/*PURPOSE OF FUNCTION: Creates a linked list*/
LinkedList* createLinkedList()
{
    /*creating an empty list*/
    LinkedList* list;
    /*allocates space in memory for the list*/
    list = (LinkedList*)malloc(sizeof(LinkedList));
    /*set the head and tail to null to shohw that the list is empty*/
    list->head = NULL;
    list->tail = NULL;
    return list;
}

/*PURPOSE OF FUNCTION: inserts an item at the start of the list*/
void insertStart( LinkedList* list, char *entry )
{
    /*list is empty*/
    void* oldHead = list->head;
    if ( oldHead == NULL )
    {
        /*allocate space in memory for a new node*/
        LinkedListNode *newNode = ( LinkedListNode* )malloc( sizeof( LinkedListNode ) );
        /*give the new node data according to the entry variable supplied to it*/
        newNode->data = entry;
        /*make the new node both the head and the tail*/
        list->head = newNode;
        list->tail = newNode;
        /*free pointer to old head, used to tell if list is empty or not*/
        free( oldHead );
    }
    /*list has one or more elements*/
    else
    {
        /*allocate space in memory for a new node*/
        LinkedListNode *newNode = ( LinkedListNode* )malloc( sizeof( LinkedListNode ) );
        /*give the new node data according to the entry variable supplied to it*/
        newNode->data = entry;
        /*set the the current head's previous as the newnode, set the newnodes next as the current head, set the newnode as the head*/
        list->head->previous = newNode;
        newNode->next = list->head;
        list->head = newNode; 
    }
}

/*PURPOSE OF FUNCTION: Returns the total length of the list*/
int listLength( LinkedListNode* node )
{
    int length = 0;
    /*if there is still a node in the list*/
    if( node != NULL )
    {
        /*recursive call to find the total length of the list and store it in variable length*/
        length = 1 + listLength( ( *node ).next );
    }
    return length;
}

/*PURPOSE OF FUNCTION: Prints the current linked list to the terminal, with a new line in between each node*/
void printLinkedList( LinkedList* list, LinkedListNode* node ) 
{
        /*if there is still a node in the list*/
   	    while ( node != NULL ) 
   	    {
            printf( "\n" );
            /*print the node to the terminal*/
            printf( "%s\n", node->data ); 
            /*move to the next node in the linked list*/
            node = node->next;
   	    }
}

/*PURPOSE OF FUNCTION: Removes the first node in the linked list*/
void removeStart( LinkedList* list )
{
    /*create a temporary node that will become the removed node, and be disjointed and freed from the list*/
    LinkedListNode *temp;
    /*if the list is empty tell the user*/
    if ( list->head == NULL )
    {
        printf( "The list is empty!" );
    }
    /*if there is only one item in the list*/
    if ( list->head == list->tail )
    {
        /*set the head and tail to be null and remove the node*/
        temp = list->head;
        list->head = NULL;
        list->tail = NULL;
    }
    /*if there is more than one item in the list*/
    else
    {
        /*set the node to be removed as the temp*/
        temp = list->head;
        /*set the next node to be the new head*/
        list->head = list->head->next;
    }
    /*free the temporary node as not to cause memory leaks*/
    free( temp );
}

/*PURPOSE OF FUNCTION: Returns the first node in the list*/
char* peekStart( LinkedList* list )
{
    /*create a variable to store the contents of the node*/
    char* startNode;
    /*set variable startNode to the data stored in the first node*/
    startNode = list->head->data;
    /*return the variable*/
    return startNode;
}

/*PURPOSE OF FUNCTION: Frees the memory taken up by the linked list, and every node inside of it*/
void freeLinkedList( LinkedList* list )
{
    /*create a temporary node that will become the node to be freed*/
    LinkedListNode *temp3;
    /*while there is still an item in the list*/
    while ( list->head != NULL )
    {
        /*set the temporary node to be equal to the head*/
        temp3 = list->head;
        /*go to the next node*/
        list->head = list->head->next;
        /*free the temporary node*/
        free( temp3 );
    }
    /*free the pointer to the list itself as to not cause memory leaks*/
    free(list);
}

/*NOTE: List uses char* instead of void* for data type, as it is custom to this assignments purpose.*/
/*NOTE: Functions such as insertLast and removeLast were not included as they were not needed for this assignment*/
