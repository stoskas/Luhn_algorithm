
#include <stdio.h>
#include <string.h>

struct Foithths{
    int arithmos_mitroou;
    char onoma[25];
    char eponymo[25];
    char patronymo[25];
    char mhtronymo[25];
    char dieuthinsi[40];
    long int stathero_thl;
    long long int kinhto_thl;
    char mathima_epilogis[60];
};

// void printFoithths(struct Foithths foithths){
    
//     printf("Student's id is  : %d\n", foithths.arithmos_mitroou);
//     printf("Student's name is : %s\n", foithths.onoma);
//     printf("Student's surname is  : %s\n", foithths.eponymo);
//     printf("Student's father name is : %s\n", foithths.patronymo);
//     printf("Student's mother name is : %s\n", foithths.mhtronymo);
//     printf("Student's address is : %s\n", foithths.dieuthinsi);
//     printf("Student's phone number is : %lld\n", foithths.stathero_thl);
//     printf("Student's mobile number is : %lld\n", foithths.kinhto_thl);
//     printf("Student's chosen course is : %s\n", foithths.mathima_epilogis);
// }

int main(){

    struct Foithths record[2];

    //1st student's record
    record[0].arithmos_mitroou = 19057;
    strcpy(record[0].onoma, "Stefanos");
    strcpy(record[0].eponymo,"Toskas");
    strcpy(record[0].patronymo,"Nikos");
    strcpy(record[0].mhtronymo,"Eleni");
    strcpy(record[0].dieuthinsi,"A,Papandreoy 56");
    record[0].stathero_thl = 2106830820;
    record[0].kinhto_thl = 6942284017;
    strcpy(record[0].mathima_epilogis,"Prolog");

        //2nd student's record
    record[1].arithmos_mitroou = 19058;
    strcpy(record[1].onoma, "Takis");
    strcpy(record[1].eponymo,"Makis");
    strcpy(record[1].patronymo,"Pantelis");
    strcpy(record[1].mhtronymo,"Marika");
    strcpy(record[1].dieuthinsi,"Eleusinas 62");
    record[1].stathero_thl = 2106523456;
    record[1].kinhto_thl = 6932256543;
    strcpy(record[1].mathima_epilogis,"Prolog");

        //3rd student's record
    record[2].arithmos_mitroou = 19059;
    strcpy(record[2].onoma, "Sakis");
    strcpy(record[2].eponymo,"Dakis");
    strcpy(record[2].patronymo,"Aghsilaos");
    strcpy(record[2].mhtronymo,"Sothria");
    strcpy(record[2].dieuthinsi,"Filolaou 43");
    record[2].stathero_thl = 2106542345;
    record[2].kinhto_thl = 6934567890;
    strcpy(record[2].mathima_epilogis,"Prolog");

    for(i=0; i<3; i++){

    }    
    // printFoithths(Foithths1);

    return 0;
}



