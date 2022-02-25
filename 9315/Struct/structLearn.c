#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Books{
    char title[50];
    char author[50];
    char subject[50];
    int book_id;
};

typedef struct Books *Book;

Book newBook(){
    Book book = malloc(sizeof(Book));
    return book;
}

int main(){
    Book book = newBook();
    strcpy(book->title,"aaa");
    printf("%s\n",book->title);
    free(book);
    return 0;    
}

