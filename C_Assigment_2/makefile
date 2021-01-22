CC = gcc
CFLAGS = -g -Wall -pedantic -ansi -Werror
OBJ = Assignment2.o newSleep.o linkedList.o Colour.o
OBJ2 = -D STACK
EXEC = program

$(EXEC) : $(OBJ)
	$(CC) $(OBJ) -o $(EXEC)

Assignment2.o : Assignment2.c Assignment2.h newSleep.h
	$(CC) -c Assignment2.c $(CFLAGS) $(OBJ2)

newSleep.o : Assignment2.h
	$(CC) -c newSleep.c $(CFLAGS)

linkedList.o : Assignment2.h
	$(CC) -c linkedList.c $(CFLAGS)

Colour.o : Assignment2.h
	$(CC) -c Colour.c $(CFLAGS)

clean:
	rm -f $(EXEC) $(OBJ) 
