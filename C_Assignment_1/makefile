CC = gcc
CFLAGS = -Wall -pedantic -ansi -g #-D INDEX=1
OBJ = Assignment.o Colour.o
EXEC = Assignment

$(EXEC) : $(OBJ)
	$(CC) $(OBJ) -o $(EXEC)

all: Assignment.c Colour.c

Assignment.o : Assignment.h
	$(CC) -c Assignment.c $(CFLAGS)

Colour.o : Assignment.h
	$(CC) -c Colour.c $(CFLAGS)

clean:
	rm -f $(EXEC) $(OBJ) 
