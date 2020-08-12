
#include <stdio.h>
#include <string.h>

struct Foithths{
    int arithmos_mitroou;
    char onoma[25];
    char eponymo[25];
    char patronymo[25];
    char mhtronymo[25];
    char dieuthinsi[40];
    long stathero_thl;
    long kinhto_thl;
    char mathima_epilogis[60];
};

int main(){

    struct Foithths Foithths1;

    Foithths1.arithmos_mitroou = 19057;
    strcpy(Foithths1.onoma, "Stefanos");
    strcpy(Foithths1.eponymo,"Toskas");
    strcpy(Foithths1.patronymo,"Nikos");
    strcpy(Foithths1.mhtronymo,"Eleni");
    strcpy(Foithths1.dieuthinsi,"A,Papandreoy 56");
    Foithths1.stathero_thl = 2106830820;
    Foithths1.kinhto_thl = 6942284017;
    strcpy(Foithths1.mathima_epilogis,"Prolog");
    
    printFoithths(Foithths1);

    return 0;
}

void printFoithths(struct Foithths foithths){
    
    printf("Student's id is  : %d\n", foithths.arithmos_mitroou);
    printf("Student's name is : %s\n", foithths.onoma);
    printf("Student's surname is  : %s\n", foithths.eponymo);
    printf("Student's father name is : %s\n", foithths.patronymo);
    printf("Student's mother name is : %s\n", foithths.mhtronymo);
    printf("Student's address is : %s\n", foithths.dieuthinsi);
    printf("Student's phone number is : %ld\n", foithths.stathero_thl);
    printf("Student's mobile number is : %ld\n", foithths.kinhto_thl);
    printf("Student's chosen course is : %s\n", foithths.mathima_epilogis);
}

