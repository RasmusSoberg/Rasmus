#include <stdio.h>
#include <stdbool.h>


int main(){

    void users(){
        printf("users\n");

    }

    while(true){
        printf("ADMIN MENU\n");
        printf("1. Remote open door\n");
        printf("2. List all cards in system\n");
        printf("3. Add/remove acce\n");
        printf("4. Exit\n");
        printf("5. FAKE TEST SCAN CARD\n");
        printf("Select option: ");
        int option;
        scanf(" %d", &option);
        if(option == 4){
            break;
        if(option == 1){
            printf("Door opening\n");
        if(option == 2){
            printf("\n");
        }
        }
        }
    } 
    return 0;
}