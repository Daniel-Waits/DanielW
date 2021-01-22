#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

typedef struct LinkedListNode {
    char* data;
    struct LinkedListNode* next;
    struct LinkedListNode* previous;
} LinkedListNode;

typedef struct {
    LinkedListNode* head;
    LinkedListNode* tail;
} LinkedList;
 
LinkedList* createLinkedList();
void insertStart( LinkedList* list, char* entry );
int listLength( LinkedListNode* node );
void printLinkedList( LinkedList* list, LinkedListNode* node );
void removeStart( LinkedList* list );
void freeLinkedList( LinkedList* list );
char* peekStart( LinkedList* list );

#endif
